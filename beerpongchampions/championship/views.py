from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import *
from .forms import CreateUserForm, PlayerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max

def logoutUser(request):
    logout(request)
    return redirect('login')

def leaderboard(request):
    leaders = Player.objects.filter(user__groups__name="player").order_by("-points")[:5]
    max_p = Player.objects.filter(user__groups__name="player").aggregate(Max('points'))
    players = Player.objects.filter(user__groups__name="player").order_by("-points")
    for i in range(len(players)):
        players[i].p_points = players[i].points*100/max_p['points__max']
        players[i].save()
    assignPlayerLevel()
    top_amateurs = Player.objects.filter(user__groups__name="player", player_level="Amateur").order_by("-points")[:5]
    top_intermediate = Player.objects.filter(user__groups__name="player", player_level="Intermediate").order_by("-points")[:5]
    top_professional = Player.objects.filter(user__groups__name="player", player_level="Professional").order_by("-points")[:5]
    top_wrld_class = Player.objects.filter(user__groups__name="player", player_level="World Class").order_by("-points")[:5]
    top_champion = Player.objects.filter(user__groups__name="player", player_level="Champion").order_by("-points")[:5]
    context = {'leaders': leaders,
               'top_amateurs':top_amateurs,
               'top_intermediate':top_intermediate,
               'top_professional':top_professional,
               'top_wrld_class':top_wrld_class,
               'top_champion':top_champion}
    return render(request, 'championship/leaderboard.html', context)

def assignPlayerLevel():
    players = Player.objects.filter(user__groups__name="player")
    for i in range(len(players)):
        if players[i].points <= 20:
            players[i].player_level = 'Amateur'
            players[i].save()
        elif 20 < players[i].points <= 40:
            players[i].player_level = 'Intermediate'
            players[i].save()
        elif 40 < players[i].points <= 60:
            players[i].player_level = 'Professional'
            players[i].save()
        elif 60 < players[i].points <= 80:
            players[i].player_level = 'World Class'
            players[i].save()
        elif 80 < players[i].points:
            players[i].player_level = 'Champion'
            players[i].save()

def home(request):
    if request.user.is_authenticated:
        player = request.user.player.name
    else:
        player = "unauthenticated"

    context = {'player':player}
    return render(request, 'championship/home.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/accountView/' + user.username)
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'championship/login.html', context)

def registerPage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'championship/register.html', context)

@login_required(login_url='login')
def accountView(request, pk):
    player = Player.objects.get(user__username=pk)
    if player.profile_pic == None:
        player.profile_pic = "profile_pic_default.png"
    info_graphics = {'Amateur':'lechfree.png',
                     'Intermediate':'desperados.png',
                     'Professional':'tyskie.png',
                     'World Class':'harnas.png',
                     'Champion':'kuflowe.png'}
    graphic = '/static/images/'+ info_graphics[player.player_level]

    if request.method == 'POST':
        return redirect('/accountSettings/' + player.user.username)

    context = {'player':player, 'graphic':graphic}
    return render(request, 'championship/account_view.html', context)

@login_required(login_url='login')
def accountSettings(request, pk):
    player = Player.objects.get(user__username=pk)
    form = PlayerForm(instance=player)

    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()

    context = {'form':form, 'player':player}
    return render(request, 'championship/account_settings.html', context)
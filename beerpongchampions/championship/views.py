from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def leaderboard(request):
    context = {}
    return render(request, 'championship/leaderboard.html', context)

def home(request):
    context = {}
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
    context = {}
    return render(request, 'championship/account_settings.html', context)
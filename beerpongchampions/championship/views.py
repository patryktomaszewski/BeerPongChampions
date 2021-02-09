from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import *
from .forms import CreateUserForm
from django.contrib import messages

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
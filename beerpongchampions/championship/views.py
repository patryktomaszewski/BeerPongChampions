from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import *

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
from django.shortcuts import render

# Create your views here.


def leaderboard(request):
    context = {}
    return render(request, 'championship/leaderboard.html', context)

def home(request):
    context = {}
    return render(request, 'championship/home.html', context)


def login(request):
    context = {}
    return render(request, 'championship/login.html', context)
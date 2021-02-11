from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path('accountView/<pk>', views.accountView, name="accountView"),
    path('accountSettings/<pk>', views.accountSettings, name="accountSettings"),
]
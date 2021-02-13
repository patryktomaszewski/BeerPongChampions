from .models import Player
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['name','email','profile_pic', 'player_level']
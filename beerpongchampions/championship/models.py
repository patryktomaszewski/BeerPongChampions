from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your models here.

class Player(models.Model):
    Level = (
        ('Amateur', 'Amateur'),
        ('Intermediate', 'Intermediate'),
        ('Professional', 'Professional'),
        ('World Class', 'World Class'),
        ('Champion', 'Champion'),
    )

    user = models.OneToOneField(User, null=True, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    points = models.FloatField(null=True, default=0.0)
    p_points = models.FloatField(null=True, default=0.0)
    player_level = models.CharField(max_length=200, null=True, choices=Level, default="Amateur")
    profile_pic = models.ImageField(default="profile_pic_default.png", null=True )


    def __str__(self):
        return self.name

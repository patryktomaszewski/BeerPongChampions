from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Player
from django.dispatch import receiver

#@receiver(post_save, sender=User)
def create_player(sender, instance, created, **kwargs):
    if created:

        group = Group.objects.get(name='player')
        instance.groups.add(group)
        Player.objects.create(user=instance, name=instance.username, email=instance.email)

post_save.connect(create_player, sender=User)
# @receiver(post_save, sender=User)
# def update_player(sender, instance, created, **kwargs):
#     if created == False:
#         instance.profile.save()



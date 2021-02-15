# Generated by Django 3.1.2 on 2021-02-15 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('championship', '0002_auto_20210211_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='p_points',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='profile_pic',
            field=models.ImageField(default='profile_pic_default.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

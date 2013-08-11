
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    phonenumber = models.CharField(blank=True, max_length=50)
    userimage = models.ImageField(blank=True, upload_to='.')

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

admin.site.register(UserProfile)


class PlayerProfile(models.Model):
    user = models.ForeignKey(User, unique=True)


User.playerprofile = property(lambda u: PlayerProfile.objects.get_or_create(user=u)[0])

admin.site.register(PlayerProfile)

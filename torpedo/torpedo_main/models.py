#!/usr/bin/python


from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    phonenumber = models.CharField(blank=True, max_length=50)
    userimage = models.ImageField(blank=True, upload_to='.')

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Section(models.Model):
    group = models.ForeignKey(Group)
    fee = models.FloatField(blank=False, default=0)

    def __unicode__(self):
        return "%s" % self.group.name

Group.section = property(lambda g: Section.objects.get_or_create(group=g)[0])


class MemberProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    payments = models.FloatField(blank=False, default=0)
    memberof = models.ManyToManyField(Section)

    @property
    def memberfee(self):
        fee = 0
        for membership in self.memberof.all():
            fee += membership.fee
        return fee

User.memberprofile = property(lambda u: MemberProfile.objects.get_or_create(user=u)[0])


class PlayerProfile(models.Model):
    user = models.ForeignKey(User, unique=True)


User.playerprofile = property(lambda u: PlayerProfile.objects.get_or_create(user=u)[0])

admin.site.register(UserProfile)
admin.site.register(MemberProfile)
admin.site.register(PlayerProfile)
admin.site.register(Section)

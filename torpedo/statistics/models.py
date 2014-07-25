"""
Statistics model
"""

from datetime import timedelta
from datetime import datetime
from django.db import models
from django.contrib import admin
from django.db.models import Sum


class League(models.Model):
    """
    League is a set of games for a certain period of time.
    """
    name =  models.TextField()
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.name


class Team(models.Model):
    """
    Team is a set of players.
    """
    name =  models.TextField(null=True, blank=True)
    league = models.ForeignKey(League, null=True, blank=True)
    #players = models.ManyToManyField('Player', related_name="teams", null=True, blank=True)

    def __unicode__(self):
        return "Team: %r" % self.name


class Game(models.Model):
    date = models.DateTimeField()
    location = models.TextField(null=True, blank=True)
    home = models.ForeignKey(Team, related_name='home', null=True, blank=True)
    guest = models.ForeignKey(Team, related_name='guest', null=True, blank=True)
    league = models.ForeignKey(League, null=True, blank=True)

    def get_home_name(self):
        return self.home.name

    def set_home_name(self, name):
        home_team = Team.objects.get(name=name)
        self.home = home_team
    home_name = property(get_home_name, set_home_name)

    def get_guest_name(self):
        return self.guest.name

    def set_guest_name(self, name):
        guest_team = Team.objects.get(name=name)
        self.guest = guest_team
    guest_name = property(get_guest_name, set_guest_name)

    @property
    def home_goals(self):
        home_goals = Goal.objects.filter(game=self, team=self.home)
        return home_goals.count()

    @property
    def guest_goals(self):
        return Goal.objects.filter(game=self, team=self.guest).count()

    def __unicode__(self):
        return "Game: %s, %r - %r" % (self.date, self.home, self.guest)

    @property
    def played(self):
        now = datetime.now()
        gamedate = self.date.replace(tzinfo=None)
        return (now-gamedate).total_seconds() > 0

class Player(models.Model):
    number = models.IntegerField(blank=True)
    name = models.TextField(blank=True)
    role= models.TextField(blank=True)
    team=models.ForeignKey(Team, blank=True, null=True)
    league = models.ForeignKey(League, null=True, blank=True)

    @property
    def team_name(self):
        #teams = self.teams.all()
        return self.team.name

    @property
    def goals(self):
        return self.scoring.count()

    @property
    def assists(self):
        return self.assisting.count()

    @property
    def points(self):
        return self.goals + self.assists

    @property
    def penalties(self):
        penalty_time = timedelta()
        for penalty in self.penalty_set.all():
            penalty_time += timedelta(hours=penalty.length.hour,
                                      minutes=penalty.length.minute,
                                      seconds=penalty.length.second,
                                      )
        return penalty_time

    def __unicode__(self):
        return "Player: #%r: %r" % (self.number, self.name)


class Goal(models.Model):
    time = models.TimeField(null=False)
    game = models.ForeignKey(Game)
    team = models.ForeignKey(Team)
    player = models.ForeignKey(Player, related_name='scoring', blank=True, null=True)
    assisting = models.ForeignKey(Player, related_name='assisting', blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    league = models.ForeignKey(League, null=True, blank=True)

    def __unicode__(self):
        return "Goal: %r, %r" % (self.player, self.time)


class Penalty(models.Model):
    time = models.TimeField(null=False)
    length = models.TimeField(null=False) 
    game = models.ForeignKey(Game)
    team = models.ForeignKey(Team)
    player = models.ForeignKey(Player, blank=True, null=True)
    reason = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True)
    league = models.ForeignKey(League, null=True, blank=True)

    def __unicode__(self):
        return "Penalty: %r,  %r" % (self.time, self.player)

admin.site.register(League)
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Goal)
admin.site.register(Penalty)

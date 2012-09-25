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


class Team(models.Model):
    """
    Team is a set of players.
    """
    name =  models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "Team: %r" % self.name

class Game(models.Model):
    date = models.DateTimeField()
    location = models.TextField(null=True, blank=True)
    home = models.ForeignKey(Team, related_name='home', null=True, blank=True)
    guest = models.ForeignKey(Team, related_name='guest', null=True, blank=True)

    def __unicode__(self):
        return "Game: %s, %r - %r" % (self.date, self.home, self.guest)

class Player(models.Model):
    number = models.IntegerField()
    name = models.TextField()
    role= models.TextField(blank=True)
    team = models.ForeignKey(Team, related_name='player')

    @property
    def team_name(self):
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
        from datetime import timedelta
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
    player = models.ForeignKey(Player, related_name='scoring')
    assisting = models.ForeignKey(Player, related_name='assisting')
    note = models.TextField(blank=True)

    def __unicode__(self):
        return "Goal: %r, %r" % (self.player, self.time)

class Penalty(models.Model):
    time = models.TimeField(null=False)
    length = models.TimeField(null=False) 
    game = models.ForeignKey(Game)
    team = models.ForeignKey(Team)
    player = models.ForeignKey(Player)
    reason = models.IntegerField()
    note = models.TextField(blank=True)

    def __unicode__(self):
        return "Penalty: %r,  %r" % (self.time, self.player)

admin.site.register(League)
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Goal)
admin.site.register(Penalty)

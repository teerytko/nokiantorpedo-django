# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'League'
        db.create_table('statistics_league', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('to_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('statistics', ['League'])

        # Adding model 'Team'
        db.create_table('statistics_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('statistics', ['Team'])

        # Adding model 'Game'
        db.create_table('statistics_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('home', self.gf('django.db.models.fields.related.ForeignKey')(related_name='home', to=orm['statistics.Team'])),
            ('guest', self.gf('django.db.models.fields.related.ForeignKey')(related_name='guest', to=orm['statistics.Team'])),
        ))
        db.send_create_signal('statistics', ['Game'])

        # Adding model 'Player'
        db.create_table('statistics_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('role', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='player', to=orm['statistics.Team'])),
        ))
        db.send_create_signal('statistics', ['Player'])

        # Adding model 'Goal'
        db.create_table('statistics_goal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.TimeField')()),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['statistics.Game'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['statistics.Team'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(related_name='scoring', to=orm['statistics.Player'])),
            ('assisting', self.gf('django.db.models.fields.related.ForeignKey')(related_name='assisting', to=orm['statistics.Player'])),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('statistics', ['Goal'])

        # Adding model 'Penalty'
        db.create_table('statistics_penalty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.TimeField')()),
            ('length', self.gf('django.db.models.fields.TimeField')()),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['statistics.Game'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['statistics.Team'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['statistics.Player'])),
            ('reason', self.gf('django.db.models.fields.IntegerField')()),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('statistics', ['Penalty'])


    def backwards(self, orm):
        # Deleting model 'League'
        db.delete_table('statistics_league')

        # Deleting model 'Team'
        db.delete_table('statistics_team')

        # Deleting model 'Game'
        db.delete_table('statistics_game')

        # Deleting model 'Player'
        db.delete_table('statistics_player')

        # Deleting model 'Goal'
        db.delete_table('statistics_goal')

        # Deleting model 'Penalty'
        db.delete_table('statistics_penalty')


    models = {
        'statistics.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'guest': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'guest'", 'to': "orm['statistics.Team']"}),
            'home': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home'", 'to': "orm['statistics.Team']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {})
        },
        'statistics.goal': {
            'Meta': {'object_name': 'Goal'},
            'assisting': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assisting'", 'to': "orm['statistics.Player']"}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['statistics.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scoring'", 'to': "orm['statistics.Player']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['statistics.Team']"}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        'statistics.league': {
            'Meta': {'object_name': 'League'},
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'to_date': ('django.db.models.fields.DateField', [], {})
        },
        'statistics.penalty': {
            'Meta': {'object_name': 'Penalty'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['statistics.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.TimeField', [], {}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['statistics.Player']"}),
            'reason': ('django.db.models.fields.IntegerField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['statistics.Team']"}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        'statistics.player': {
            'Meta': {'object_name': 'Player'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'role': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player'", 'to': "orm['statistics.Team']"})
        },
        'statistics.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['statistics']
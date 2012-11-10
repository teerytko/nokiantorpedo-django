# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'League.from_date'
        db.alter_column('statistics_league', 'from_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'League.to_date'
        db.alter_column('statistics_league', 'to_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Team.name'
        db.alter_column('statistics_team', 'name', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Game.home'
        db.alter_column('statistics_game', 'home_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['statistics.Team']))

        # Changing field 'Game.location'
        db.alter_column('statistics_game', 'location', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Game.guest'
        db.alter_column('statistics_game', 'guest_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['statistics.Team']))

        # Changing field 'Penalty.player'
        db.alter_column('statistics_penalty', 'player_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['statistics.Player'], null=True))

        # Changing field 'Penalty.reason'
        db.alter_column('statistics_penalty', 'reason', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Goal.assisting'
        db.alter_column('statistics_goal', 'assisting_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['statistics.Player']))

        # Changing field 'Goal.note'
        db.alter_column('statistics_goal', 'note', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Goal.player'
        db.alter_column('statistics_goal', 'player_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['statistics.Player']))

    def backwards(self, orm):

        # Changing field 'League.from_date'
        db.alter_column('statistics_league', 'from_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 11, 10, 0, 0)))

        # Changing field 'League.to_date'
        db.alter_column('statistics_league', 'to_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 11, 10, 0, 0)))

        # Changing field 'Team.name'
        db.alter_column('statistics_team', 'name', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Game.home'
        db.alter_column('statistics_game', 'home_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['statistics.Team']))

        # Changing field 'Game.location'
        db.alter_column('statistics_game', 'location', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Game.guest'
        db.alter_column('statistics_game', 'guest_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['statistics.Team']))

        # Changing field 'Penalty.player'
        db.alter_column('statistics_penalty', 'player_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['statistics.Player']))

        # Changing field 'Penalty.reason'
        db.alter_column('statistics_penalty', 'reason', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Goal.assisting'
        db.alter_column('statistics_goal', 'assisting_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['statistics.Player']))

        # Changing field 'Goal.note'
        db.alter_column('statistics_goal', 'note', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Goal.player'
        db.alter_column('statistics_goal', 'player_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['statistics.Player']))

    models = {
        'statistics.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'guest': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'guest'", 'null': 'True', 'to': "orm['statistics.Team']"}),
            'home': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'home'", 'null': 'True', 'to': "orm['statistics.Team']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'statistics.goal': {
            'Meta': {'object_name': 'Goal'},
            'assisting': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'assisting'", 'null': 'True', 'to': "orm['statistics.Player']"}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['statistics.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'scoring'", 'null': 'True', 'to': "orm['statistics.Player']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['statistics.Team']"}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        'statistics.league': {
            'Meta': {'object_name': 'League'},
            'from_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'to_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'statistics.penalty': {
            'Meta': {'object_name': 'Penalty'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['statistics.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.TimeField', [], {}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['statistics.Player']", 'null': 'True', 'blank': 'True'}),
            'reason': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['statistics.Team']"}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        'statistics.player': {
            'Meta': {'object_name': 'Player'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'role': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player'", 'to': "orm['statistics.Team']"})
        },
        'statistics.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['statistics']
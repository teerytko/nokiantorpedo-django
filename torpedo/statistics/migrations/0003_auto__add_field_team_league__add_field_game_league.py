# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Team.league'
        db.add_column('statistics_team', 'league',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['statistics.League'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Game.league'
        db.add_column('statistics_game', 'league',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['statistics.League'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Team.league'
        db.delete_column('statistics_team', 'league_id')

        # Deleting field 'Game.league'
        db.delete_column('statistics_game', 'league_id')


    models = {
        'statistics.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'guest': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'guest'", 'null': 'True', 'to': "orm['statistics.Team']"}),
            'home': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'home'", 'null': 'True', 'to': "orm['statistics.Team']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['statistics.League']", 'null': 'True', 'blank': 'True'}),
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
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['statistics.League']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['statistics']
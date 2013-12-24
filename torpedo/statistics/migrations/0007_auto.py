# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field players on 'Team'
        db.delete_table('statistics_team_players')


    def backwards(self, orm):
        # Adding M2M table for field players on 'Team'
        db.create_table(u'statistics_team_players', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm[u'statistics.team'], null=False)),
            ('player', models.ForeignKey(orm[u'statistics.player'], null=False))
        ))
        db.create_unique(u'statistics_team_players', ['team_id', 'player_id'])


    models = {
        u'statistics.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'guest': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'guest'", 'null': 'True', 'to': u"orm['statistics.Team']"}),
            'home': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'home'", 'null': 'True', 'to': u"orm['statistics.Team']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['statistics.League']", 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'statistics.goal': {
            'Meta': {'object_name': 'Goal'},
            'assisting': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'assisting'", 'null': 'True', 'to': u"orm['statistics.Player']"}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['statistics.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['statistics.League']", 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'scoring'", 'null': 'True', 'to': u"orm['statistics.Player']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['statistics.Team']"}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        u'statistics.league': {
            'Meta': {'object_name': 'League'},
            'from_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'to_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'statistics.penalty': {
            'Meta': {'object_name': 'Penalty'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['statistics.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['statistics.League']", 'null': 'True', 'blank': 'True'}),
            'length': ('django.db.models.fields.TimeField', [], {}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['statistics.Player']", 'null': 'True', 'blank': 'True'}),
            'reason': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['statistics.Team']"}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        u'statistics.player': {
            'Meta': {'object_name': 'Player'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'role': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'statistics.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['statistics.League']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['statistics']
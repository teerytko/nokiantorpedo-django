# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.url'
        db.delete_column(u'events_event', 'url')

        # Adding field 'Event.link'
        db.add_column(u'events_event', 'link',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Event.url'
        db.add_column(u'events_event', 'url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Event.link'
        db.delete_column(u'events_event', 'link')


    models = {
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'events.osallistujatevent': {
            'Meta': {'object_name': 'OsallistujatEvent', '_ormbases': [u'events.Event']},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['events.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'})
        },
        u'events.sportsevent': {
            'Meta': {'object_name': 'SportsEvent'},
            'distance': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['events']
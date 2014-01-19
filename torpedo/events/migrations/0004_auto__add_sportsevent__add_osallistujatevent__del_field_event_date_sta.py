# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SportsEvent'
        db.create_table(u'events_sportsevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('distance', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['SportsEvent'])

        # Adding model 'OsallistujatEvent'
        db.create_table(u'events_osallistujatevent', (
            (u'event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['events.Event'], unique=True, primary_key=True)),
            ('guid', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('author_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'events', ['OsallistujatEvent'])

        # Deleting field 'Event.date_start'
        db.delete_column(u'events_event', 'date_start')

        # Deleting field 'Event.link'
        db.delete_column(u'events_event', 'link')

        # Deleting field 'Event.guid'
        db.delete_column(u'events_event', 'guid')

        # Deleting field 'Event.category'
        db.delete_column(u'events_event', 'category')

        # Deleting field 'Event.author'
        db.delete_column(u'events_event', 'author')

        # Deleting field 'Event.author_email'
        db.delete_column(u'events_event', 'author_email')

        # Deleting field 'Event.comments'
        db.delete_column(u'events_event', 'comments')

        # Deleting field 'Event.content'
        db.delete_column(u'events_event', 'content')

        # Adding field 'Event.start_date'
        db.add_column(u'events_event', 'start_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Event.end_date'
        db.add_column(u'events_event', 'end_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Event.type'
        db.add_column(u'events_event', 'type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Event.description'
        db.add_column(u'events_event', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Event.url'
        db.add_column(u'events_event', 'url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'SportsEvent'
        db.delete_table(u'events_sportsevent')

        # Deleting model 'OsallistujatEvent'
        db.delete_table(u'events_osallistujatevent')

        # Adding field 'Event.date_start'
        db.add_column(u'events_event', 'date_start',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Event.link'
        db.add_column(u'events_event', 'link',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Event.guid'
        db.add_column(u'events_event', 'guid',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, db_index=True),
                      keep_default=False)

        # Adding field 'Event.category'
        db.add_column(u'events_event', 'category',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Event.author'
        db.add_column(u'events_event', 'author',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'Event.author_email'
        db.add_column(u'events_event', 'author_email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True),
                      keep_default=False)

        # Adding field 'Event.comments'
        db.add_column(u'events_event', 'comments',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Event.content'
        db.add_column(u'events_event', 'content',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'Event.start_date'
        db.delete_column(u'events_event', 'start_date')

        # Deleting field 'Event.end_date'
        db.delete_column(u'events_event', 'end_date')

        # Deleting field 'Event.type'
        db.delete_column(u'events_event', 'type')

        # Deleting field 'Event.description'
        db.delete_column(u'events_event', 'description')

        # Deleting field 'Event.url'
        db.delete_column(u'events_event', 'url')


    models = {
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
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
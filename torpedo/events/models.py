from django.db import models
from django.utils.translation import ugettext_lazy as _ 
from django.contrib import admin


class Event(models.Model):
    start_date = models.DateTimeField(_('date'), null=True, blank=True)
    end_date = models.DateTimeField(_('end date'), null=True, blank=True)
    title = models.CharField(_('title'), max_length=255)
    type = models.CharField(_('type'), blank=True, max_length=255)
    description = models.TextField(_('description'), blank=True)
    link = models.URLField(_('link'), null=True, blank=True)

    @property
    def duration(self):
        return self.end_date - self.start_date;

class SportsEvent(models.Model):
    distance = models.CommaSeparatedIntegerField('distance', max_length=255, null=True, blank=True)


class OsallistujatEvent(Event):
    guid = models.CharField(_('guid'), max_length=200, db_index=True)
    author = models.CharField(_('author'), max_length=50, blank=True)
    author_email = models.EmailField(_('author email'), blank=True)
    comments = models.TextField(_('comments'), blank=True)

    def __unicode__(self):
        return u'%s' % (self.title)

    def get_absolute_url(self):
        return self.link

class OsallistujatEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'author', 'start_date')
    search_fields = ['link', 'title']
    date_hierarchy = 'start_date'

admin.site.register(Event)
admin.site.register(SportsEvent)
admin.site.register(OsallistujatEvent, OsallistujatEventAdmin)

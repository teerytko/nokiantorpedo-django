from django.db import models
from django.utils.translation import ugettext_lazy as _ 
from django.contrib import admin

# Create your models here.

class Event(models.Model):
    title = models.CharField(_('title'), max_length=255)
    link = models.URLField(_('link'), )
    content = models.TextField(_('content'), blank=True)
    date_start = models.DateTimeField(_('date start'), null=True, blank=True)
    guid = models.CharField(_('guid'), max_length=200, db_index=True)
    author = models.CharField(_('author'), max_length=50, blank=True)
    author_email = models.EmailField(_('author email'), blank=True)
    comments = models.URLField(_('comments'), blank=True)

    def __unicode__(self):
        return u'%s' % (self.title)

    def get_absolute_url(self):
        return self.link

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'author', 'date_start')
    search_fields = ['link', 'title']
    date_hierarchy = 'date_start'

admin.site.register(Event, EventAdmin)
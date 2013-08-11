from django.conf.urls import patterns, include, url
from sitemap import SitemapForum, SitemapTopic
from django.conf import settings
from django.conf.urls.static import static

# from forms import RegistrationFormUtfUsername
#from djangobb_forum import settings as forum_settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

sitemaps = {
    'forum': SitemapForum,
    'topic': SitemapTopic,
}

urlpatterns = patterns('',
    # Examples:

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Apps
    url(r'^', include('torpedo_main.urls')),
    url(r'^statistics', include('statistics.urls')),

    # Sitemap
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # Apps
    (r'^forum/', include('djangobb_forum.urls', namespace='djangobb')),
    #(r'^messages/', include('django_messages.urls')),
    (r'^feeds/', include('feedjack.urls')),
    (r'^events/', include('events.urls')),
) 

if settings.SERVE_MEDIA:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

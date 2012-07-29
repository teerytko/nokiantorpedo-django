from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Apps
    url(r'^', include('torpedo_main.urls')),
    url(r'^statistics', include('statistics.urls')),
    (r'^forum/', include('djangobb_forum.urls', namespace='djangobb')),
)

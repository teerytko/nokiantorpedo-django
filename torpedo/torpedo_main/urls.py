from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'torpedo_main.views.home', name='home'),
    url(r'^calendar$', 'torpedo_main.views.calendar', name='calendar'),
    url(r'^association$', 'torpedo_main.views.association', name='association'),
    url(r'^account/', include('django_authopenid.urls')),
    url(r'^forum/account/', include('django_authopenid.urls')),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout', 
        {'next_page': '/'}),
)

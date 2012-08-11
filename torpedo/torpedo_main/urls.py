from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'torpedo_main.views.home', name='home'),
    url(r'^calendar$', 'torpedo_main.views.calendar', name='calendar'),
    url(r'^association$', 'torpedo_main.views.association', name='association'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    
)

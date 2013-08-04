from django.conf.urls import patterns, url, include
from torpedo_main.feeds import LatestTopicPosts

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'torpedo_main.views.home', name='home'),
    url(r'^floorball$', 'torpedo_main.views.floorball', name='floorball'),
    url(r'^endurance$', 'torpedo_main.views.endurance', name='endurance'),
    url(r'^calendar$', 'torpedo_main.views.calendar', name='calendar'),
    url(r'^association$', 'torpedo_main.views.association', name='association'),
    url(r'^profile$', 'torpedo_main.views.profile', name='profile'),
    url(r'^account/signin/$', 'torpedo_main.views.signin', name='user_signin'),
    url(r'^account/', include('django_authopenid.urls')),
    url(r'^forum/account/', include('django_authopenid.urls')),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout', 
        {'next_page': '/'}),
    url(r'^forum/feeds/topicposts/$', LatestTopicPosts(),
        name='forum_topicposts_feed'),
)

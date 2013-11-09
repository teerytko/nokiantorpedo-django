from django.conf.urls import patterns, url, include
from torpedo_main.feeds import LatestTopicPosts
from torpedo_main.views import TorpedoRegistrationView
from django.views.generic import RedirectView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'torpedo_main.views.home', name='home'),
    url(r'^floorball$', 'torpedo_main.views.floorball', name='floorball'),
    url(r'^endurance$', 'torpedo_main.views.endurance', name='endurance'),
    url(r'^calendar$', 'torpedo_main.views.calendar', name='calendar'),
    url(r'^association$', 'torpedo_main.views.association', name='association'),
    url(r'^manage$', 'torpedo_main.views.manage', name='manage'),
    url(r'^profile_edit$', 'torpedo_main.views.profile_edit', name='profile_edit'),
    url(r'^profile$', 'torpedo_main.views.profile', name='profile'),
    url(r'^profile/(?P<username>.*)$', 'torpedo_main.views.profile', name='profile'),
    url(r'^profiledlg/(?P<username>.*)$', 'torpedo_main.views.profile_edit', 
        {'dialog': True}),
    url(r'^memberdlg/(?P<username>.*)$', 'torpedo_main.views.member_edit', 
        {'dialog': True}),
    url(r'^profileimg/(?P<username>.*)$', 'torpedo_main.views.profile_img', 
        {'dialog': True}),
    url(r'^account/signin/$', 'torpedo_main.views.signin', name='user_signin'),
    url(r'^account/signup/$', 
        TorpedoRegistrationView.as_view(),
        name='user_signup'),
    url(r'^forum/account/signin/$', RedirectView.as_view(url='/account/signin/')),
    url(r'^forum/account/signup/$', RedirectView.as_view(url='/account/signup/')),
    url(r'^account/', include('django_authopenid.urls')),
    url(r'^forum/account/', include('django_authopenid.urls')),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout', 
        {'next_page': '/'}),
    url(r'^forum/feeds/topicposts/$', LatestTopicPosts(),
        name='forum_topicposts_feed'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^channel/$', 'torpedo_main.views.channel'),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^flattest/$', 'flatpage', {'url': '/test/'}, name='test'),
    url(r'^license/$', 'flatpage', {'url': '/license/'}, name='license'),
    (r'^pages/', include('django.contrib.flatpages.urls')),
)
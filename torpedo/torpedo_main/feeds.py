'''
Created on 6.9.2012

@author: teerytko
'''

from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from djangobb_forum.feeds import ForumFeed, Post, Topic, Forum, Category

class LatestTopicPosts(ForumFeed):
    title = _('Latest posts on topic on forum')
    description = _('Latest post on topic on forum')
    title_template = 'djangobb_forum/feeds/topics_title.html'
    description_template = 'djangobb_forum/feeds/topics_description.html'

    def get_object(self, request):
        user_groups = request.user.groups.all()
        if request.user.is_anonymous():
            user_groups = []
        allow_forums = Forum.objects.filter(
                Q(category__groups__in=user_groups) | \
                Q(category__groups__isnull=True))
        return allow_forums

    def items(self, allow_forums):
        posts = Post.objects.filter(topic__forum__in=allow_forums).order_by('-created')[:15]
        # filter out posts that have the same topic
        seen_topics = []
        sposts = []
        for post in posts:
            if post.topic not in seen_topics:
                sposts.append(post)
                seen_topics.append(post.topic)
        return sposts

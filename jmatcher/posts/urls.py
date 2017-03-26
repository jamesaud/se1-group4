# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.home,
        name='home'
    ),
    url(regex=r'^create/$', view=views.post_status, name="post_status"),
    url(regex=r'^see/$', view=views.get_all_posts, name="get_all_posts"),
    url(regex=r'^see/(?P<post_id>[\d]+)/$', view=views.get_post, name="get_post"),
    url(regex=r'^likePost/$', view=views.like_post, name="like_post"),
    url(regex=r'^sharePost/$', view=views.share_post, name="share_post")
]

#Its better to have the same view name and the url name
#The form is submitted to the url and it is triggering a view
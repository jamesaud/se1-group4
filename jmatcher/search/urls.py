# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.search,
        name='search'
    ),
    url(r'^searchUser/$',
        view=views.searchUser,
        name='searchUser'),
]

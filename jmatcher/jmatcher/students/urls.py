# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.index,
        name='index'
    ),

    url(
        regex=r'^update/$',
        view=views.update,
        name='update'
    ),
    url(
        regex=r'^account-signup/$',
        view=views.account_signup,
        name='account_signup'
    ),
    url(
        regex=r'^signup/$',
        view=views.SignUp.as_view(),
        name='signup'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.home,
        name='home'
    ),
    url(
        regex=r'^~list/$',
        view=views.students,
        name='list'
    ),


]

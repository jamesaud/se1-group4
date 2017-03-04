# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.jobTest,
        name='job'
    ),
    url(r'^postJob/$',
        view=views.postJob,
        name='postJob'),

    url(r'^jobList/$',
        view=views.listJob,
        name='jobList'),

    url(r'^employerPost/$',
        view = views.employerPost,
        name = 'employerPost'),

    url(r'^postSuccess/$',
            view = views.postSuccess,
            name = 'postSuccess'),

    url(r'^job_detail/(?P<job_id>[\d]+)/$',
            view = views.job_detail,
            name = 'job_detail'),
]



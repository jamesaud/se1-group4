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

    url(r'^jobDelete/(?P<job_id>[\d]+)/delete/$',
            view = views.jobDelete,
            name = 'jobDelete'),

    url(r'^jobEdit/(?P<job_id>[\d]+)/edit/$',
            view = views.jobEdit,
            name = 'jobEdit'),

    url(r'^viewApplications/(?P<job_id>[\d]+)/$',
        view = views.viewApplications,
        name = 'viewApplications'),

    url(r'^jobApply/$',
        view=views.jobApply,
        name='jobApply'),

    url(r'^getSkills/$',
        view=views.getSkills,
        name='getSkills'),

]



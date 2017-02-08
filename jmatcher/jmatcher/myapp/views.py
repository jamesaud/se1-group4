# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.shortcuts import render
from .models import Job

# View must return HtttpResponse

def index(request):
    return render(request, template_name='myapp/index.html')


def home(request, job_id):
    variables = {'name': 'awesome'}
    if request.method == 'GET':
       job = Job.objects.get(pk=job_id)
       print(job)
       variables['job'] = job

    return render(request, template_name='myapp/home.html', context=variables)
   # return HttpResponse("I'm home")


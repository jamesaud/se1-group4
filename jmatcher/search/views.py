from django.http import HttpResponse
from django.shortcuts import redirect, render

from jmatcher.job.models import Job
from .utils import get_query
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, render_to_response

from jmatcher.users.models import User
from jmatcher.job.models import Location

def jobPaginate(request, list, num):
    paginator = Paginator(list, num)
    page = request.GET.get('page', 1)

    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list

def searchUser(request):
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query_student = get_query(query_string, ['short_description', ])
        found_student_entries = User.objects.filter(entry_query_student)
    context = {}
    context['query_user'] = query_string
    context['found_student_entries'] = found_student_entries
    return render(request, template_name='search/search_user.html', context=context)

def search(request):

    location, employment_type = request.GET.get('location'), request.GET.get('employment_type')
    location = Location.objects.get(pk=location)
    dict = {'location': location, 'employment_type': employment_type}

    entry_query_job = None
    query_string = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query_job = get_query(query_string, ['post_name', 'description', ])

    
    for key, value in list(dict.items()):
        if value is None:
            del dict[key]

    if entry_query_job:
        found_job_entries = Job.objects.filter(entry_query_job, location=location, employment_type=employment_type)
    else:
        found_job_entries = Job.objects.filter(location=location, employment_type=employment_type)
    
    found_job_entries = jobPaginate(request, found_job_entries.all(), 3)
    context = {}
    context['dict'] = dict
    context['query_string'] = query_string
    context['found_job_entries'] = found_job_entries

    return render(request, template_name = 'search/search_results.html', context = context)
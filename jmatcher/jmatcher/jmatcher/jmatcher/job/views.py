from django.shortcuts import render, redirect, render_to_response

# Create your views here.

from django.http import HttpResponse
from django.contrib import messages
from .utils import get_query
from .jobForm import jobForm
from django.template import RequestContext
from jmatcher.employers.models import Employer

from .models import Job

def jobTest(request):
    return render(request, template_name= 'job/jobTest.html')


def listJob(request):
    jobs = Job.objects.all()
    return render(request, 'job/jobList.html', context={'jobs':jobs})

def postJob(request):
    form = jobForm()
    if request.method == 'GET':
        context = {}
        context['employer'] = form

        return render(request, template_name = 'job/postJob.html', context=context)

    elif request.method =='POST':
        # Save the form
        # Redirect to the success url

            form = jobForm(request.POST)

            if form.is_valid():
                newJob = Job(post_name = form.cleaned_data['post_name'],
                             employment_type = form.cleaned_data['employment_type'],
                             industry=form.cleaned_data['industry'],
                             location=form.cleaned_data['location'],
                             experience=form.cleaned_data['experience'],
                             description = form.cleaned_data['description'],
                             user = request.user)


                newJob.save()

                for skill in form.cleaned_data['skills']:
                    newJob.skills.add(skill)
                newJob.save()

                messages.add_message(request, messages.SUCCESS, 'Successfully Added Job.')
                return redirect('job:job_detail', job_id=newJob.id)

            else:
                context = {}
                context['employer'] = form
                return render(request, template_name='job/postJob.html', context=context)

def employerPost(request):
    user = request.user  # User Object
    # company_name = Employer.objects.get(pk = user.pk)
    context = {}
    jobs = user.job_set.all()
    context['jobs'] = jobs
    return render(request, template_name = 'job/employerPost.html', context = {'jobs':jobs, 'user': user})

def postSuccess(request):
    return render(request, template_name='job/jobTest.html')

def job_detail(request, job_id):
    if request.method == 'GET':
        context = {}
        job_show_detail = Job.objects.get(pk = job_id)
        context['job_show_detail'] = job_show_detail
        return render(request, template_name= 'job/jobDetail.html', context = context)
    else:
        return render(request, template_name='job/employerPost.html')

def jobDelete(request, job_id):
        job = Job.objects.get(pk = job_id)
        job.delete()
        return HttpResponse("job has been deleted")

def jobEdit(request, job_id):
    job = Job.objects.get(pk=job_id)
    form = jobForm(request.POST or None, instance = job)
    if (request.method == 'POST') and form.is_valid():
        for key, value in form.cleaned_data.items():
            setattr(job, key, value)
        job.save()
        return redirect('job:job_detail', job_id=job_id)
    return render(request, template_name = 'job/postJob.html', context = {'employer': form})

def jobApply(request, job_id):
    return HttpResponse("You have successfully appllied the job");

def jobSearch(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['post_name', 'description', ])

        found_entries = Job.objects.filter(entry_query)
        context = {}
        context['query_string'] = query_string
        context['found_entries'] = found_entries
    return render(request, template_name = 'job/search_results.html', context = context)





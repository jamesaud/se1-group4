from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.contrib import messages

from .jobForm import jobForm

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
    context = {}
    jobs = user.job_set.all()
    context['jobs'] = jobs
    return render(request, template_name = 'job/employerPost.html', context = context)

def postSuccess(request):
    return render(request, template_name='job/jobTest.html')

def job_detail(request, job_id):
    if request.method == 'GET':
        context = {}
        job_show_detail = Job.objects.get(pk = job_id);
        context['job_show_detail'] = job_show_detail
        return render(request, template_name= 'job/jobDetail.html', context = context)
    else:
        return render(request, template_name='job/employerPost.html')

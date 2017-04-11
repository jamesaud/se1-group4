from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.contrib import messages

from .jobForm import jobForm

from .models import Job, JobApplication, Skill, Location


def jobTest(request):
    return render(request, template_name='job/jobTest.html')


def listJob(request):
    user = request.user
    student = user.student
    applied_jobs = student.applications.all()
    all_jobs = Job.objects.all()

    for job in all_jobs:
        total_req_skills = job.skills.all().count()
        match_skills = 0
        for skill in user.student.skills.all():
            if skill in job.skills.all():
                match_skills += 1
        if job in applied_jobs:
            job.applied = True
        else:
            job.applied = False
        job.match_percent = (match_skills / (total_req_skills + 1)) * 100

    return render(request, 'job/jobList.html', context={'jobs': all_jobs})


def postJob(request):
    form = jobForm()
    if request.method == 'GET':
        context = {}
        context['employer'] = form

        return render(request, template_name='job/postJob.html', context=context)

    elif request.method == 'POST':
        # Save the form
        # Redirect to the success url

        form = jobForm(request.POST)

        if form.is_valid():
            newJob = Job(post_name=form.cleaned_data['post_name'],
                         employment_type=form.cleaned_data['employment_type'],
                         industry=form.cleaned_data['industry'],
                         experience=form.cleaned_data['experience'],
                         description=form.cleaned_data['description'],
                         user=request.user)

            city, state, country = form.cleaned_data['location'].split(",")
            city = city.strip()
            state = state.strip()
            country = country.strip()

            try:
                location_object = Location.objects.get(city=city, state=state, country=country)
            except Location.DoesNotExist as e:
                location_object = Location(city=city, state=state, country=country)
                location_object.save()
            finally:
                newJob.location = location_object

            newJob.save()

            for skill in form.cleaned_data['skill'].split(","):
                skill = skill.strip().lower()
                try:
                    skill_object = Skill.objects.get(skill=skill)
                except Skill.DoesNotExist as e:
                    skill_object = Skill(skill=skill)
                    skill_object.save()
                else:
                    newJob.skills.add(skill_object)
            newJob.save()

            messages.add_message(request, messages.SUCCESS, 'Successfully Added Job.')
            return redirect('job:job_detail', job_id=newJob.id)

        else:
            context = {}
            context['employer'] = form
            return render(request, template_name='job/postJob.html', context=context)


def getSkills(request):
    all_skills = Skill.objects.all()
    skills = []
    for skill in all_skills:
        skills.append(skill.skill)
    response = JsonResponse({'skills': skills})
    return response


def employerPost(request):
    user = request.user  # User Object
    context = {}
    jobs = user.job_set.all()
    for job in jobs:
        job.total_applications = job.total_applications()
    context['jobs'] = jobs
    return render(request, template_name='job/employerPost.html', context=context)


def postSuccess(request):
    return render(request, template_name='job/jobTest.html')


def job_detail(request, job_id):
    if request.method == 'GET':
        context = {}
        job_show_detail = Job.objects.get(pk=job_id);
        context['job_show_detail'] = job_show_detail
        return render(request, template_name='job/jobDetail.html', context=context)
    else:
        return render(request, template_name='job/employerPost.html')


def jobDelete(request, job_id):
    job = Job.objects.get(pk=job_id)
    job.delete()
    messages.error(request, 'Deleted Job')
    return redirect('job:jobList')


def jobEdit(request, job_id):
    job = Job.objects.get(pk=job_id)
    form = jobForm(request.POST or None, instance=job)
    if (request.method == 'POST') and form.is_valid():
        for key, value in form.cleaned_data.items():
            setattr(job, key, value)
        job.save()
        return redirect('job:job_detail', job_id=job_id)
    return render(request, template_name='job/postJob.html', context={'employer': form})


def jobSearch(request):
    from jmatcher.search.utils import get_query
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['post_name', 'description', ])

        found_entries = Job.objects.filter(entry_query)
        context = {}
        context['query_string'] = query_string
        context['found_entries'] = found_entries
    return render(request, template_name='job/search_results.html', context=context)


def jobApply(request):
    job_id = request.POST.get("job_id")

    job = Job.objects.get(pk=job_id)
    user = request.user

    job_application = JobApplication(student=user.student, job=job)
    job_application.save()
    response = JsonResponse({'message': "Success"})
    return response


'''
TODO: Write the html page
'''
'''
def viewApplications(request, job_id):
    job = Job.objects.get(pk=job_id)
    applicants = job.applications.all()
    return applicants
'''
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

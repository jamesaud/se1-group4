from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.contrib import messages

from .jobForm import jobForm, jobApplicationForm

from .models import Job, JobApplication, Skill, Location
from jmatcher.users.models import Position
from django.contrib import messages
from datetime import timedelta

def jobTest(request):
    return render(request, template_name='job/jobTest.html')


def listJob(request):
    user = request.user
    student = user.student
    applied_jobs = student.applications.all()
    all_jobs = Job.objects.all() 

    for job in all_jobs:
        job.match_percent = get_job_match_percent(user.student, job)
        
        if job in applied_jobs:
            job.applied = True
        else:
            job.applied = False

    sort = lambda j: j.match_percent
    return render(request, 'job/jobList.html', context={'jobs': sorted(all_jobs, key=sort, reverse=True), 'locations': Location.objects.all(), 'positions': Job.EMPLOYMENT_TYPE})

def get_job_match_percent(student, job):

    min_education = job.education_required
    edu_list = ['Undergraduate', 'Graduate', 'PHD']
    edu_match = 0
    
    if min_education == 'Undergraduate':
        if student.education_set.filter(level__in = edu_list).exists():
            edu_match = job.skills_weightage
    elif min_education == 'Graduate':
        edu_list.remove('Graduate')
        if student.education_set.filter(level__in = edu_list).exists():
            edu_match = job.skills_weightage
    elif min_education == 'PHD':
        edu_list.remove('Undergraduate')
        edu_list.remove('Graduate')
        if student.education_set.filter(level__in = edu_list).exists():
            edu_match = job.skills_weightage
    
    min_work_exp = job.experience*365
    student_work_exp = timedelta(0)
    work_match = 0

    for exp in student.workexperience_set.all():
        student_work_exp += exp.end_date-exp.start_date

    if student_work_exp.days > min_work_exp:
        work_match = job.experience_weightage


    total_req_skills = job.skills.all().count()
    match_skills = 0
    for skill in student.skills.all():
        if skill in job.skills.all():
            match_skills += 1
    skill_match_percent = (match_skills / (total_req_skills + 1)) * 100
    
    match_percent = edu_match + work_match + ((job.skills_weightage/100)*skill_match_percent)
    
    return match_percent

'''
TODO: Write the html page
'''

def viewApplications(request, job_id):
    job = Job.objects.get(pk=job_id)
    applications = JobApplication.objects.filter(job=job)
    for application in applications:
        application.match_percent = get_job_match_percent(application.student, job)
    return render(request, 'job/viewApplications.html', context={'applications': applications})

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
                         user=request.user,
                         education_weightage=form.cleaned_data['education_weightage'],
                         experience_weightage=form.cleaned_data['experience_weightage'],
                         skills_weightage=form.cleaned_data['skills_weightage'],
                         education_required=form.cleaned_data['education_required'])

            city, state, country = form.cleaned_data['location'].split(",")
            city = city.strip()
            state = state.strip()
            country = country.strip()

            try:
                location_object = Location.objects.get(city=city, state=state, country=country)
            except Location.DoesNotExist as e:
                location_object = Location(city=city, state=state, country=country)
                location_object.save()

            newJob.location = location_object
            newJob.save()

            for skill in form.cleaned_data['skill'].split(","):
                skill = skill.strip().lower()
                try:
                    skill_object = Skill.objects.get(skill=skill)
                except Skill.DoesNotExist as e:
                    skill_object = Skill(skill=skill)
                    skill_object.save()
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
        if request.user.is_student():
            student = request.user.student
            applied_jobs = student.applications.all()
            job = Job.objects.get(pk=job_id);
            if job in applied_jobs:
                job_applied = True
            else:
                job_applied = False
            context['job_applied'] = job_applied
        context['job_application_form'] = jobApplicationForm()
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

def jobApply(request, job_id):
    job = Job.objects.get(pk=job_id)
    user = request.user

    appl_form = jobApplicationForm(request.POST or None, request.FILES or None)
    if (request.method == 'POST') and appl_form.is_valid():
        job_application = JobApplication(student=user.student, job=job, attachment=appl_form.cleaned_data['attachment'])
        job_application.save()
        messages.success(request, 'You have successfully applied to this Job')
        return redirect('job:job_detail', job_id=job_id) 

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
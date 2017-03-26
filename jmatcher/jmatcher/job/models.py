from time import timezone


from django.db import models
from django import forms

# Create your models here.
from jmatcher.users.models import User, Skill


class Job(models.Model):

    INDUSTRY_TYPE = (
        ('Tech', "Technology Company"),
        ('Busi', "Business"),
        ('Medi', "Medicine"),
    )

    LOCATION = (
        ('CA', 'California'),
        ('WA', 'Washington'),
    )

    EMPLOYMENT_TYPE = (
        ('INTERN', 'Intern'),
        ('FULL_TIME', "Full Time"),
    )

    post_name = models.CharField(max_length=200, null=True)
    employment_type = models.CharField(max_length = 200, null = True, choices = EMPLOYMENT_TYPE)
    industry =  models.CharField(max_length = 200, null = True, choices = INDUSTRY_TYPE)
    location = models.CharField(max_length=200, null= True, choices=LOCATION)
    experience = models.CharField(max_length = 200, null=True)
    description = models.TextField(null=True)
    user = models.ForeignKey(User)
    skills = models.ManyToManyField(Skill, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.employer


class JobApply(models.Model):
    job_id = models.ForeignKey(Job)
    user_id = models.ForeignKey(User)

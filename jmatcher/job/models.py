from time import timezone
from django.db import models
from django import forms
from jmatcher.users.models import User, Skill
from jmatcher.students.models import Student

'''
TODO:
    New Models for IndustryType, Location and Employement
'''
class Location(models.Model):
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

class Job(models.Model):

    INDUSTRY_TYPE = (
        ('Tech', "Technology Company"),
        ('Busi', "Business"),
        ('Medi', "Medicine"),
    )
    EMPLOYMENT_TYPE = (
        ('INTERN', 'Intern'),
        ('FULL_TIME', "Full Time"),
    )

    post_name = models.CharField(max_length=200, null=True)
    employment_type = models.CharField(max_length = 200, null = True, choices = EMPLOYMENT_TYPE);
    industry =  models.CharField(max_length = 200, null = True, choices = INDUSTRY_TYPE)
    location = models.ForeignKey(Location, related_name='location', null=True)
    experience = models.IntegerField()
    description = models.TextField(null=True)
    user = models.ForeignKey(User)
    skills = models.ManyToManyField(Skill, null=True, related_name="reqskills")
    applications = models.ManyToManyField(Student, through='JobApplication',related_name="applications")
    education_weightage = models.IntegerField(default=34)
    experience_weightage = models.IntegerField(default=33)
    skills_weightage = models.IntegerField(default=33)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.employer

    def total_applications(self):
        return self.applications.count()

class JobApplication(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    attachment = models.FileField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
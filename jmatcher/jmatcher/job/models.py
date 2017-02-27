from time import timezone


from django.db import models
from django import forms

# Create your models here.
from jmatcher.company.models import Company
from jmatcher.users.models import User


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
        ('FULL TIME', "FULL TIME"),
    )

    post_name = models.CharField(max_length=200, null=True)
    employment_type = models.CharField(max_length = 200, null = True, choices = EMPLOYMENT_TYPE);
    industry =  models.CharField(max_length = 200, null = True, choices = INDUSTRY_TYPE)
    location = models.CharField(max_length=200, null= True, choices=LOCATION)
    experience = models.CharField(max_length = 200, null=True);
    description = models.CharField(max_length=2000, null=True)
    user = models.ForeignKey(User);
    created_at = models.DateTimeField(auto_now_add=True);
    updated_at = models.DateTimeField(auto_now_add=True);

    def _str_(self):
        return self.employer




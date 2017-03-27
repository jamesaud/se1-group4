# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    #location = models.OneToOneField(Location)
    connections = models.ManyToManyField("self", null=True)

    image = models.ImageField(blank=True, null=True)
    background = models.ImageField(blank=True, null=True)
    short_description = models.CharField(blank=True, null=True, max_length=90)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        if self.is_employer():
            return reverse('employers:home', kwargs={'username': self.username})
        else:
            return reverse('students:home', kwargs={'username': self.username})


    def is_employer(self):
        return True if hasattr(self, 'employer') else False

    def is_student(self):
        return True if hasattr(self, 'student') else False

    def get_image_url(self):
        try:
            return self.image.url
        except ValueError:
            return 'https://thebenclark.files.wordpress.com/2014/03/facebook-default-no-profile-pic.jpg'

    def get_background_url(self):
        try:
            return self.background.url
        except ValueError:
            return 'http://www.planwallpaper.com/static/images/10e39f13ddfb80570f3e44fb2016cb76.jpg'

    def get_name(self):
        if self.is_employer():
            return self.employer.company_name
        else:
            return self.get_full_name()




SKILL_CHOICES = (
    ('Django', 'Django'),
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('Ruby', 'Ruby'),
)

class Skill(models.Model):
    skill = models.CharField(max_length=255, choices=SKILL_CHOICES)

    def __str__(self):
        return self.skill




class PositionChoices:
    INTERN = 'Intern'
    FULL_TIME = 'Full Time'

    Choices = (
        (INTERN, 'Intern'),
        (FULL_TIME, 'Full Time')
    )

class Position(models.Model):
    position = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.position

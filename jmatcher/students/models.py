from django.db import models
from jmatcher.users.models import User, Position, PositionChoices
from address.models import AddressField
from jmatcher.users.models import Skill


class Student(models.Model):
    user = models.OneToOneField(User)
    skills = models.ManyToManyField(Skill, related_name="skills")
    position = models.OneToOneField(Position, null=True, on_delete=models.SET_NULL)

class PositionChoices:
    INTERN = 'Intern'
    FULL_TIME = 'Full Time'

    Choices = (
        (INTERN, 'Intern'),
        (FULL_TIME, 'Full Time')
    )

class LevelChoices:
    UNDERGRAD = 'Undergraduate'
    GRAD = 'Graduate'
    PHD = 'PHD'

    Choices = (
        (UNDERGRAD, 'Intern'),
        (GRAD, 'Full Time'),
        (PHD, 'PHD')
    )


class WorkExperience(models.Model):
    student = models.ForeignKey(Student)
    title = models.CharField(max_length=60)
    position = models.CharField(choices=PositionChoices.Choices, max_length=100) # Choise of 'intern' or 'full time'
    start_date = models.DateField()
    end_date = models.DateField()   # Enforce that end_date comes after start_date.
    description = models.CharField(max_length=255)


class Education(models.Model):
    student = models.ForeignKey(Student)
    level = models.CharField(choices=LevelChoices.Choices, max_length=80) # Choices
    institution_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()   # Enforce that end_year comes after start_year.


class Project(models.Model):
    student = models.ForeignKey(Student)
    title = models.CharField(max_length=80) # Choices
    description = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()   # Enforce that end_year comes after start_year.

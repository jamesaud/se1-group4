from django.db import models
from jmatcher.users.models import User
from address.models import AddressField
from jmatcher.users.models import Skill


class Student(models.Model):
    user = models.OneToOneField(User)
    skills = models.ManyToManyField(Skill)



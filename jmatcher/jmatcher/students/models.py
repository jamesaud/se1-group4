from django.db import models
from jmatcher.users.models import User, Position, PositionChoices
from address.models import AddressField
from jmatcher.users.models import Skill


class Student(models.Model):
    user = models.OneToOneField(User)
    skills = models.ManyToManyField(Skill)
    position = models.OneToOneField(Position, null=True, on_delete=models.SET_NULL)



from django.db import models

from jmatcher.users.models import User


class Company(User):
    company_name = models.CharField(max_length=200);
    # location = models.OneToOneField;
    website = models.URLField();
    description = models.CharField(max_length= 400);

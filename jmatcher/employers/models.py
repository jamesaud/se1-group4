from django.db import models
from jmatcher.users.models import User
from address.models import AddressField
SIZE_CHOICES = (
    ('1-50', '1-50'),
    ('51-100', '51-100'),
    ('101-1000', '101-1000'),
)



class Employer(models.Model):

    user = models.OneToOneField(User)
    company_name = models.CharField(blank=False, max_length=255, null=True)
    location = AddressField(null=True)
    website = models.URLField(blank=False, null=True)
    size = models.CharField(choices=SIZE_CHOICES, blank=False, null=True, max_length=255)
    description = models.CharField(blank=False, null=True, max_length=2000)

    def __str__(self):
        return self.company_name


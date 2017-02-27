from django.contrib.admin import AdminSite
from django.contrib import admin

from jmatcher.company.models import Company

admin.site.register(Company)

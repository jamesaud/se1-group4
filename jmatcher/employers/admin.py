from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Employer


admin.site.register(Employer)
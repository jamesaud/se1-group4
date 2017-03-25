from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Position, Student


admin.site.register(Student)
admin.site.register(Position)

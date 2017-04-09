# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 06:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_education_workexperience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='end_year',
        ),
        migrations.RemoveField(
            model_name='education',
            name='start_year',
        ),
        migrations.AddField(
            model_name='education',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

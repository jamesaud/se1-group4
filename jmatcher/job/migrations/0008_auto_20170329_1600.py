# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 16:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_jobapply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapply',
            name='job_id',
        ),
        migrations.RemoveField(
            model_name='jobapply',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='JobApply',
        ),
    ]
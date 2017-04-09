# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_position'),
        ('job', '0009_auto_20170329_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapplication',
            old_name='job_id',
            new_name='job',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='user_id',
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='applications',
            field=models.ManyToManyField(related_name='applications', through='job.JobApplication', to='students.Student'),
        ),
    ]

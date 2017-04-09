# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_auto_20170409_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='location',
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='job.Location'),
        ),
    ]

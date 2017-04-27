# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_auto_20170409_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='job.Location'),
            preserve_default=False,
        ),
    ]

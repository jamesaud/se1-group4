# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 17:53
from __future__ import unicode_literals

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('job', '0020_auto_20170422_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='experience'
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=1),
            preserve_default=False
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0023_auto_20170423_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='education_required',
            field=models.CharField(choices=[('Undergraduate', 'Undergraduate'), ('Graduate', 'Graduate'), ('PHD', 'PHD')], default=1, max_length=80),
            preserve_default=False,
        ),
    ]

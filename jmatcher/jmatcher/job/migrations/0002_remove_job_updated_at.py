# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 16:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='updated_at',
        ),
    ]
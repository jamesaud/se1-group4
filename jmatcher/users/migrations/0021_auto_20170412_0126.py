# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20170410_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill',
            field=models.CharField(max_length=255),
        ),
    ]

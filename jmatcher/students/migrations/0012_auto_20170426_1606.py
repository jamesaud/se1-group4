# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_auto_20170422_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='level',
            field=models.CharField(choices=[('Undergraduate', 'Undergraduate'), ('Graduate', 'Graduate'), ('PHD', 'PHD')], max_length=80),
        ),
    ]

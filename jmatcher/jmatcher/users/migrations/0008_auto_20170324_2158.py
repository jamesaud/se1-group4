# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='id',
        ),
        migrations.AlterField(
            model_name='position',
            name='position',
            field=models.CharField(choices=[('Intern', 'Intern'), ('Full Time', 'Full Time')], max_length=255, primary_key=True, serialize=False),
        ),
    ]

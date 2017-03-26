# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 21:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_position'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='position',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Position'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20170326_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
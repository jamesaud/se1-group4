# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 19:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20170326_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='shares',
            field=models.ManyToManyField(related_name='shares', to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0018_auto_20170422_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='attachment',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
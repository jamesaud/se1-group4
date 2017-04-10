# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 16:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0008_auto_20170329_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Job')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='applications',
            field=models.ManyToManyField(related_name='applications', through='job.JobApplication', to=settings.AUTH_USER_MODEL),
        ),
    ]

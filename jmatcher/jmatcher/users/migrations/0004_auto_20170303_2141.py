# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 21:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_student_student_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(choices=[('Django', 'Django'), ('Python', 'Python'), ('Java', 'Java'), ('Ruby', 'Ruby')], max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='connections',
            field=models.ManyToManyField(related_name='_user_connections_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
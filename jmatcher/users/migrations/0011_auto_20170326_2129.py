# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20170326_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='background',
            field=models.ImageField(blank=True, default='http://www.planwallpaper.com/static/images/10e39f13ddfb80570f3e44fb2016cb76.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='https://thebenclark.files.wordpress.com/2014/03/facebook-default-no-profile-pic.jpg', null=True, upload_to=''),
        ),
    ]

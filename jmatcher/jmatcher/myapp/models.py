# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class Job(models.Model):
    name = models.CharField(max_length=250, null=False)
    description = models.CharField(max_length=5000, null=False)

    def __str__(self):
        return self.name

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from tags.models import Tag


class my_entries(models.Model):

    header = models.CharField(max_length=220)
    body = models.CharField(max_length=520)
    owner = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)
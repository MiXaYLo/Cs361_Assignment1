from __future__ import unicode_literals

from django.db import models

# Create your models here.

#my_entries = [('header', 'body text'), ('header2', 'body text2'),('header3','body text3'),('header4', 'body text4')]



class my_entries(models.Model):

    header = models.CharField(max_length=220)
    body = models.CharField(max_length=520)
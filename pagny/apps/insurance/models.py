# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Insurance(models.Model):
    add1 = models.CharField(max_length=30)
    add2 = models.CharField(max_length=30)
    time = models.CharField(max_length=10)
    value = models.CharField(max_length=10)
    finishes = models.CharField(max_length=10)
    domestichelp = models.CharField(max_length=10)


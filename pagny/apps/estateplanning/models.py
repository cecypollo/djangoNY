# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class estateP(models.Model):
    q1 = models.CharField(max_length=10)
    q2 = models.CharField(max_length=10)
    q3 = models.CharField(max_length=10)
    q4 = models.CharField(max_length=10)
    q5 = models.CharField(max_length=10)



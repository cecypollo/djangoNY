# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class ClientSignIn(models.Model):
    username = models.CharField(max_length=10)
    password= models.CharField(max_length=30)

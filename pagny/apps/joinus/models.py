# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Client(models.Model):
    title = models.CharField(max_length=10)
    firstname = models.CharField(max_length=30)
    surname = models.CharField(max_length=80)
    birth = models.CharField(max_length=10)
    marital = models.CharField(max_length=20)
    children = models.CharField(max_length=10)
    housenum = models.CharField(max_length=10)
    street = models.CharField(max_length=30)
    postalcode = models.CharField(max_length=10)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    pin = models.CharField(max_length=4)
    email = models.CharField(max_length=30)
    telnum = models.CharField(max_length=10)


# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import estateform
from models import estateP

def index(request):
    return render(request, 'signin/signin.html')


def estate_view(request):
    if request.method=='POST':
        form=estateform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('estateplanning:estateplanning')
    else:
        form=estateform()
    return render(request,'estateplanning/estateform.html',{'form':form})
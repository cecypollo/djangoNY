# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import taxform
from models import TaxP

def index(request):
    return render(request, 'signin/signin.html')


def tax_view(request):
    if request.method=='POST':
        form=taxform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('taxplanning:taxplanning')
    else:
        form=taxform()
    return render(request,'taxplanning/taxform.html',{'form':form})
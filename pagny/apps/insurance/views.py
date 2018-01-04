# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import insuranceform
from models import Insurance

def index(request):
    return render(request, 'insurance/insuranceform.html')


def insurance_view(request):
    if request.method=='POST':
        form=insuranceform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('insurance:insurance')
    else:
        form=insuranceform()
    return render(request,'insurance/insuranceform.html',{'form':form})
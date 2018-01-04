# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import signinform
from models import ClientSignIn

def index(request):
    return render(request, 'signin/signin.html')


def sigin_view(request):
    if request.method=='POST':
        form=signinform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('signin:signin')
    else:
        form=signinform()
    return render(request,'signin/signinform.html',{'form':form})
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import joinusform
from models import Client

def index(request):
    return render(request, 'joinus/joinus.html')


def client_view(request):
    if request.method=='POST':
        form=joinusform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('joinus:joinus')
    else:
        form=joinusform()
    return render(request,'joinus/joinusform.html',{'form':form})

def client_list(request):
    client= Client.objects.all()
    context={'clients': client}
    return render(request, 'joinus/joinuslist.html', context)

def client_edit(request, id_client):
    client=Client.objects.get(id=id_client)
    if request.method=="GET":
        form=joinusform(instance=client)
    else:
        form=joinusform(request.POST, instance=client)
        if form.is_valid():
            form.save()
        return redirect('joinus/joinus/joinuslist.html')
    return render(request, 'joinus/joinusform.html', {'form':form})

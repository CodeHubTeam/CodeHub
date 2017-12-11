# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models
from .models import User
from django.shortcuts import get_object_or_404, render
# Create your views here.
def index(request):
    return render(request,'index.html')

def mainPage(request):
    return render(request,'mainPage.html')

def login(request):
    return render(request,'login.html')

def code(request):
    return render(request,'code.html')

def branch(request):
    return render(request,'branch.html')

def register(request):
    return render(request,'register.html')

def processRegister(request):
    print ("注册中")
    name = request.POST.get('name')
    print (name)
    email = request.POST.get('email')
    print (email)
    password = request.POST.get('password')
    print (password)
    rePassword = request.POST.get('rePassword')
    print (rePassword)
    print (models.User.objects.create(user_name=name,mail=email,password=password))
    return render(request,'projectCatalog.html')

def proceLogin(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    #theuser = User.objects.get(pk=name)
    theuser = get_object_or_404(User, pk=name)
    if theuser.password != password: print ("wrong password")
    return render(request, 'projectCatalog.html')

def processCreate(request):
    return render(request, 'projectCreate.html')
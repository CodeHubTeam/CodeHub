# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# import models
from django.shortcuts import render
from . import models
from .models import User,Project
from django.shortcuts import get_object_or_404, render,render_to_response
import pygit2
import json

# Create your views here.
def create_dir(path):
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print ('项目创建成功')
        return path
        #return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print ('该项目已存在')
        return path
        #return False
def create_usr_dir(dir_name):
    #git.create_dir(dir_name)
    print('Building a bare git repo for usr,', dir_name)
    repo = pygit2.init_repository(dir_name, bare=True)
    print("Bare repo for usr is:", repo)
def index(request):
    return render(request,'index.html')

def mainPage(request):
    return render(request,'mainPage.html')

def login(request):
    return render(request,'login.html')

def code(request):
    return render(request,'code.html')

def branch(request):
    data = models.show_branches_refs('/home/picher/workSpace/rep_for_bob/')
    return render(request, 'branch.html', {
            'List': json.dumps(data),
        })

def create_branch(request):
    if request.method == "POST":
        name = request.POST.get('proBranch')
        print(name)
        models.new_switch_branch('/home/picher/workSpace/rep_for_bob/', name)
        result = "Create new branch success!"
        print(result)

def switch_branch(request):
    if request.method == "POST":
        name = request.POST.get('switch_branch')
        models.switch_branch('/home/picher/workSpace/rep_for_bob/', name)
        result = "switch branch success!"
        print(result)



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

# def processCreate(request):
#     return render(request, 'projectCreate.html')
# class ProjectForm(forms.Form):
#     project_name = forms.CharFeild()
#     description = forms.CharFeild()
#     repo_path = froms.CharFeild()
#     lead_

def process_project_create(request):
    if request.method == 'POST':#dir_name是绝对路径例如/home/bob/apps/CodeHub/XYJ
        # user = request.user#还要把user写入session
        # user_path = request.user.user_path
        project_name = request.POST.get('project_name')
        description = request.POST.get('description')
        # dir_name = create_dir(user_path+'/'+project_name)
        print(project_name,description)
        # create_usr_dir(dir_name)
        # project = Project(project_name = project_name,description = description,repo_path = dir_name,lead_user = user)
        # project.save()
    else:
        return render_to_response('projectCreate.html')
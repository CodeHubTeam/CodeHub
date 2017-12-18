# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from . import models
from django.urls import reverse
from .models import User, project_user, Project
from django.shortcuts import get_object_or_404, render
import pygit2
import json

from . import mygit
#from mygit import *                 #去掉注释就使用了pygit2，没装pygit2请注释此行
import os.path
#codehub_path = '/Users/sxyzc/repo/'   #一般所有用户所在的目录，全局设置，迁移后自己修改
codehub_path = os.path.dirname(__file__)+'/repo/'


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
    repo = pygit2.init_repository(dir_name+'/.git', bare=False)
    print("Bare repo for usr is:", repo)


# Create your views here.
def index(request):
    return render(request,'index.html')

def mainPage(request):
    return render(request,'mainPage.html')

def login(request):
    return render(request,'login.html')

def code_test(request):
    return render(request,'code.html')

#def code(request, project_owner, project_id):
#
"""
def code(request, *args, **kwargs):
    #print args
    print (kwargs['project_name'])
    print (kwargs['project_owner'])
    #mycat_id = kwargs['pk']
    #print(project_ii)
    print ("22222222222")
"""
def code(request):
    #try:
    print 'code'
    p_owner,p_name = request.GET.get('project_owner'),request.GET.get('project_name')
    if p_owner == None:
        p_owner,p_name = request.session['now_project_owner'],request.session['now_project_name']
    print p_owner,p_name
    project = Project.objects.get(project_name=p_name,lead_user=p_owner)
    #project = Project.objects.get(project_id=res)
    request.session['now_project_id'] = project.project_id
    request.session['now_project_name'] = project.project_name
    request.session['now_project_owner'] = project.lead_user.user_name
    request.session['now_project_repo_path'] = codehub_path + '/' +project.lead_user.user_name+ '/'+project.project_name+'/'
    files = os.listdir(codehub_path + project.repo_path)
    print (files)
    print ('***************')
    print (codehub_path + project.repo_path)
    #except Project.DoesNotExist:
    #    raise Http404("Project does not exist")
    return render(request, 'code.html', {'project': project,'files': files})


def branch(request):
    data = mygit.show_branches_refs(request.session['now_project_repo_path'])
    return render(request, 'branch.html', {'data': data})


def create_branch(request):
    if request.method == "POST":
        name = request.POST.get('new_branch')
        mygit.new_branch(request.session['now_project_repo_path'], name)
        status = 0
        result = "Create new branch success!"
        print(result)
        data = mygit.show_branches_refs(request.session['now_project_repo_path'])
        return render(request, 'branch.html', {'data': data})

#def delete_branch(request):

def delete_branch(request):
    #if request.method == "POST":
    name = request.GET.get('branch_name')
    mygit.delete_branch(request.session['now_project_repo_path'], name)
    result = "Delete new branch success!"
    print(result)
    data = mygit.show_branches_refs(request.session['now_project_repo_path'])
    return render(request, 'branch.html', {'data': data})

def merge_branch(request):
    frombranch = request.POST.get('frombranch')
    msg = request.POST.get('message')
    frombranch_exist = mygit.merge(request.session['now_project_repo_path'],frombranch,msg)
    if frombranch_exist:
        data = mygit.show_branches_refs(request.session['now_project_repo_path'])
        return render(request, 'branch.html', {'data': data})
    else:
        data = mygit.show_branches_refs(request.session['now_project_repo_path'])
        return render(request, 'branch.html', {'data': data})

def switch_branch(request):
    tobranch = request.POST.get('tobranch')
    mygit.switch_branch(request.session['now_project_repo_path'], tobranch)
    data = mygit.show_branches_refs(request.session['now_project_repo_path'])
    return render(request, 'branch.html', {'data': data})


def register(request):
    return render(request,'register.html')

def profile(request):
    print ("注册中")
    name = request.session['now_project_owner']
    if name == request.session['user_name']:
        is_user = True
    else : is_user = False
    theuser = get_object_or_404(User, pk=name)
    # print(theuser)
    # print("---------------")
    pro_list = []

    pro_id_list = project_user.objects.filter(user_name=request.session['user_name'])
    for i, j in enumerate(pro_id_list):
        pro_list.append(Project.objects.get(pk=j.project_id))
    print (pro_list)
    print (request.session['user_name'])
    return render(request, 'projectCatalog.html', {'projects': pro_list,'is_user':is_user})

def processRegister(request):
    print ("注册中")
    name = request.POST.get('name')
    print (name)
    email = request.POST.get('email',"noemail")
    print (email)
    password = request.POST.get('password')
    print (password)
    rePassword = request.POST.get('rePassword','norepassword')
    print (rePassword)
    if email != "noemail":
        print (models.User.objects.create(user_name=name,mail=email,password=password))
        pro_list = []
        request.session['user_name'] = name
        pro_id_list = project_user.objects.filter(user_name=request.session['user_name'])
        for i, j in enumerate(pro_id_list):
            pro_list.append(Project.objects.get(pk=j.project_id))
        print (pro_list)
        print (request.session['user_name'])
        is_user = True
        return render(request, 'projectCatalog.html', {'projects': pro_list,'is_user':is_user})
    else:
        theuser = get_object_or_404(User, pk=name)
        # print(theuser)
        # print("---------------")
        pro_list = []
        if theuser.password != password:
            print ("wrong password")
            list = ["密码错误"]
            print json.dumps(list)
            print 123
            return render(request,'login.html',{'List':json.dumps(list)})
        else:
            request.session['user_name'] = name
            pro_id_list = project_user.objects.filter(user_name=request.session['user_name'])
            for i, j in enumerate(pro_id_list):
                pro_list.append(Project.objects.get(pk=j.project_id))
            print (pro_list)
            print (request.session['user_name'])
        is_user = True
        return render(request, 'projectCatalog.html', {'projects': pro_list,'is_user':is_user})

"""
def proceLogin(request):
    print("----------")
    name = request.POST.get('name')
    password = request.POST.get('password')
    #theuser = User.objects.get(pk=name)
    theuser = get_object_or_404(User, pk=name)
    #print(theuser)
    #print("---------------")
    pro_list = []
    if theuser.password != password: print "wrong password"
    else:
        request.session['user_name'] = name
        pro_id_list = project_user.objects.filter(user_name=request.session['user_name'])
        for i, j in enumerate(pro_id_list):
        	pro_list.append(Project.objects.get(pk=j.project_id))
        print pro_list
        print request.session['user_name']
    return render(request, 'projectCatalog.html', {'projects': pro_list})
"""
def processCreate(request):
    return render(request, 'projectCreate.html')


def process_project_create(request):
    if request.method == 'POST':#dir_name是绝对路径例如/home/bob/apps/CodeHub/XYJ
        #user = request.session['user']#还要把user写入session
        #user_path = request.user.user_path
        project_name = request.POST.get('project_name')
        description = request.POST.get('description')
        dir_name = create_dir(codehub_path+'/'+request.session['user_name']+'/'+project_name)
        repo_path = request.session['user_name']+'/'+project_name+'/'
        print(project_name,description)
        create_usr_dir(dir_name)
        #project = Project(project_name = project_name,repo_path = dir_name,lead_user = get_object_or_404(User, pk=request.session['user_name']))
        #project.save()#description = description,
        print 'sdsfsdf'
        tem = models.Project.objects.create(project_name = project_name,repo_path = repo_path,lead_user = get_object_or_404(User, pk=request.session['user_name']))
        print tem
        print tem.project_id
        models.project_user.objects.create(project_id = tem.project_id,user_name = get_object_or_404(User, pk=request.session['user_name']))
        print 'sssssssss'
        request.session['now_project_owner'],request.session['now_project_name'] = request.session['user_name'],project_name
        return HttpResponseRedirect(reverse('hub:code'))
    #else:
    return render(request, 'projectCreate.html')


def member(request):
#def member(request, *args, **kwargs):
    #print args

    print ('member!!!!!!!!!!!!!!!!!!!!')
    pro_id  = request.session['now_project_id']
    print ('member')

    input_member = request.POST.get('i_name', "ffff")
    #pro_id = 1
    print('pro_id', pro_id)
    print ('input_member', input_member)
    if len(input_member) == 0:
        pass
    else:
        ff = models.User.objects.filter(user_name=input_member)
        if len(ff) != 0:
            uu = models.User.objects.get(user_name=input_member)
            pp = models.project_user.objects.filter(user_name=input_member,project_id=pro_id)
            if len(pp) == 0:
                models.project_user.objects.create(project_id=pro_id, user_name=uu)
                print ('ok')
            else:
                print ('已存在')

    all_members = models.project_user.objects.filter(project_id=pro_id)
    print (len(all_members),"#########")
    return render(request, 'member.html', {"members": all_members})
def upload(request):
    if request.method == 'GET':
        return render_to_response('upload.html')
    elif request.method == 'POST':
        obj = request.FILES.get('fafafa')
        f = open(os.path.join('hub','repo',request.session['now_project_owner'],request.session['now_project_name'],obj.name),'wb')
        print f
        print '@@@@@@@@@@@@@@@@'
        for line in obj.chunks():
            f.write(line)
        f.close()
        print '33333333'
        mygit.change_commit(codehub_path+os.path.join(request.session['now_project_owner'],request.session['now_project_name'])+'/',obj.name,'test','admin','admin@gmail.com')
        print '********'
        return render_to_response('upload.html')
# 	pro_id = 1
# 	all_members = models.project_user.objects.filter(project_id=pro_id)
# #return render(request, 'member.html', {"members": all_members})
#         return render(request, 'member.html')

"""
def proMem(request):
    print 'promem!!!!!!!!!!!!!!!!!!!!'
    input_member = request.POST.get('i_name', 1)
    pro_id = request.session['now_project_id']
    print('pro_id', pro_id)
    print ('input_member', input_member)
    if len(input_member) == 0:
        pass
    else:
        ff = models.User.objects.filter(user_name=input_member)
        if len(ff) != 0:
            uu = models.User.objects.get(user_name=input_member)
            pp = models.project_user.objects.filter(user_name=input_member)
            if len(pp) == 0:
                models.project_user.objects.create(project_id=pro_id, user_name=uu)
                print 'ok'
            else:
                print '已存在'
        #findup = models.Project.objects.get(project_id=pro_id)
        # allusers = models.User.objects.all().values_list('user_name')
        # print len(allusers)
        # print allusers
        # if 'user01' in allusers:
        #     print 'zai'
        # else:
        #     print 'buzai'
        #     models.project_user.objects.create(project_id=pro_id, user_name=input_member)

            #findup = models.Project.objects.get(project_id=pro_id)
        #print findup2
        # if findup2 is not null:
        #     pass
        # else:
        #     models.project_user.objects.create(project_id = pro_id, user_name = input_member)

    all_members = models.project_user.objects.filter(project_id=pro_id)
    print "dsfsdfsdkjfhkjsda"
    #return render_to_response('member.html', {"members": all_members})
    return render(request, 'member.html', {"members": all_members})
    pass
"""

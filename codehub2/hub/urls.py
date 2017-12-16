from django.conf.urls import url

from . import views
app_name = 'hub'
urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^mainPage', views.mainPage),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^projectCatalog', views.processRegister, name='processRegister'),
    url(r'^projectCatalog', views.processRegister, name='processLogin'),
    #url(r'^projectCatalog', views.proceLogin, name='processLogin'),
    #url(r'^projectCreate', views.processCreate),
    url(r'^projectCreate', views.process_project_create, name='process_project_create'),
    url(r'^upload', views.upload),
    url(r'^code', views.code),

    url(r'^branch', views.branch),
    url(r'^create_new_branch', views.create_branch, name='newbranch'),
    url(r'^delete', views.delete_branch, name='deletebranch'),
    url(r'^merge', views.merge_branch, name='mergebranch'),
    url(r'^switch', views.switch_branch, name='switchbranch'),

    url(r'^member', views.member,name='proMem'),
    #url(r'^[\S]+/[\S]+/member', views.member,name='proMem'),
    #url(r'^(?P<project_owner>[\S]+)/(?P<project_name>[\S]+)/member', views.member,name='proMem'),
    #url(r'^member', views.proMem,name='proMem'),
    #url(r'^(?P<project_owner>[\S]+)/(?P<project_name>[\S]+)/$', views.code),
    #url(r'^(?P<project_ii>[0-9]+)/$', views.code),
    #url(r'^edit/action/', views.edit_action, name = 'edit_action'),
]
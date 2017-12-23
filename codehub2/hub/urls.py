from django.conf.urls import url

from . import views
app_name = 'hub'
urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^mainPage', views.mainPage),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^profile', views.profile,name='profile'),

    url(r'^projectCreate', views.project_create, name='project_create'),
    url(r'^upload', views.upload,name='upload'),
    url(r'^code_file', views.code_file,name='code_file'),
    url(r'^code_edit', views.code_edit,name='code_edit'),
    url(r'^process_edit', views.process_edit,name='process_edit'),
    url(r'^code_new', views.code_new,name='code_new'),
    url(r'^process_new', views.process_new,name='process_new'),
    url(r'^code', views.code, name='code'),
    url(r'^getZip', views.getZip, name='getZip'),


    url(r'^commit', views.commit, name='commit'),

    url(r'^branch', views.branch,name='branch'),
    url(r'^create_new_branch', views.create_branch, name='newbranch'),
    url(r'^delete', views.delete_branch, name='deletebranch'),
    url(r'^merge', views.merge_branch, name='mergebranch'),
    url(r'^switch', views.switch_branch, name='switchbranch'),
    url(r'^code_switch', views.code_switch_branch, name='code_switchbranch'),

    url(r'^member', views.member,name='proMem'),
    url(r'^member', views.member,name='member'),
    url(r'^delMem', views.delMem, name='delMem'),
    
    url(r'^settings', views.settings,name='settings'),
    url(r'^delProject', views.delProject, name='delProject'),
    #url(r'^[\S]+/[\S]+/member', views.member,name='proMem'),
    #url(r'^(?P<project_owner>[\S]+)/(?P<project_name>[\S]+)/member', views.member,name='proMem'),
    #url(r'^member', views.proMem,name='proMem'),
    #url(r'^(?P<project_owner>[\S]+)/(?P<project_name>[\S]+)/$', views.code),
    #url(r'^(?P<project_ii>[0-9]+)/$', views.code),
    #url(r'^edit/action/', views.edit_action, name = 'edit_action'),
]

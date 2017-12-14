from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^index', views.index),
    url(r'^mainPage', views.mainPage),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^projectCatalogR', views.processRegister, name='processRegister'),
    url(r'^projectCatalogL', views.proceLogin, name='processLogin'),
    url(r'^projectCreate', views.process_project_create, name='process_project_create'),
    url(r'^code', views.code),
    url(r'^branch', views.branch),
    url(r'^create_new_branch', views.create_branch, name='newbranch'),
    url(r'^delete', views.delete_branch, name='deletebranch'),
    url(r'^merge', views.merge_branch, name='mergebranch'),
    url(r'^switch', views.switch_branch, name='switchbranch'),
    #url(r'^edit/action/', views.edit_action, name = 'edit_action'),
]
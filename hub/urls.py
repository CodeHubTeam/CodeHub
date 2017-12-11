from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^index', views.index),
    url(r'^mainPage', views.mainPage),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^projectCatalogR', views.processRegister, name='processRegister'),
    url(r'^projectCatalogL', views.proceLogin, name='processLogin'),
    url(r'^projectCreate', views.processCreate),
    url(r'^code', views.code),
    url(r'^branch', views.branch),
    #url(r'^edit/action/', views.edit_action, name = 'edit_action'),
]
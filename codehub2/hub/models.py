# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
	"""docstring for User"""
	user_name = models.CharField(primary_key=True,max_length=30)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=30)
	def __str__(self):
		return self.user_name
	# def __init__(self, arg):
	# 	super(User, self).__init__()
	# 	self.arg = arg
	# def __str__(self) :
 #        return self.user_id
class  Project(models.Model):
	"""docstring for  Project"""
	# def __init__(self, arg):
	# 	super( Project, self).__init__()
	# 	self.arg = arg
	project_id = models.AutoField(primary_key=True)
	project_name = models.CharField(max_length=100)
	repo_path = models.CharField(max_length=100)
	lead_user = models.ForeignKey(User)
	def __str__(self):
		return self.project_name

class project_user(models.Model):
	"""docstring for Project_user"""
	project_id = models.IntegerField()
	user_name = models.ForeignKey(User)
	#def __str__(self):
	#	return self.project_id
	#def __str__(self):
	#	return self.project_id,self.user_name
	#def __init__(self, arg):
	# 	super(Project_user, self).__init__()
	# 	self.arg = arg
class user_commit(models.Model):
	commit_id = models.IntegerField(primary_key=True)
	user_name = models.ForeignKey(User)
	description = models.CharField(max_length=100)
	branch_name = models.CharField(max_length=100)
	commit_time = models.DateTimeField()
	def __str__(self):
		return self.commit_id

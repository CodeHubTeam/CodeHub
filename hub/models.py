# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import pygit2
from pygit2 import Repository
import time
import os

# Create your models here.
class User(models.Model):
	"""docstring for User"""
	user_name = models.CharField(primary_key=True,max_length=30)
	mail = models.CharField(max_length=100)
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
	project_id = models.IntegerField(primary_key=True)
	project_name = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	repo_path = models.CharField(max_length=100)
	lead_user = models.ForeignKey(User)
	def __str__(self):
		return self.project_id

class project_user(models.Model):
	"""docstring for Project_user"""
	project_id = models.IntegerField(primary_key=True)
	user_name = models.ForeignKey(User)
	def __str__(self):
		return self.project_id
	# def __init__(self, arg):
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


# 以下功能函数负责git端的通信操作
# 目录操作：
# 如果没有特殊的说明,穿进来的凡是文件夹，只需要传入仓库的路径即可
# 用户注册成功后，应立即调用下面的create_usr_dir()函数生成文件夹和对应的git空目录
# 创建文件夹，需要一个绝对路径作为参数
def create_dir(path):
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print '文件夹 ' + path + ' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print '文件夹 ' + path + ' 目录已存在'
        return False
# 创建 git 用户主目录，需要用户的主目录绝对路径
# 例如：
# codehub在：/home/bob/apps/CodeHub
# 用户 jerry 注册了一个新账号:SCUT_JERRY
# 则用户主目录的绝对路径为：/home/bob/apps/CodeHub/SCUT_JERRY
def create_usr_dir(dir_name):
    git.create_dir(dir_name)
    print('Building a bare git repo for usr,', dir_name)
    repo = pygit2.init_repository(dir_name, bare=True)
    print("Bare repo for usr is:", repo)
# 创建 git 用户项目目录，需要完整的绝对路径作为参数，即‘用户主目录+项目名称’
def create_working_dir(dir_name):
    git.create_dir(dir_name)
    local_dir = dir_name
    print('Creating a working dir for usr repo', local_dir)
    repo = pygit2.init_repository(local_dir, False)
    print('New repo for usr is:', repo)
# 提交记录模块
# 显示最新的和所有的记录，暂时只能显示提交附带的msg，不能显示出作者提交人和时间等信息
# 显示最新的提交记录
def show_HEAD_commit(dir):
    repo = Repository(dir + '.git')
    commit = repo[repo.head.target]
    print(commit.message)
# git log 查看git日志
def log(dir):
    repo = Repository(dir)
    last = repo[repo.head.target]
    for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
        print(commit.message)

# 提交文件模块
# 编辑文件后提交,所有的对于单个文件的更,包括新建文件都可以调用这个函数
# 提交函数应该包括用户仓库路径，文件在本地的相对路径
# 例如：用户主目录：/home/bob/apps/CodeHub/SCUT_JERRY, 他的一个仓库：/test,
# test的目录结构：
# test—new－try.py
#      |
#      test.md
# 那么更改 try.py,应该提交的参数应该是：
# working_dir:/home/bob/apps/CodeHub/SCUT_JERRY
# wenjian:new/try.py
# 最后,从后台应该传来提交人的【名字】以及他的【邮箱】进行提交签名
# 这里最好不要用默认的配置,每次都传一下比较好
def change_commit(working_dir, wenjian, edit_msg, usr_name, usr_email):
    repo = Repository(working_dir + '.git')
    index = repo.index
    # print(index.diff_to_workdir)
    index.add(wenjian)
    index.write()
    oid = index.write_tree()
    author = pygit2.Signature(usr_name, usr_email, int(time.time()), 480)
    reference_name = repo.head.name
    father = repo.head.target
    repo.create_commit(reference_name, author, author, edit_msg, oid, [father])
    print('Commit complete successfully! Time is ',time.localtime())
# 未测试！提交所有的修改
def all_commit(working_dir,all, edit_msg, usr_name, usr_email):
    repo = Repository(working_dir + '.git')
    index = repo.index
    # print(index.diff_to_workdir)
    index.add_all(all)
    index.write()
    oid = index.write_tree()
    author = pygit2.Signature(usr_name, usr_email, int(time.time()), 480)
    reference_name = repo.head.name
    father = repo.head.target
    repo.create_commit(reference_name, author, author, edit_msg, oid, [father])
    print('Commit complete successfully! Time is ',time.localtime())


# 分支操作模块
# 合并分支
def merge(dir, reference, msg):
    repo = Repository(dir)
    other_branch_ref = repo.lookup_reference(reference)
    other_branch_tip = other_branch_ref.target
    # repo.merge(other_branch_tip)
    print('merge complete!')
    user = repo.default_signature
    tree = repo.index.write_tree()
    message = msg
    new_commit = repo.create_commit('HEAD', user, user, message, tree, [repo.head.target, other_branch_tip])
    print(new_commit)

# 下面是一些简单的分支操作
# 显示所有的branch,所有的引用,并返回一个branch列表,用户登陆的时候可以调用
def show_branches_refs(dir):
    repo = Repository(dir)
    branches_list = list(repo.branches)
    print(branches_list)
    all_refs = list(repo.references)
    print(all_refs)
    return branches_list
# 新建并且切换分支
def new_switch_branch(working_dir, branch_name):
    repo = Repository(working_dir + '.git')
    commit = repo.revparse_single('HEAD')
    new_branch = repo.branches.create(branch_name, commit, force=False)
    repo.checkout('refs/heads/' + new_branch.branch_name)
    print('switch to a new branch: ' + branch_name)
# 新建分支
def new_branch(working_dir, branch_name):
    repo = Repository(working_dir + '.git')
    commit = repo.revparse_single('HEAD')
    new_branch = repo.branches.create(branch_name, commit, force=False)
    print('new branch ' + branch_name)
# 切换分支
def switch_branch(working_dir, branch_name):
    repo = Repository(working_dir + '.git')
    print('switch to: ' + branch_name)
    branch = repo.branches[branch_name]
    repo.checkout('refs/heads/' + branch.branch_name)
# 删除分支
def delete_branch(working_dir, branch_name):
    repo = Repository(working_dir + '.git')
    repo.branches.delete(branch_name)


# 调试函数，查看 pygit2 部署情况
# 加载查看工作目录
def check(dir):
    repo = Repository(dir + '.git')
    print('Path to the git repository is:', repo.path)
    if not repo.is_bare:
        print('Working directory of the repository is', repo.workdir)
    return repo




import os.path
rootdir = '/home/picher/workSpace/rep_for_bob/'                                  # 指明被遍历的文件夹
def walk():
    for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for dirname in dirnames:  # 输出文件夹信息
            print "parent is:" + parent
            print  "dirname is" + dirname
            for filename in filenames:  # 输出文件信息
                print "parent is: " + parent
                print "filename is:" + filename
                print "the full name of the file is:" + os.path.join(parent, filename)  # 输出文件路径信息
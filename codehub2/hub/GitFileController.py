from . import mygit, FileController
from mygit import *
from FileController import *

def create_working_dir(dir_name,usr_name,usr_email):
	FileController.create_dir(dir_name)
	mygit.create_working_dir(dir_name,usr_name,usr_email)
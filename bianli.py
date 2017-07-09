import os 
import os.path
rootdir='/Users/jiangjiawei/Desktop/gen_dir'

for parent,dirnames,filenames in os.walk(rootdir):
	print parent
	#return all full_dir name

	print dirnames
	#return list(element is dir name) that all dir contains

	print filenames
	#return list (element is file name) that all dir contains

##This module is used to work/interact with OS to automate many task like 
#creating Dir,removing Dir,identifying cureent working directory etc
import os
#os
#os.path
#os.system()
#os.walk()


#Basic OS module operation
#os.getcwd()
#print(os.getcwd())
#os.chdir("/path/ to which where u need to move")

#os.listdir
#print(os.listdir())

#os.mkdir()
#os.mkdir("Dire path/name")

#os.makedirs(path) (Recursive directory creation)

#os.makedirs("xyz/abz/cda")

#os.remove("path")
#os.removedirs("path")
#os.rmdir("path")
#os.rename(src,dst)

#print(os.environ)

#print(os.getuid())


#OS.PATH operation--Submodule of os module

#os.path.sep
#os.path.basename(path)
#os.path.dirname(path)

#path=/home/ec2-user/test.py
#print(os.path.basename(path))----test.py
#print(os.path.dirname(path))----/home/ec2-user/

#os.path.join(path1,path2)
#os.path.split(path)---is used to split the path name into a pair head and tail
#os.path.getsize(path)---in bytes
#os.path.exists(path)----True/false if my path is exists or not
#os.path.isfile(path)----path is file path 
#os.path.isdir(path)----path os dir or not
#os.path.islink(path)---is softlink or not

#os.walk used to generate directory and file names in directory tree by walking

path="C://Users/SA20508925//Desktop//"
#print(list(os.walk(path)))
for r,d,f in os.walk(path):
    print(r,d,f)



#Read a path and identify files and directory
import os
'''
path=input("Enter your directory")
print(os.listdir(path))
'''
req_path=input("Enter the require path: ")
if os.path.isfile(req_path):
    print(f"given path {req_path} is a file.please enter only directory path")
else:
    all_f_ds=os.listdir(req_path)
    if len(all_f_ds)==0:
        print(f"The given path {req_path} is an empty path")
    else:
        req_ext=input("Enter the require extension .py/.txt/.log/.sh: ")
        req_files=[]
        for each_f in all_f_ds:
            if each_f.endswith(req_ext):
               req_files.append(each_f)  
        if len(req_files)==0:
            print(f"There are no {req_ext} file in given path {req_path}")
        else:           
            print(f"The required files are : {req_files} ")       
       



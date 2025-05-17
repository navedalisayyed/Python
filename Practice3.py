import os
req_path=input("Enter path to change working dir: ")
print("the current working dir is ",os.getcwd())
try:
    os.chdir(req_path)
    print("Now your new working dir is :" ,os.getcwd())
except FileNotFoundError:
    print("Given path is not valid path")
except NotADirectoryError:
    print("Given path is file path")
except PermissionError:
    print("You dont have access to change for the given path")
except Exception as e:
    print(e)                
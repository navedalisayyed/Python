import os
path=input("Enter your path: ")
if os.path.exists(path):

    if os.path.isfile(path):
        print(f"The Given {path} is a file")
    else:
        print(f"The Given {path} is a dir")    
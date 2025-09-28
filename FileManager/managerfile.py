#https://youtu.be/cEfgjU5Zlu0


import os
import shutil 
path=input("enter your path : ")

files=os.listdir(path)

for i in files:
    filename,extension = os.path.splitext(i)
    extension_1=extension[1:]
    folder_path=path+"\\"+ extension_1
    if os.path.exists():
        # print("True")
        shutil.move(path+"\\"+i,path+"\\"+extension_1+"\\"+i)
    else:
        # print("False")
        os.makedirs(folder_path)
        shutil.move(path+i,path+"\\"+extension_1+"\\"+i)
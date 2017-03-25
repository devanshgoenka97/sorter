#!usr/bin/env/python
import os
import shutil
#Shivam's change
#second change
#Third change from fork
#The Path of the directory to be sorted
path = '/path/to/directory'
#This populates a list with the filenames in the directory
list_ = os.listdir(path)

#Traverses every file
for file_ in list_:
    name,ext = os.path.splitext(file_)
    #Stores the extension type
    ext = ext[1:]
    #If it is directory, it forces the next iteration
    if ext == '':
        continue
    #If a directory with the name 'ext' exists, it moves the file to that directory
    if os.path.exists(path+'/'+ext):
       shutil.move(path+'/'+file_,path+'/'+ext+'/'+file_)
    #If the directory does not exist, it creates a new directory
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file_,path+'/'+ext+'/'+file_)

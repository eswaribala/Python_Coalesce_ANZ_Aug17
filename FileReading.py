# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:00:26 2017

@author: BALASUBRAMANIAM
"""
import os
filePath=r"F:\yatrabakup\day6"

for dirpath,dirnames,filenames in os.walk(filePath):
    print(filenames)
    for x in filenames:
        print(x)
        (shortname,extension)=os.path.splitext(x)
        print(extension)
        if(extension=='.txt'):
            path=filePath+"/"+x
            contents=open(path,mode='r')
            for line in contents:
                print(line)
    
''' 
if(os.path.exists(filePath)):
    print("File Exists")
    (shortname, extension) = os.path.splitext(filename)
    print(extension)
    if(extension=='.txt'):
       contents=open(filePath,mode='r')
       for line in contents:
           print(line)
else:
    print("File Not found")
'''

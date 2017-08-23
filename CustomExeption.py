# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:21:28 2017

@author: BALASUBRAMANIAM
"""

class AgeException(Exception):
    """Raised when Age is negative number"""
    
    pass

class NameException(Exception):
     """Raised when Name is not in only alphabets"""
    
     pass

try:
    
    age=input("Enter Age")
    if (int(age)<0):
        raise AgeException
except AgeException:
       print("Age cannot be negative number")
       
import re

try:
   name=input("Enter Name")
   match = re.search(r'^[A-Za-z]*$', name) 
   if match:
        print(match.group())
   else:
       raise NameException
except NameException:
    print("Name cannot have numbers or special chars")


# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 12:10:43 2017

@author: BALASUBRAMANIAM
"""

class MobilePhone:
    #parameterized constructor
    def __init__(self, ram,im,sec,pro,disp):
        #properties
        self.RAM=ram
        self.internalMemory=im
        self.security=sec
        self.processor=pro
        self.display=disp
        
    def setInternalMemory(self,im):
        self.internalMemory=im
    #behaviour    
    def specifications(self):
        print(self.RAM)
        print(self.internalMemory)
        print(self.display) 

#object 
redmi=MobilePhone("4GB","64GB",False,"Octa","1200x1600")
redmi.specifications()
#object 
iphone=MobilePhone("8GB","32GB",True,"Octa","1200x1400")
print("Before Modifications.....")
iphone.specifications()
iphone.setInternalMemory("64GB")
print("After Modifications.....")
iphone.specifications()



        
        
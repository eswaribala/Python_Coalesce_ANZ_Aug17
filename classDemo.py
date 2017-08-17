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
        
    def getProcessor(self):
        return self.processor
    #behaviour    
    def specifications(self):
        print(self.RAM)
        print(self.internalMemory)
        print(self.display) 
        
        
        
class Customer:
    def __init__(self,custId,pwd,actno,mNo):
        self.customerId=custId
        self.password=pwd
        self.accountNo=actno
        self.mobileNo=mNo
        
    def getCustomerId(self):
        return self.customerId
        
    def getPassword(self):
        return self.password
    def getCustomerId(self):
        return self.customerId
    def getAccountNo(self):
        return self.accountNo
    def getMobileNo(self):
        return self.mobileNo
        
#inheritance
class PlatinumCustomer(Customer):
  
    def __init__(self,custId,pwd,actno,mNo,cashbackoffer,
                 rewardpoints):
        Customer.__init__(self,custId,pwd,actno,mNo)
        self.cashbackOffer=cashbackoffer
        self.rewardPoints=rewardpoints
        
    def customerInformation(self):
        print(self.customerId)
        print(self.accountNo)
        print(self.rewardPoints)
        

        
        
 


#object 
redmi=MobilePhone("4GB","64GB",False,"Octa","1200x1600")
print(redmi.getProcessor())
#object 
iphone=MobilePhone("8GB","32GB",True,"Quad","1200x1400")
print(iphone.getProcessor())
print("Before Modifications.....")
iphone.specifications()
iphone.setInternalMemory("64GB")
print("After Modifications.....")
iphone.specifications()


#create customer object
c1=Customer(24576,"Test@123",593675786,9952032457)
c2=Customer(24567,"Test@123",593675734,9952033456)
c3=Customer(24555,"Test@123",593675456,9952037867)

#print data 
print(c1.getMobileNo())

c4=PlatinumCustomer(43873,"Test@123",3578643,8056010298,0.05,0)
c4.customerInformation()






        
        
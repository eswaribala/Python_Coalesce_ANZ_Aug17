# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:54:28 2017

@author: BALASUBRAMANIAM
"""

import pymysql

def createConnection():
    conn = pymysql.connect(host="localhost",user="root",
                   passwd="vignesh",
                   db="anz_bankdb")
    return conn


def fetchAllRecords():
    conn=createConnection()
    query = "select * from Customer"
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def fetchByCustomerId(customerId):
    conn=createConnection()
    cursor=conn.cursor()
    cursor.execute("""select * from Customer where 
    Customer_Id='%d'""" %(customerId))
    return cursor.fetchall()


rows=fetchByCustomerId(235476)
for row in rows:
    for col in row:
        print(col,end='\t')
        

 




 



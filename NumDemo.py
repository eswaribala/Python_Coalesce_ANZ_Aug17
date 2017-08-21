# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 19:32:32 2017

@author: BALASUBRAMANIAM
"""

import numpy as np

a = np.array([[1.0, 2.0], [3.0, 4.0]])
print(a)
print(a.transpose())
print(a.diagonal())
print(a.flatten())
#matrix inverse
print(np.linalg.inv(a))
#Eigeon Values
print(np.linalg.eig(a))

#bitwise and
print(np.bitwise_and(13, 17))

#pack the bits
a = np.array([[[1,0,1],
                [0,1,0]],
              [[1,1,0],
               [0,0,1]]])
b = np.packbits(a, axis=-1)
print(b)

#binary representation
print(np.binary_repr(-3, width=5))

#swap case
c=np.array(['a1B c','1b Ca','b Ca1','cA1b'],'S5'); 
print(np.char.swapcase(c))

#business calendar
bdd = np.busdaycalendar(
             holidays=['2011-07-01', '2011-07-04', '2011-07-17'])
print(bdd.holidays)

'''
data=np.arange(15).reshape(5,3)
print(data.shape)
print(data)

a = np.floor(10*np.random.random((3,4)))



a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"
import numpy as np

a = np.zeros((2,2))   # Create an array of all zeros
print(a)              # Prints "[[ 0.  0.]
                      #          [ 0.  0.]]"

b = np.ones((1,2))    # Create an array of all ones
print(b)              # Prints "[[ 1.  1.]]"

c = np.full((2,2), 7)  # Create a constant array
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"

d = np.eye(2)         # Create a 2x2 identity matrix
print(d)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"

e = np.random.random((2,2))  # Create an array filled with random values
print(e)                     # Might print "[[ 0.91940167  0.08143941]
                             #               [ 0.68744134  0.87236687]]"

'''

















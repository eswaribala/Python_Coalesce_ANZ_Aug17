# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import scipy
data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2010_alcohol_consumption_by_country.csv')
df = data[0:10]

mean = np.mean(data['alcohol'])
st_dev = np.std(data['alcohol'])

print("The mean is %r" %(mean))
print("The standard deviation is %r" %(st_dev))
median = np.median(data['alcohol'])
maximum = np.max(data['alcohol'])
minimum = np.min(data['alcohol'])
a = [15, 20, 35, 40, 50]
perc =  np.percentile(a,100)

print("The median is %r" %(median))
print("The maximum is %r" %(maximum))
print("The minimum is %r" %(minimum))
print("The percentile is %r" %(perc))
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 06:50:33 2017

@author: BALASUBRAMANIAM
"""

import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pylab as plb
df = pd.DataFrame(columns=('Time', 'Sales'))
start_date = dt.datetime(2015, 7,1)
end_date = dt.datetime(2015, 7,10)
daterange = pd.date_range(start_date, end_date)
for single_date in daterange:
 row = dict(zip(['Time', 'Sales'],
     [single_date,
     int(50*np.random.rand(1))]))
 row_s = pd.Series(row)
 row_s.name = single_date.strftime('%b %d')
 df = df.append(row_s)
df.ix['Jul 01':'Jul 10', ['Time', 'Sales']].plot()
z = np.polyfit(range(0, 10),
    df.as_matrix(['Sales']).flatten(), 1)
p = np.poly1d(z)
plb.plot(df.as_matrix(['Sales']),
   p(df.as_matrix(['Sales'])), 'm-')
plt.ylim(0, 50)
plt.xlabel('Sales Date')
plt.ylabel('Sale Value')
plt.title('Plotting Time')
plt.legend(['Sales', 'Trend'])
plt.show()
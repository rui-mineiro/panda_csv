#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 21:54:37 2022

@author: minas
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dl


# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html
# plt.get_fignums()

# data=pd.read_csv('data.csv',index_col=0, parse_dates=True)
data=pd.read_csv('data2.csv',index_col=0, parse_dates=True)
data=data.sort_index()
data['MOUNT']=data.cumsum(axis=0)
data.drop('VALUE', axis=1, inplace=True)
data['MOUNT']=data['MOUNT']-data['MOUNT'].min()

fig, ax = plt.subplots()
xtime=dl.date2num(data.index)
ax.set_xticks(xtime)
border=(max(xtime)-min(xtime))*0.05
xlmin=min(xtime)-border
xlmax=max(xtime)+border
ax.set_xlim(left=xlmin , right=xlmax)
# ax.set_xticklabels(data.index,rotation=90)
plt.step(xtime,data.iloc[:,0])





# data.plot()

# ax.set_xticks(data.iloc[:, 0])

# ax.set_xticklabels(data.index.strftime('%Y-%m-%d %H:%M:%S'),rotation=40)
# ax.set_xticklabels(data.index.strftime('%Y-%m-%d %H:%M:%S'))

plt.show()

# head  -500 data2_original.csv > data2.csv ; ./show_csv.py



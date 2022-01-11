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

data=pd.read_csv('data.csv')
fig, ax = plt.subplots()
xtime=dl.date2num(data.iloc[:, 0])
ax.set_xticks(xtime)
border=(max(xtime)-max(xtime))*0.05
xlmax=min(xtime)-border
xlmin=max(xtime)+border
ax.set_xlim(left=xlmax , right=xlmin)




# data.plot()

# ax.set_xticks(data.iloc[:, 0])

# ax.set_xticklabels(data.index.strftime('%Y-%m-%d %H:%M:%S'),rotation=40)
# ax.set_xticklabels(data.index.strftime('%Y-%m-%d %H:%M:%S'))

# plt.show()



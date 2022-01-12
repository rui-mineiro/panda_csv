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

data=pd.read_csv('data.csv',index_col=0, parse_dates=True)

fig, ax = plt.subplots()
# xtime=dl.date2num(data.index)
# ax.set_xticks(xtime)
# border=(max(xtime)-min(xtime))*0.05
# xlmax=min(xtime)-border
# xlmin=max(xtime)+border
# ax.set_xlim(left=xlmin , right=xlmax)
# ax.set_xticklabels(data.index,rotation=90)





data.plot()


# ax.set_xticks(data.iloc[:, 0])

# ax.set_xticklabels(data.index.strftime('%Y-%m-%d %H:%M:%S'),rotation=40)
# ax.set_xticklabels(data.index.strftime('%Y-%m-%d %H:%M:%S'))

# plt.show()



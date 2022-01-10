#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 21:54:37 2022

@author: minas
"""
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

def loadData(fname):
    data=pd.read_csv(fname,header=0, index_col=0, parse_dates=True, squeeze=True)
    return data


data=loadData('data.csv')
data.bar()
# fig = pyplot.figure()
# ax = fig.add_subplot(111)
# ax.set_xticks(data)
# ax.set_xticklabels(data.index.strftime('%Y-%m-%d %H:%M:%S'),rotation=40)
# Hello
# Hello

#   data.show()
plt.show()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 21:54:37 2022

@author: minas
"""
import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv('data.csv')
X = list(data.iloc[:, 0])
Y = list(data.iloc[:, 1])
plt.bar(X, Y, color='g', align='edge')
plt.show()


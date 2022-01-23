#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 21:54:37 2022

@author: minas
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dl
from matplotlib.widgets import Slider
from matplotlib.widgets import RangeSlider


data=pd.read_csv('data2.csv',index_col=0, parse_dates=True)
data=data.sort_index()
data['MOUNT']=data.cumsum(axis=0)
data.drop('VALUE', axis=1, inplace=True)
data['MOUNT']=data['MOUNT']-data['MOUNT'].min()

fig, ax = plt.subplots(1, 1, figsize=(10, 5))
plt.subplots_adjust(bottom=0.35)

num_weeks=3
iloc_start=100
iloc_end=5000


x=dl.date2num(data.index[iloc_start:iloc_end])
y=data.iloc[iloc_start:iloc_end,0]

weeks     = dl.WeekdayLocator(byweekday=6)
weeks_fmt = dl.DateFormatter('%a, %d %b')

days     = dl.DayLocator()
days_fmt = dl.DateFormatter('%a')

ax.xaxis.set_major_locator(weeks)
ax.xaxis.set_major_formatter(weeks_fmt)


ax.xaxis.set_minor_locator(days)
ax.xaxis.set_minor_formatter(days_fmt)


ax.tick_params(axis="x", which="both", rotation=90)

plt.step(x,y)

slide_start = plt.axes([0.20, 0.1 , 0.60, 0.03])
slide_end   = plt.axes([0.20, 0   , 0.60, 0.03])

# slider = RangeSlider(ax_slide, "Period", x.min(), x.max())
slider_start = Slider(slide_start, "Start" , 15 , 30 , valinit=20 )
slider_end   = Slider(slide_end  , "End"   , 15 , 30 , valinit=20 )


plt.show()


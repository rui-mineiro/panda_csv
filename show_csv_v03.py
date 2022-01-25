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
from datetime import datetime, timedelta , date


data=pd.read_csv('data2.csv',index_col=0, parse_dates=True)
data=data.sort_index()
data['MOUNT']=data.cumsum(axis=0)
data.drop('VALUE', axis=1, inplace=True)
data['MOUNT']=data['MOUNT']-data['MOUNT'].min()

idx_str=0
idx_end=data.size-1

day_str_delta=0
day_end_delta=data.index[idx_end]-data.index[idx_str]



def x(idx_str,idx_end,data):
    return dl.date2num(data.index[idx_str:idx_end])

def y(idx_str,idx_end,data):
    return data.iloc[idx_str:idx_end,0]


fig, ax = plt.subplots(1, 1, figsize=(10, 5))
line,= plt.step(x(idx_str,idx_end,data),y(idx_str,idx_end,data))
plt.subplots_adjust(bottom=0.35)

weeks     = dl.WeekdayLocator(byweekday=6)
weeks_fmt = dl.DateFormatter('%a, %d %b')

days     = dl.DayLocator()
days_fmt = dl.DateFormatter('%a')

ax.xaxis.set_major_locator(weeks)
ax.xaxis.set_major_formatter(weeks_fmt)

ax.xaxis.set_minor_locator(days)
ax.xaxis.set_minor_formatter(days_fmt)

ax.tick_params(axis="x", which="both", rotation=90)


slide_start = plt.axes([0.20, 0.1   , 0.60, 0.03])
slide_end   = plt.axes([0.20, 0.05  , 0.60, 0.03])

slider_start = Slider(slide_start, "Start" , 0 , 30 , valinit=0 )
slider_end   = Slider(slide_end  , "End"   , 0 , 30 , valinit=20 )

def update(val):
    idx_str=slider_start.val
    idx_end=slider_end.val
    line.set_xdata(x(idx_str,idx_end,data))
    line.set_ydata(y(idx_str,idx_end,data))
    fig.canvas.draw_idle()

slider_start.on_changed(update)
slider_end.on_changed(update)

plt.show()

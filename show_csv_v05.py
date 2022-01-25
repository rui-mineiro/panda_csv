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


data_csv=pd.read_csv('data2.csv',index_col=0, parse_dates=True)
data_csv=data_csv.sort_index()
data_csv['MOUNT']=data_csv.cumsum(axis=0)
data_csv.drop('VALUE', axis=1, inplace=True)
data_csv['MOUNT']=data_csv['MOUNT']-data_csv['MOUNT'].min()

data=data_csv
idx_str=0
idx_end=data_csv.size-1
day_start=0
day_delta=data_csv.index[idx_end]-data.index[idx_str]
day_end=day_delta.days


def set_data(day_str,day_end):
    # str_date = data_csv.index[0]+day_str
    str_date = data_csv.index[0]+timedelta(days=day_str)
    end_date = data_csv.index[0]+timedelta(days=day_end)
    mask=(data_csv.index > str_date) & (data_csv.index <= end_date)
    data=data_csv.loc[mask]
    return data


def reset_data():
    return data_csv


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

slider_start = Slider(slide_start, "Start" , day_start , day_end , valinit=0 )
slider_end   = Slider(slide_end  , "End"   , day_start , day_end , valinit=20 )

def update(val):
    data=set_data(slider_start.val,slider_end.val)
    line.set_xdata(x(idx_str,idx_end,data))
    line.set_ydata(y(idx_str,idx_end,data))
    fig.canvas.draw_idle()

slider_start.on_changed(update)
slider_end.on_changed(update)

plt.show()


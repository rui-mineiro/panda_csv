#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dl
from matplotlib.widgets import Slider,Button
from datetime import timedelta

def set_data(day_str,day_end):
    str_date = data_csv.index[0]+timedelta(days=day_str)
    end_date = data_csv.index[0]+timedelta(days=day_end)
    mask=(data_csv.index > str_date) & (data_csv.index <= end_date)
    data=data_csv.loc[mask]
    return data

def update_str(val):
    if slider_end.val < ( slider_start.val + 1 ) :
        slider_end.set_val(slider_start.val + 1)
    data=set_data(slider_start.val,slider_end.val)
    x=dl.date2num(data.index)
    y=data.iloc[:,0]
    line.set_xdata(x)
    line.set_ydata(y)
    ax.set_xlim([data.index[0],data.index[-1]])
    fig.canvas.draw_idle()

def update_end(val):
    if slider_start.val > ( slider_end.val - 1 ) :
        slider_start.set_val(slider_end.val - 1)
    data=set_data(slider_start.val,slider_end.val)
    x=dl.date2num(data.index)
    y=data.iloc[:,0]
    line.set_xdata(x)
    line.set_ydata(y)
    ax.set_xlim([data.index[0],data.index[-1]])
    fig.canvas.draw_idle()

def resetData(event):
    data=set_data(day_start,day_end)
    x=dl.date2num(data.index)
    y=data.iloc[:,0]
    slider_start.reset()
    slider_end.reset()
    line.set_xdata(x)
    line.set_ydata(y)
    ax.set_xlim([data.index[0],data.index[-1]])
    fig.canvas.draw_idle()
    


data_csv=pd.read_csv('data2.csv',index_col=0, parse_dates=True)
data_csv=data_csv.sort_index()
data_csv['MOUNT']=data_csv.cumsum(axis=0)
data_csv.drop('VALUE', axis=1, inplace=True)
data_csv['MOUNT']=data_csv['MOUNT']-data_csv['MOUNT'].min()
day_start=0
day_delta=data_csv.index[-1]-data_csv.index[0]
day_end=day_delta.days
data=set_data(day_start,day_end)
    
fig, ax = plt.subplots(1, 1, figsize=(10, 5))
x=dl.date2num(data.index)
y=data.iloc[:,0]
line,= plt.step(x,y)
ax.set_xlim([data.index[0],data.index[-1]])
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
slider_end   = Slider(slide_end  , "End"   , day_start , day_end , valinit=day_end )

resetax = plt.axes([0.85, 0.04, 0.1, 0.04])
button = Button(resetax, 'Reset', color='0.85',hovercolor='skyblue')



slider_start.on_changed(update_str)
slider_end.on_changed(update_end)
button.on_clicked(resetData)

plt.show()


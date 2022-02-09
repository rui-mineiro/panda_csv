#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dl
from matplotlib.widgets import Slider
from datetime import timedelta

def set_data(day_str,day_end):
    if day_end-day_str>5 :
        majl=dl.WeekdayLocator(byweekday=6)
        majl_fmt=dl.DateFormatter('%a, %d %b')
        minl=dl.DayLocator()
        minl_fmt=dl.DateFormatter('%a')
    else:
        majl=dl.DayLocator()
        majl_fmt=dl.DateFormatter('%a, %d %b')
        minl=dl.HourLocator()
        minl_fmt=dl.DateFormatter('%H:%M')
    ax.xaxis.set_major_locator(majl)
    ax.xaxis.set_major_formatter(majl_fmt)
    ax.xaxis.set_minor_locator(minl)
    ax.xaxis.set_minor_formatter(minl_fmt)
    str_date = data_csv.index[0]+timedelta(days=day_str)
    end_date = data_csv.index[0]+timedelta(days=day_end)
    str_date=data_csv[data_csv.index > str_date ].head(1).index[0]
    end_date=data_csv[data_csv.index > end_date].head(1).index[0]
    return [str_date,end_date]

def update_str(val):
    if slider_start.val > (slider_end.val - 1):
       if slider_start.val > day_end - 1  :
        slider_end.set_val(day_end)
        slider_start.set_val(day_end-1)            
       else:
        slider_end.set_val(slider_start.val + 1)
    data=set_data(slider_start.val,slider_end.val)
    ax.set_xlim(data)
    fig.canvas.draw_idle()

def update_end(val):
    if slider_end.val < (slider_start.val + 1):
       if slider_end.val < day_start + 1  :
        slider_start.set_val(day_start)
        slider_end.set_val(day_start+1)            
       else:
        slider_start.set_val(slider_end.val - 1)
    data=set_data(slider_start.val,slider_end.val)
    ax.set_xlim(data)
    fig.canvas.draw_idle()



data_csv=pd.read_csv('data8.csv',index_col=0,parse_dates=True , dtype = {'VALUE':'float16'}, names=('DATE','VALUE','ACTIVITY'), sep='\t')
data_csv=data_csv.sort_index()
activity = data_csv['ACTIVITY'].unique()
if len(activity)==1: 
  data_csv[activity]=activity[0]
else:
  data_csv[activity]=activity
mask=data_csv[activity].eq(data_csv['ACTIVITY'], axis=0)
data_csv[activity]=data_csv[activity].where( mask, other=0)
data_csv[activity]=data_csv[activity].where(~mask, other=data_csv['VALUE'],axis=0)
data_csv.drop('VALUE'   , axis=1, inplace=True)
data_csv.drop('ACTIVITY', axis=1, inplace=True)
data_csv[activity]=data_csv[activity].cumsum(axis=0)
data_csv[activity]=data_csv[activity].cumsum(axis=1)




x=dl.date2num(data_csv.index)
y=data_csv.T.values.tolist()

fcolor=['b','c','m','r','y','g','k']
fig, ax = plt.subplots(1, 1, figsize=(10, 5) )
ax.fill_between(x, 0, y[0], facecolor='b', step='post',label=activity[0])
ativities=len(activity)
if ativities>1:
    lineN=list(range(1,ativities))
    for n in lineN:
     ax.fill_between(x, y[n-1], y[n], facecolor=fcolor[n], step='post',label=activity[n])


ax.legend(loc='upper left')
ax.set_xlim([data_csv.index[0],data_csv.index[-1]])
ax.set_ylim([0,sum(y[-1])/len(y[-1])*3])
plt.subplots_adjust(bottom=0.35)


ax.tick_params(axis="x", which="both" , rotation=90)
ax.tick_params(axis="x", which="minor", labelsize=9)
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)


day_start=0
day_delta=data_csv.index[-1]-data_csv.index[0]
day_end=day_delta.days
slide_start = plt.axes([0.20, 0.1   , 0.60, 0.03])
slide_end   = plt.axes([0.20, 0.05  , 0.60, 0.03])
slider_start = Slider(slide_start, "Start" , day_start , day_end , valinit=0 )
slider_end   = Slider(slide_end  , "End"   , day_start , day_end , valinit=day_end )
slider_start.on_changed(update_str)
slider_end.on_changed(update_end)

plt.show()


#!/usr/bin/env python
# coding: utf-8

# In[88]:


import pandas as pd
import numpy as np
import plotly.express as px
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual


from datetime import datetime as dt
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from pylab import *


from plotly.subplots import make_subplots
import plotly.graph_objects as go


# In[89]:


df= pd.read_csv('D:/website/data/all_location/mumbai.csv')   #!!!!!!!!location change here!!!!!!!!!


# In[90]:


df = df.fillna(-99999)

df=df[(df.month>=1) & (df.month<=12)] 
df=df[(df.date>=1) & (df.date<=31)]
for column in ['year', 'month','date']:
    df[column] = df[column].astype(int)


# In[91]:





# # index-1: rainy day of each year!!!!!!!

# In[92]:


def rainyday(data):
    df11 = data.loc[data['rain']>2.5]
    a = df11.groupby(df11['year']).rain.count()
    a.to_csv("D:/website/data/pune_index/rainyday_year.txt")          #!!!!!!!!location change here!!!!!!!!!
    a.to_csv("D:/website/data/pune_index/rainyday_year.csv")          #!!!!!!!!location change here!!!!!!!!!
    dff = pd.read_csv('D:/website/data/pune_index/rainyday_year.csv') #!!!!!!!!location change here!!!!!!!!!
    fig = px.line(dff,x='year',y='rain', template="ggplot2")
       
    
    fig.update_layout(
    title={
        'text': "<b>Rainy Days/Year [pune(23.2599° N, 77.4126° E)]</b>",    #!!!!!!!!location and latlon change here!!!!!!!!!
        'y':0.97,
        'x':0.52,
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis_title="Years",
    yaxis_title="No of Rainy Days",
    #legend_title="Number of Rainy Days",
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="black")
    )
    
    fig.show()
#     fig.write_html("D:/website/data/pune_index/pune_yearlyrainyday.html", include_plotlyjs="cdn") #!!!!!!!!location change here!!!!!!!!!
    fig.write_image("D:/website/data/pune_index/pune_yearlyrainyday.png") #!!!!!!!!location change h


# # index-2:heavy rain day of each year!!!!!!!

# In[93]:


def heavyrain(data):
    df11=data.loc[data['rain']>80]
    a=df11.groupby(df11['year']).rain.count()
    a.to_csv("D:/website/data/pune_index/heavyrainfallday_year.txt")          #!!!!!!!!location change here!!!!!!!!!
    a.to_csv("D:/website/data/pune_index/heavyrainfallday_year.csv")          #!!!!!!!!location change here!!!!!!!!!
    dff = pd.read_csv('D:/website/data/pune_index/heavyrainfallday_year.csv') #!!!!!!!!location change here!!!!!!!!!
    fig=px.line(dff,x='year',y='rain', template="ggplot2")
    
    fig.update_layout(
    title={
        'text': "<b>Heavy Rainfall Days/Year [pune(23.2599° N, 77.4126° E)]</b>",  #!!!!!!!!location and latlon change here!!!!!!!!!
        'y':0.97,
        'x':0.52,
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis_title="Years",
    yaxis_title="Heavy Rainfall Days/Year",
    #legend_title="No of Heavy Rainfall Days",
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="black")
    )
    
    
    fig.show()
    #fig.write_html("D:/website/data/pune_index/pune_yearlyheavyrainfallday.html",include_plotlyjs="cdn") #!!!!!!!!location change here!!!!!!!!!
    fig.write_image("D:/website/data/pune_index/pune_yearlyheavyrainfallday.png")


# # index-3:Highest T/ year!!!!!!!

# In[94]:


def maxT(data):
    a=data.loc[data.groupby("year")["tmax"].idxmax()]
    a.to_csv("D:/website/data/pune_index/tmax_year.txt")          #!!!!!!!!location change here!!!!!!!!!
    a.to_csv("D:/website/data/pune_index/tmax_year.csv")          #!!!!!!!!location change here!!!!!!!!!
    dff = pd.read_csv('D:/website/data/pune_index/tmax_year.csv') #!!!!!!!!location change here!!!!!!!!!
    fig=px.line(dff,x='year',y='tmax', template="ggplot2")
    
    fig.update_layout(
    title={
        'text': "<b>Maximum Temperature/Year [pune(23.2599° N, 77.4126° E)]</b>",    #!!!!!!!!location and latlon change here!!!!!!!!!
        'y':0.97,
        'x':0.52,
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis_title="Years",
    yaxis_title="MaxT(deg C)/Year",
    #legend_title="No of Heavy Rainfall Days",
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="black")
    )
    
    fig.show()
    #fig.write_html("D:/website/data/pune_index/pune_yearlymaximumtemp.html",include_plotlyjs="cdn") #!!!!!!!!location change here!!!!!!!!!
    fig.write_image("D:/website/data/pune_index/pune_yearlymaximumtemp.png")


# # index-4:Minimum T/ year!!!!!!!

# In[95]:


def minT(data):
    a=data.loc[data.groupby("year")["tmin"].idxmin()]
    a.to_csv("D:/website/data/pune_index/tmin_year.txt")          #!!!!!!!!location change here!!!!!!!!!
    a.to_csv("D:/website/data/pune_index/tmin_year.csv")          #!!!!!!!!location change here!!!!!!!!!
    dff = pd.read_csv('D:/website/data/pune_index/tmin_year.csv') #!!!!!!!!location change here!!!!!!!!!
    fig=px.line(dff,x='year',y='tmax', template="ggplot2")
    
    fig.update_layout(
    title={
        'text': "<b>Minimum Temperature/Year [pune(23.2599° N, 77.4126° E)]</b>",     #!!!!!!!!location and latlon change here!!!!!!!!!
        'y':0.97,
        'x':0.52,
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis_title="Years",
    yaxis_title="MinT(deg C)/Year",
    #legend_title="No of Heavy Rainfall Days",
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="black")
    )
    
    
    
    fig.show()
    #fig.write_html("D:/website/data/pune_index/pune_yearlyminimumtemp.html",include_plotlyjs="cdn") #!!!!!!!!location change here!!!!!!!!!
    fig.write_image("D:/website/data/pune_index/pune_yearlymin imumtemp.png")


# # index:5 : consecutive wet day=CWD

# ### below section calculates the maximum number of consecutive (>=3days) days with rain >2.5mm 

# In[96]:


def CWD(data):
    data['dateInt']=data['year'].astype(str) + data['month'].astype(str).str.zfill(2)+ data['date'].astype(str).str.zfill(2)
    data['ymd'] = pd.to_datetime(data['dateInt'], format='%Y%m%d')
    data.drop(['dateInt'], axis=1)
    df = data.filter(['ymd','year','rain'], axis=1)

    df_wet = df[(df.rain >= 2.5)].dropna() #take rain more than 2.5mm
    df_wet['Newkey'] = df_wet.ymd.diff().dt.days.ne(1).cumsum()
    df_wet= df_wet.groupby(['Newkey','year'])['ymd'].agg(['first','last','count'])
    df_wet = df_wet[df_wet['count'] >= 3]  #three or more consecutive days raifall
    CWD=df_wet.loc[df_wet.groupby("year")["count"].idxmax()]

    CWD.to_csv("D:/website/data/mumbai_index/CWD_year.txt")                    #!!!!!!!!location change here!!!!!!!!!
    CWD.to_csv("D:/website/data/mumbai_index/CWD_year.csv")                    #!!!!!!!!location change here!!!!!!!!!
    df_plt = pd.read_csv('D:/website/data//mumbai_index/CWD_year.csv')          #!!!!!!!!location change here!!!!!!!!!
    fig = px.line(df_plt,x='year',y='count', template="ggplot2")

    fig.update_layout(
    title={
        'text': "<b>Consecutive Wet Days/Year [mumbai(23.2599° N, 77.4126° E)]</b>",    #!!!!!!!!location and latlon change here!!!!!!!!!
        'y':0.97,
        'x':0.52,
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis_title="Years",
    yaxis_title="Days/Year",
    #legend_title="No of Heavy Rainfall Days",
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="black")
    )


    fig.show()
    #fig.write_html("D:/website/data/mumbai_index/mumbai_yearlyCWD.html",include_plotlyjs="cdn") #!!!!!!!!location change here!!!!!!!!!
    fig.write_image("D:/website/data/mumbai_index/mumbai_yearlyCWD.png")


# In[97]:



# from plotly.subplots import make_subplots


# In[98]:


# def all(data):
#     fig = make_subplots(rows=2, cols=1)
#     fig.add_trace(rainyday(data),row=1,col=1)
#     fig.add_trace(heavyrain(data),row=2,col=1)


# In[99]:


def index_plot(data):
    rainyday(data)
    heavyrain(data)
    maxT(data)
    minT(data)
    CWD(data)
    #all(data)
    return


# In[100]:


index_plot(df)  
#fig.write_html("D:/website/data/srinagar_index/x.html",include_plotlyjs="cdn") #!!!!!!!!location change here!!!!!!!!!


# In[12]:


import sys,os
import cgi, cgitb
cgitb.enable()
form = cgi.FieldStorage()# Get data from fields
if form.getvalue('dropdown'):
   subject = form.getvalue('dropdown')
else:
   subject = 'Not entered'


# In[13]:


if(subject == "Rainyday/Year"):
    rainyday(data)
else:
    print('<h3>Choose the correct option!!</h3>')
    

if(subject == "Heavy Rainy Day/Year"):
    heavyrain(data)
else:
    print('<h3>Choose the correct option!!</h3>')
    
    
if(subject == "Maximum T/year"):
    maxT(data)
else:
    print('<h3>Choose the correct option!!</h3>')
    
    
if(subject == "Minimum T/Year"):
    minT(data)
else:
    print('<h3>Choose the correct option!!</h3>')
    
    
if(subject == "Consecutive Wet Days/Year"):
    CWD(data)
else:
    print('<h3>Choose the correct option!!</h3>')
    


# # This section is for local server publishing

# In[75]:


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


# In[50]:


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout=html.Div([
     html.H1(children='index 1'),
     dcc.Graph(
        id='index-graph',
        figure=index_plot(df)
     )
])


if __name__ == '__main__':
    app.run_server(debug=False)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[7]:


#import module
import os
from ipywidgets import interact, interactive, fixed, interact_manual

import ipywidgets as widgets

from ipywidgets import FloatSlider

from ipywidgets import VBox, HBox, interactive_output

from ipywidgets import Dropdown
from matplotlib.image import imread
from ipywidgets import Button
import pickle

from matplotlib import pyplot as plt
from matplotlib.pylab import subplots
from wordcloud import WordCloud
import numpy as np
from random import shuffle
from ipywidgets import IntSlider
import pandas as pd
from matplotlib.image import imread

from ipywidgets import AppLayout, Layout


# In[9]:


#data pre-process and define variables
#load data
path=os.path.abspath(os.path.dirname(os.getcwd()))+'\\'+'data\\'
data = pickle.load(open(path+'data_combined.p', 'rb'))

year_end=2019
year_start=2015
month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
start_month=1
end_month=(year_end-year_start+1)*12


time_idx=pd.date_range(start=str(year_start)+'0101',end=str(year_end)+'1231',freq='M')
fmt='%Y-%m'
options = [(item.strftime(fmt),item) for item in time_idx]

fsx=widgets.SelectionSlider(
            description='Period',
            options=options,
            continuous_update=False
        )
#This is the program running indicator
stat=widgets.Label(value="Please select a input time period")

loaded={}
loaded['like']=0
loaded['hate']=0
stat2=widgets.Label(value="Please select a input time period")

stat3=widgets.Label(value="Please select a input time period")
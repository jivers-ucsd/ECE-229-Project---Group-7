#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Authors:
#Guangjun Xue 
#Yuchen Zhang


# # This part is for tuning and degbugging. Please skip this part

# In[2]:


from ipywidgets import interact, interactive, fixed, interact_manual

import ipywidgets as widgets

from ipywidgets import FloatSlider

from ipywidgets import VBox, HBox, interactive_output

from ipywidgets import Dropdown
from matplotlib.image import imread
from ipywidgets import Button


# # Part I : Cloud Map Over Time

# In[3]:


import pickle
import os


# In[4]:


#load data
path=os.path.abspath(os.path.dirname(os.getcwd()))+'\\'+'data\\'
data = pickle.load(open(path+'data_combined.p', 'rb'))

# In[5]:


#data set is dictionary of different genres


# In[6]:


#structure of data
data['gaming'].head(100)


# In[7]:


from matplotlib import pyplot as plt
from matplotlib.pylab import subplots
from wordcloud import WordCloud
import numpy as np
from random import shuffle
from ipywidgets import IntSlider
import pandas as pd
from matplotlib.image import imread

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
def wordscloud(x,Genre):
    """
     This function is to plot graph for Part I : Cloud Map Over Time.
    x : input time
     Genre: different topics"""

    plt.cla()
    loading="Now loading..."
    plt.axis('off') 
    plt.text(0.5,0.5,loading)

    stat.value=loading    
    data_cloud=data[Genre]
    freq=np.array(list(data_cloud.frequency_time))
    string = ''
    m,n=freq.shape
    for i in range(m):
        time=str(x).split(' ')[0].split('-')
        col=(int(time[0])-year_start)*12+int(time[1])
        string=string+(data_cloud.loc[i].words+' ')*(freq[i,col-1])
    if string.split()==[]:
        """if there is no words shown"""
        string='There is no interesting word'
        plt.cla()
        plt.axis('off') 
        plt.text(0.5,0.5,string)

        plt.show()       
        stat.value='Complete! '
        return
    lis=string.split(' ')
    shuffle(lis)
    string=' '.join(lis)
    wc = WordCloud(
               background_color='white',max_words=20,
               width=1000,
               height=1000,
               ).generate(string)  #wordcloud
    plt.cla()
    plt.imshow(wc)  
    plt.axis('off') 
    plt.show()

    stat.value='Complete! '
interactive_plot = interactive(wordscloud,x=fsx,Genre=['cooking', 'influencers', 'gaming'])


# In[8]:


def test_partI():
    """This is the test function for Part I"""
    year_end=2019
    year_start=2015
    Genre=['cooking', 'influencers', 'gaming']
    time_idx=pd.date_range(start=str(year_start)+'0101',end=str(year_end)+'1231',freq='M')
    fmt='%Y-%m'
    options = [(item.strftime(fmt),item) for item in time_idx]
    shuffle(options)
    optionstest=[i[0] for i in options]
    for j in range(2):
        testx=optionstest[j]
        for i in Genre:
            wordscloud(testx,i)


# # Part II: Like and Dislike

# In[9]:


Genre= Dropdown(options=['cooking', 'influencers', 'gaming'])
Fsx=widgets.SelectionSlider(
            description='Period',
            options=options,
            continuous_update=False
        )
loaded={}
loaded['like']=0
loaded['hate']=0
stat2=widgets.Label(value="Please select a input time period")
def P_N_cloud(x,Genre):
    """
    This function is to plot graph for Part II: Like and Dislike words over time.
    x: input time
      Genre: diffenrent topics
      like: positive or negative result"""
    fig = plt.figure()
    loading="Now loading..."

    if loaded['like']==0 and loaded['hate']==0:

        stat2.value=loading
    
    data_cloud=data[Genre]
    data_cloud_like=data_cloud[data_cloud.polarity>0]
    data_cloud_hate=data_cloud[data_cloud.polarity<=0]
    like_hate=0
    for data_cloud in [data_cloud_like,data_cloud_hate]:
        like_hate+=1
        if like_hate==1:
            ax = fig.add_subplot(121)
            like='like'
        elif like_hate==2:
            ax = fig.add_subplot(122)
            like='hate'
        data_cloud=data_cloud.reset_index()
        freq=np.array(list(data_cloud.frequency_time))
        string = ''
        if freq.shape==(0,):
            string='There is no interesting word'
            ax.cla()
            ax.axis('off') 
            ax.text(0.5,0.5,string)

            loaded[like]=1
            if loaded['like']==1 and loaded['hate']==1:
                stat2.value='Complete! '
                loaded['like']=0
                loaded['hate']=0
            return

        m,n=freq.shape
        for i in range(m):
            time=str(x).split(' ')[0].split('-')
            col=(int(time[0])-year_start)*12+int(time[1])
            string=string+(data_cloud.loc[i].words+' ')*(freq[i,col-1])
        if string.split()==[]:
            """if there is no words shown"""
            string='There is no interesting word'
            ax.cla()
            ax.axis('off') 
            ax.text(0.5,0.5,string)

            loaded[like]=1
            if loaded['like']==1 and loaded['hate']==1:
                stat2.value='Complete! '
                loaded['like']=0
                loaded['hate']=0
            return
        lis=string.split(' ')
        shuffle(lis)
        string=' '.join(lis)
        wc = WordCloud(
                   background_color='white',max_words=20,
                   width=1000,
                   height=1000,
                   ).generate(string)  #wordcloud

        ax.cla()
        ax.imshow(wc)  
        ax.axis('off')
        if like=='like':
            ax.set_title('Positive')
        elif like=='hate':
            ax.set_title('Negative')

        loaded[like]=1
        if loaded['like']==1 and loaded['hate']==1:
            stat2.value='Complete! '
            loaded['like']=0
            loaded['hate']=0
    plt.show()
interactive_plot_like_hate = interactive(P_N_cloud,x=Fsx,Genre=Genre)


# In[10]:


def test_partII():
    """This function will test part II """
    year_end=2019
    year_start=2015
    Genre=['cooking', 'influencers', 'gaming']
    time_idx=pd.date_range(start=str(year_start)+'0101',end=str(year_end)+'1231',freq='M')
    fmt='%Y-%m'
    options = [(item.strftime(fmt),item) for item in time_idx]
    shuffle(options)
    optionstest=[i[0] for i in options]
    for j in range(2):
        testx=optionstest[j]
        for i in Genre:
            P_N_cloud(testx,i)


# # Part III: Text Analysis 

# In[11]:


stat3=widgets.Label(value="Please select a input time period")
def analyze_text_color(text, genre, metric):
    '''
    Purpose: 
    Analyze the given text and produce color labels for the words 
    Input:
    text = str; scalar depicting the text that needs to be analyzed
    genre = str; scalar depicting the genre of the content: "cooking", "gaming", "influencers"
    metric = str; scalar depicting the metric to base the analysis on: "likes_mean", "likes_median",
             "dislikes_mean", "dislikes_median", "views_mean", "views_median", "polarity", "subjectivity"
    Output:
    analysis = list; a list with the same number of elements as number of words in given text, with each
               corresponding element being the color for that word: "red" means bad, "yellow" means okay, "green"
               means good and "white" means "Not found" (in database)
    '''
    from textblob import TextBlob
    import pickle
    path=os.path.abspath(os.path.dirname(os.getcwd()))+'\\'
    pickle.load(open(path+'data_project.p', 'rb'))
    Blob = TextBlob(text)
    scores = []
    df_genre = data[genre]
    for word in list(Blob.words):
        if word in list(df_genre.words):
            word_index = df_genre.words[df_genre.words==word].index[0]
            scores.append(df_genre[metric][word_index])
        else:
            scores.append("Not found")
    intervals = [df_genre[metric].mean()-df_genre[metric].std(), df_genre[metric].mean()+df_genre[metric].std()]
    analysis = []
    for score in scores:
        if score=="Not found":
            analysis.append("white")#not found
            continue
        if score<=intervals[0]:
            analysis.append("red")#bad words
        elif score>intervals[0] and score<=intervals[1]:
            analysis.append("yellow")#okay words
        elif score>intervals[1]:
            analysis.append("green")#good words
    return analysis
w=widgets.Textarea(
    value='',
    placeholder='Type to analyze',
    description='Text box:',
    disabled=False,
    continuous_update=False
)
print(analyze_text_color('funny lives in splatoon', 'gaming', 'likes_mean'))
def color_changer(x,Genre,Metric):
    stat3.value='Now loading...'
    categorization = analyze_text_color(x,Genre,Metric)
    words = x.split()
    for word in words:
        color = analyze_text_color(word,Genre,Metric)
        if color[0] == "red":
            print('\033[31m %s' %word, end = "")
        elif color[0] == "yellow":
            print('\033[33m %s' %word, end = "")
        elif color[0] == "green":
            print('\033[32m %s' %word, end = "")
        else:
            print('\033[37m %s' %word, end = "")
    stat3.value='Complete!'

b1 = Button(description='Red for bad words')
b1.style.button_color = 'lightpink'
b2 = Button(description='Green for good words')
b2.style.button_color = 'lightgreen'
b3 = Button(description='Yellow for okay words')
b3.style.button_color = 'lightyellow'
b4 = Button(description='White for others')
button1 = widgets.VBox([b1,b2])
button2 = widgets.VBox([b3,b4])
labell=widgets.HBox([b1,b2,b3,b4])

box = interactive(color_changer,x=w,Genre=['cooking', 'influencers', 'gaming'],Metric=["likes_mean", "likes_median",
             "dislikes_mean", "dislikes_median", "views_mean", "views_median", "polarity", "subjectivity"])


# In[12]:


'''test_text_colors'''
def test_color():
    assert analyze_text_color('today we will cook delicious beef', 'cooking', 'subjectivity')==['yellow', 'white', 'yellow', 'yellow', 'green', 'yellow']
    assert analyze_text_color('amazing social skills', 'influencers', 'likes_mean')==['yellow', 'yellow', 'white']
    assert analyze_text_color('funny lives in splatoon', 'gaming', 'likes_mean')==['yellow', 'white', 'yellow', 'white']


# # Overall

# ## Displays below will be presented in the website.

# In[13]:


#description of all three parts
descrip_part1="""
In this part, you can use our tools to create a word cloud of popular words in different time periods. Size of a word will be based on
its popularity. 
 We also provide you with different genres to choose. You can check the popular words within the genre you have interest in.
 The time will be in a month and year format that the user can toggle with the slider and see how the word cloud changes over time.
"""
descrip_part2="""
A second display will compose of two word clouds that present the positive and negative words respectively, 
showcasing the words’ popularity based on its size. We determine Positive/Negative of a word by its polarity.
Based on a corpus generated at a lot of institutes across the world with experts in linguistics and psychology, 
we have a polarity and subjectivity defined for each word. Polarity is between -1 and +1. Positive polarity means that 
people have positive attitude towards the word.
"""
descrip_part3="""
Our Text Analysis tool will generate word connotations based on the words typed into the textbox.  
Words will be colored according to its positive or negative sentiment.
 For example, words in red denoting a negative word, words in yellow denoting neutral words and green denoting a positive word. Words that can not be 
 decided will remain in black.
 Also, you can select the genre and metric of interest. 
"""
Descrip_part1=widgets.HTML(value = f"<b><font size='2' color='Black'>{descrip_part1}</b>")
Descrip_part2=widgets.HTML(value = f"<b><font size='2' color='Black'>{descrip_part2}</b>")
Descrip_part3=widgets.HTML(value = f"<b><font size='2' color='Black'>{descrip_part3}</b>")


# In[14]:


#folder for different part
accordion = widgets.Accordion(children=[VBox([Descrip_part1,interactive_plot,stat]),
                                        VBox([Descrip_part2,
                                              HBox([interactive_plot_like_hate]),stat2]),
                                        VBox([Descrip_part3,box,labell,stat3])])
accordion.set_title(0, 'Popular Keywords over Time')
accordion.set_title(1, 'Likes&Dislikes over Time ')
accordion.set_title(2, 'Text Analysis ')


# In[15]:


#container for the main interface
from ipywidgets import AppLayout, Layout
title = 'Youtube Trend over Time'
Title = widgets.HTML(value = f"<b><font size='5' color='Black'>{title}</b>")
descrip="""How insane is it that sometimes you see the most amazing video on youtube, 
and yet it took nearly a decade for it to be popular? Or a subpar video which hits a 
million views within a week? A lot of it has to do with the way you market your content. 
Sponsoring advertisements for your posts helps, but it depends heavily on the 
textual supporting descriptions that you add. And an even deeper question is: what makes certain 
words more popular than others? What receives more hate by the public? Are certain 
topics more active during election years or during a pandemic? Fortunately, our platform and tools will figure it out for you
. We’re trying to create a simple 
platform which serves as a proof of concept for how sentiment analysis can be extended 
to utility on a daily basis, with a very wide customer demographic.
"""
Descrip=widgets.HTML(value = f"<b><font size='2' color='Black'>{descrip}</b>")
AppLayout(header=VBox([Title,Descrip]),
          left_sidebar=None,
          center=accordion,
          right_sidebar=None,
          footer=None)
          
          #widgets.IntSlider(description='c',
                                   #layout=Layout(height='auto', width='auto')))


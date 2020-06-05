loaded={}
loaded['like']=0
loaded['hate']=0
def P_N_cloud(x,Genre):
    """
    This function is to plot graph for Part II: Like and Dislike words over time.
    x: input time
      Genre: diffenrent topics
      like: positive or negative result"""
    #import modules
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
    
    import os
    os.system("__init__.py")
    #load data
    path=os.path.abspath(os.path.dirname(os.getcwd()))+'\\'
    data = pickle.load(open(path+'data_project.p', 'rb'))
    year_end=2019
    year_start=2015
    
    stat2=widgets.Label(value="Please select a input time period")
    
    
    
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
    #plt.show()
def wordscloud(x,Genre):
    """
     This function is to plot graph for Part I : Cloud Map Over Time.
    x : input time
     Genre: different topics"""
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
    
    import os
    os.system("__init__.py")
    #load data
    path=os.path.join(os.getcwd(),'data')
    path=os.path.join(path,'data_combined.p')
    data = pickle.load(open(path, 'rb'))
    
    year_end=2019
    year_start=2015
    
    stat=widgets.Label(value="Please select a input time period")
    
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

        #plt.show()       
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
    #plt.show()

    stat.value='Complete! '
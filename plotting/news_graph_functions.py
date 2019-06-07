# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:31:49 2019
@author: cyrus
"""
import numpy as np
import matplotlib.pyplot as plt

def bar(channel_names,pos_vals,neg_vals,title_name='Polarity Scores per Channel',x_lbl='News Channel',y_lbl='Percent'):
    '''
    plot the bar graphs for all channels
    Args:
        channel_names: list of news channel names as string ie ['FOX','BBC','CNN']
        pos_vals: contains the positive normalized values of each news channel in news_names
        neg_vals: contains the negative normalized values of each news channel in news_names
        title_name: name of plot title
        x_lbl: x axis label
        y_lbl: y axis label
    Returns:
        bar graph
    '''
    fig,ax = plt.subplots(figsize=(7,6))
    ax.bar(channel_names,pos_vals,width=0.4,align='edge') #plot the positive values
    ax.bar(channel_names,neg_vals,width=-0.4,align='edge') #plot the negative values
    ax.set_title(title_name)
    ax.set_xticklabels(channel_names,rotation=0)
    ax.set_ylabel(y_lbl)
    ax.set_xlabel(x_lbl)
    ax.legend(('positive','negative'),loc='best')
    fig
    
def trump_comments_plot():
    '''
    Manually take the pos trump sent and neg trump sent from the Wall video section
    of FOX, BBC, and CNN.txt inside ECE-143-Project---Group-11\sentiment_analysis\textblob_data\news
    '''
    fig,ax = plt.subplots(1,2,figsize = (6,10))
    plt.subplots_adjust(right=2.3)

    #organized from least to most subscribers
    names = ['FOX','BBC','CNN']

    #values taken from D:\ECE-143-Project---Group-11\sentiment_analysis\textblob_data\news
    positive_score = [27.185175414862904,20.325324675324683,39.84338798450779]
    negative_score = [13.885322833994708,8.012678571428571,21.13975319271372]

    #normalize the scores
    summed_score=[sum(x) for x in zip(positive_score,negative_score)]
    normalized_pos=[x[0]/x[1] for x in zip(positive_score,summed_score)]
    normalized_neg=[x[0]/x[1] for x in zip(negative_score,summed_score)]

    ax[0].barh(names,normalized_pos,height=0.2,align='edge')
    ax[0].barh(names,normalized_neg,height=-0.2,align='edge')
    ax[0].set_title('Pos/Neg Polarity of Trump Comments')
    ax[0].legend(('positive','negative'),loc='best')
    ax[0].set_xlabel('Percent')
    ax[0].set_ylabel('News Channel')

    #plot number of positive trump comments and negative trump comments
    pos_trump = [67,43,111]
    neg_trump = [152,107,249]

    ax[1].barh(names,pos_trump,height=0.2,align='edge')
    ax[1].barh(names,neg_trump,height=-0.2,align='edge')
    ax[1].set_title('# of Positive vs Negative Trump Comments')
    ax[1].legend(('# of positive comments','# of negative comments'),loc='best')
    ax[1].set_xlabel('Number of Comments')
    ax[1].set_ylabel('News Channel')
    fig
    
def norm_polarities(file):
    '''
    This function takes in a file which has the total positive and negative polarity of comments for each individual video topic.
    It sums up all the positive polarities and negative polarities to get a grand total polarity over all the video topics.
    It then normalizes the result.
    Args:
        file: (txt) .txt file containing the polarities of each video topic
    Returns:
        pos_norm: (float) sums up pos_sum and neg_sum and divides pos_sum by total
        neg_norm: (float) same as pos_norm except divides neg_sum by total
    '''
    assert isinstance(file,str)
    pos_sum = 0
    neg_sum = 0
    with open(file,'r') as f:
        a = f.readlines()
        for i in range(len(a)): #loop through each video topic
            data = a[i].split(' ')
            pos_sum += float(data[-2]) #sum up the positive polarities
            neg_sum += abs(float(data[-1])) #sum up the negative polarities
        #get the normalized pos/neg value
        total = pos_sum + neg_sum
        pos_norm = pos_sum/total
        neg_norm = neg_sum/total
        
    return pos_norm,neg_norm

def get_sentiment_trump(file):
    '''
    This function returns the positive, negative, and neutral strings containing 'trump' from file.
    The strings are determined as positive or negative by passing it through textblob
    Args:
        file: (str) file containing all the comments for one video topic of one channel
    Returns:
        pos_str: (str) one big string that combines all the comments that were deemed positive by textblob
        neg_str: (str) one big string that combines all the comments that were deemed negative by textblob
        neutral_str: (str) one big string that combines all the comments that were given a polarity of 0 by texblob
    '''
    assert isinstance(file,str)
    from textblob import TextBlob
    pos_str = ''
    neg_str = ''
    neutral_str = ''
    with open(file,'r',encoding='utf8') as f:
        for text in f:
            blob = TextBlob(text)
            for sentence in blob.sentences:
                sent = sentence.sentiment.polarity
                a = sentence.lower()
                if sent > 0:
                    if 'trump' in a:
                        pos_str = pos_str + ' ' + str(a)
                elif sent == 0:
                    if 'trump' in a:
                        neutral_str = neutral_str + ' ' + str(a)
                else:
                    if 'trump' in a:
                        neg_str = neg_str + ' ' + str(a)
        return (pos_str,neg_str,neutral_str)
    
def get_sentiment(file):
    '''
    This function returns the positive, negative, and neutral strings from file.
    Unlike get_sentiment_trump, this function does not only look for sentences containing 'trump'
    The strings are determined as positive or negative by passing it through textblob
    Args:
        file: (str) file containing all the comments for one video topic of one channel
    Returns:
        pos_str: (str) one big string that combines all the comments that were deemed positive by textblob
        neg_str: (str) one big string that combines all the comments that were deemed negative by textblob
        neutral_str: (str) one big string that combines all the comments that were given a polarity of 0 by texblob
    '''
    assert isinstance(file,str)
    from textblob import TextBlob
    pos_str = ''
    neg_str = ''
    neutral_str = ''
    with open(file,'r',encoding='utf8') as f:
        for text in f:
            blob = TextBlob(text)
            for sentence in blob.sentences:
                sent = sentence.sentiment.polarity
                a = sentence.lower()
                if sent > 0:
                    pos_str = pos_str + ' ' + str(a)
                elif sent == 0:
                    neutral_str = neutral_str + ' ' + str(a)
                else:
                    neg_str = neg_str + ' ' + str(a)
        return (pos_str,neg_str,neutral_str)
    

def posneg_wordcloud(sent):
    from wordcloud import WordCloud,STOPWORDS
    import matplotlib.pyplot as plt
    '''
    This function takes in a sentence and creates a wordcloud from that sentence.
    Args:
        sent: (str) sentence you want to make a wordcloud of
    Returns:
        wordcloud of sent
    '''
    assert isinstance(sent,str)
    s = list(set(STOPWORDS)) + ['donald','president','go','will','mr','wall','people','say','know','want','trump','california']
    wc = WordCloud(width = 1400, height = 800,
                    background_color ='white',
                    stopwords=s,
                    collocations = False,
                    min_font_size = 10).generate(sent) 
    plt.imshow(wc)
    plt.axis('off')
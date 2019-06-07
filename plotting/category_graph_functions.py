#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:58:00 2019

@author: sethurishabh

Functions for plotting graphs for Demographic Analysis Section
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def get_cooking_data(path):
    """
    Get Dataframe containing sentiment values per user for cooking category.
    
    Inputs
    ------
    path : str
        Path to directory with cooking sentiments
    
    Returns
    -------
    cooking
        Dataframe with sentiment values
        
    """
    assert isinstance(path, str)
    fileName = path + 'cooking.txt'
    assert os.path.exists(fileName), 'File Doesn\'t exist'
    cooking = pd.read_csv(fileName, sep=", ",header=None, engine='python')
    cooking.columns = ['Creator','File','Positive','Negative','Gender','Country']
    c = list(cooking['File'])
    c = [i.split('.')[0] for i in c]
    cooking['Creator'] = c
    cooking.set_index('Creator', inplace=True)
    cooking.drop(columns=['File', 'Country'], inplace=True)
    cooking['Category'] = ['Cooking']*len(cooking)
    return cooking

def get_influencer_data(path):
    """
    Get Dataframe containing sentiment values per user for influencer category.
    
    Inputs
    ------
    path : str
        Path to directory with influencer sentiments
    
    Returns
    -------
    influencers
        Dataframe with sentiment values
        
    """
    assert isinstance(path, str)
    fileName = path + 'influencers.txt' 
    assert os.path.exists(fileName), 'File Doesn\'t exist'
    influencers = pd.read_csv(fileName, sep=" ",header=None)
    influencers.columns = ['Creator','Positive','Negative']
    c = list(influencers['Creator'])
    c = [i.split('.')[0] for i in c]
    influencers['Creator'] = c
    influencers.set_index('Creator', inplace=True)
    influencers['Gender'] = ['Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male','Male', 'Female', 'Female']
    influencers['Category'] = ['Influencers']*len(influencers)
    return influencers

def get_gaming_data(path):
    """
    Get Dataframe containing sentiment values per user for gaming category.
    
    Inputs
    ------
    path : str
        Path to directory with gaming sentiments
    
    Returns
    -------
    gaming
        Dataframe with sentiment values
        
    """
    assert isinstance(path, str)
    fileName = path + 'gaming.txt'
    assert os.path.exists(fileName), 'File Doesn\'t exist'
    gaming = pd.read_csv(fileName, sep=" ",header=None)
    gaming.columns = ['Creator','Positive','Negative']
    c = list(gaming['Creator'])
    c = [i.split('.')[0] for i in c]
    gaming['Creator'] = c
    gaming.set_index('Creator', inplace=True)
    gaming['Category'] = ['Gaming']*len(gaming)
    gaming['Gender'] = ['Male']*len(gaming)
    return gaming

def normalize_sentiment(df):
    """
    Adds columns that normalize positive and negative sentiment.
    
    Inputs
    ------
    df : DataFrame
        input data with positive and negative sentiments to be modified
        
    """
    assert isinstance(df, pd.DataFrame), 'df must be of type DataFrame'
    assert 'Negative' in df.columns, 'df must have column Negative'
    assert 'Positive' in df.columns, 'df must have column Positive'
    df['Negative'] = abs(df['Negative'])
    df['Normalized Positive'] = df['Positive']/(df['Positive']+df['Negative'])*100
    df['Normalized Negative'] = df['Negative']/(df['Positive']+df['Negative'])*100
    
def get_subscriber_counts(path, df):
    """
    Returns dataframe with subscribers and subscriber ranges.
    
    Inputs
    ------
    path : str
        Path to directory with subscriber counts
    df : DataFrame
        input data frame 
        
    Returns
    -------
    with_subs
        dataframe containing input data frame with subscriber information
    
    """
    assert isinstance(path, str)
    assert isinstance(df, pd.DataFrame), 'df must be of type DataFrame'
    fileName = path + 'subscriber_count.txt'
    assert os.path.exists(fileName), 'File Doesn\'t exist'
    subs = pd.read_csv(fileName, sep=" ",header=None)
    subs.columns = ['Creator', 'Subscribers', 'Category']
    subs.set_index('Creator', inplace=True)
    subs.drop(columns=['Category'], inplace=True)
    with_subs = pd.concat([df, subs], axis=1, sort=False)
    with_subs['Subscribers'] = with_subs['Subscribers']/1e6
    with_subs['Subscribers Range'] = pd.cut(with_subs['Subscribers'], [0, 1.5, 5, 15, float('inf')])
    return with_subs

def plot_vs_category(df):
    """
    Plots bar chart of negativity vs category.
    
    Inputs
    ------
    df : DataFrame
        input data frame
    
    """
    assert isinstance(df, pd.DataFrame), 'df must be of type DataFrame'
    d2 = df.groupby(by=['Category']).mean()
    ax = d2.plot.bar(y=['Normalized Negative'],width = 0.8,rot=0)
    ax.set_ylabel('% of Negative Comments')
    ax.legend(loc='upper left', bbox_to_anchor=(1,1));
    ax.get_legend().remove()
    ax.set_title('Negativity vs Category')

def plot_vs_gender(df):
    """
    Plots bar chart of negativity vs gender.
    
    Inputs
    ------
    df : DataFrame
        input data frame
    
    """
    assert isinstance(df, pd.DataFrame), 'df must be of type DataFrame'
    d2 = df.groupby(by=['Gender']).mean()
    ax = d2.plot.bar(y=['Normalized Negative'],width = 0.8,rot=0)
    ax.set_ylabel('% of Negative Comments')
    ax.legend(loc='upper left', bbox_to_anchor=(1,1));
    ax.get_legend().remove()
    ax.set_title('Negativity vs Gender')

def plot_vs_gender_by_category(df):
    """
    Plots bar chart of negativity vs gender split by category.
    
    Inputs
    ------
    df : DataFrame
        input data frame
    
    """
    assert isinstance(df, pd.DataFrame), 'df must be of type DataFrame'
    d2 = df.groupby(by=['Gender','Category']).mean()['Normalized Negative'].unstack().reset_index()
    d2.set_index('Gender', inplace=True)
    ax = d2.plot.bar(y=['Gaming', 'Cooking', 'Influencers'],width = 0.8,rot=0)
    ax.legend(loc='best')
    ax.set_ylabel('% of Negative Comments')
    ax.set_title('Negativity vs Gender per Category')
    
def plot_subs_vs_category(df):
    """
    Plots bar chart of subscribers vs category.
    
    Inputs
    ------
    df : DataFrame
        input data frame
    
    """
    assert isinstance(df, pd.DataFrame), 'df must be of type DataFrame'
    d2 = df.groupby(by=['Category']).mean()
    d2['Subscribers'] = d2['Subscribers']
    ax = d2.plot.bar(y=['Subscribers'],width = 0.8,rot=0)
    ax.set_ylabel('Subscribers (M)')
    ax.get_legend().remove()
    ax.set_title('Subscriber Count vs Category')
    
def plot_vs_subs(df):
    """
    Plots bar chart of negativity vs subscribers.
    
    Inputs
    ------
    df : DataFrame
        input data frame
    
    """
    assert isinstance(df, pd.DataFrame), 'df must be of type DataFrame'
    ind = np.arange(4)*3
    d2 = df.groupby(by=['Subscribers Range']).mean()
    neg = list(d2['Normalized Negative'])
    plt.bar(ind, neg, 2.4,label='')
    plt.ylabel('% of Negative Comments')
    plt.xlabel('Subscribers')
    plt.xticks(ind-1.5, ('0', '1.5M', '5M', '15M', 'inf'))
    plt.title('Negativity vs Subscribers')
    plt.show()

def plot_pie_chart(df, name):
    """
    Plots pie chart of positivity and negativity per category.
    
    Inputs
    ------
    df : DataFrame
        input data frame
    name : str
        title of the graph
    
    """
    assert isinstance(df, pd.DataFrame), 'df must be of type DataFrame'
    assert isinstance(name, str)
    d2 = df.groupby(by='Category').mean()
    labels = 'Positive', 'Negative'
    sizes = [d2['Normalized Positive'], d2['Normalized Negative']]
    colors = ['lightskyblue', 'lightcoral']
    plt.pie(sizes,labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=False, startangle=90)
    plt.title(name)
    plt.axis('equal')
    plt.show()
    
def plot_vs_subs_by_category(df, trends=[]):
    """
    Plots bar chart of negativity vs subscribers split by category.
    
    Inputs
    ------
    df : DataFrame
        input data frame
    trends : list
        list of trendlines to be shown
        
    """
    assert isinstance(df, pd.DataFrame), 'df must be of type DataFrame'
    assert isinstance(trends, list), 'trends must be a list'
    d2 = df.groupby(by=['Subscribers Range','Category']).mean()['Normalized Negative'].unstack().reset_index()
    c = list(d2['Cooking'])
    g = list(d2['Gaming'])
    i = list(d2['Influencers'])
    ind = np.arange(4)*3
    plt.bar(ind, c, 0.8,label='Cooking')
    plt.bar(ind + 0.8, g, 0.8, label='Gaming')
    plt.bar(ind + 1.6, i, 0.8, label='Influencers')
    if 'c' in trends:
        plt.plot(ind, c, marker='o',color='#0000ff')
    if 'i' in trends:
        plt.plot(ind + 1.6, i, marker='o',color='#00ff00')
    if 'g' in trends:
        plt.plot(ind + 0.8, g, marker='o',color='#ff0000')
    plt.ylabel('% of Negative Comments')
    plt.xlabel('Subscribers')
    plt.legend()
    plt.xticks(ind-0.7, ('0', '1.5M', '5M', '15M', 'inf'))
    plt.title('Negativity vs Subscribers per Category')
    plt.show()
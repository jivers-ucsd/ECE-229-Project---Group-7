#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:58:00 2019

@author: sethurishabh
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_cooking_data(path):
    fileName = path + 'cooking.txt'
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
    fileName = path + 'influencers.txt'    
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
    fileName = path + 'gaming.txt'    
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
    df['Negative'] = abs(df['Negative'])
    df['Normalized Positive'] = df['Positive']/(df['Positive']+df['Negative'])*100
    df['Normalized Negative'] = df['Negative']/(df['Positive']+df['Negative'])*100
    
def get_subscriber_counts(path, df):
    fileName = path + 'subscriber_count.txt'
    subs = pd.read_csv(fileName, sep=" ",header=None)
    subs.columns = ['Creator', 'Subscribers', 'Category']
    subs.set_index('Creator', inplace=True)
    subs.drop(columns=['Category'], inplace=True)
    with_subs = pd.concat([df, subs], axis=1, sort=False)
    with_subs['Subscribers'] = with_subs['Subscribers']/1e6
    with_subs['Subscribers Range'] = pd.cut(with_subs['Subscribers'], [0, 1.5, 5, 15, float('inf')])
    return with_subs

def plot_vs_category(df):
    d2 = df.groupby(by=['Category']).mean()
    ax = d2.plot.bar(y=['Normalized Negative'],width = 0.8,rot=0)
    ax.set_ylabel('% of Negative Comments')
    ax.legend(loc='upper left', bbox_to_anchor=(1,1));
    ax.get_legend().remove()
    ax.set_title('Negativity vs Category')

def plot_vs_gender(df):
    d2 = df.groupby(by=['Gender']).mean()
    ax = d2.plot.bar(y=['Normalized Negative'],width = 0.8,rot=0)
    ax.set_ylabel('% of Negative Comments')
    ax.legend(loc='upper left', bbox_to_anchor=(1,1));
    ax.get_legend().remove()
    ax.set_title('Negativity vs Gender')

def plot_vs_gender_by_category(df):
    d2 = df.groupby(by=['Gender','Category']).mean()['Normalized Negative'].unstack().reset_index()
    d2.set_index('Gender', inplace=True)
    ax = d2.plot.bar(y=['Gaming', 'Cooking', 'Influencers'],width = 0.8,rot=0)
    ax.legend(loc='best')
    ax.set_ylabel('% of Negative Comments')
    ax.set_title('Negativity vs Gender per Category')
    
def plot_subs_vs_category(df):
    d2 = df.groupby(by=['Category']).mean()
    d2['Subscribers'] = d2['Subscribers']
    ax = d2.plot.bar(y=['Subscribers'],width = 0.8,rot=0)
    ax.set_ylabel('Subscribers (M)')
    ax.get_legend().remove()
    ax.set_title('Subscriber Count vs Category')
    
def plot_vs_subs(df):
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
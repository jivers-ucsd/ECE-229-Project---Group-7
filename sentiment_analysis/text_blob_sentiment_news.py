#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:43:58 2019

@author: sethurishabh
"""

DATA_DIR = '../data/news/'
OUT_DIR = './textblob_data/news/'

from textblob import TextBlob
import sys
import os

def get_sentiment(s):
    pos_sent = 0
    neg_sent = 0
    pos = {'trump':0, 'trump_sent':0, 'democrat':0, 'republican':0}
    neg = {'trump':0, 'trump_sent':0, 'democrat':0, 'republican':0}
    
    for text in s:
        blob = TextBlob(text)
        for sentence in blob.sentences:
            sent = sentence.sentiment.polarity
            a = sentence.lower().words
            if sent > 0:
                pos_sent += sent
                if 'trump' in a:
                    pos['trump'] += 1
                    pos['trump_sent'] += sent
                if 'democrat' in a:
                    pos['democrat'] += 1
                if 'republican' in a:
                    pos['republican'] += 1
            else:
                neg_sent += sent
                if 'trump' in a:
                    neg['trump'] += 1
                    neg['trump_sent'] += sent
                if 'democrat' in a:
                    neg['democrat'] += 1
                if 'republican' in a:
                    neg['republican'] += 1
    return pos_sent, neg_sent, pos, neg

if __name__ == "__main__":
    for i in range(1, len(sys.argv)):
        folder = sys.argv[i] + '/'
        path = DATA_DIR + folder
        
        if not os.path.exists(OUT_DIR):
            os.makedirs(OUT_DIR)
        filelist = os.listdir(path)
        outfd = open(OUT_DIR+sys.argv[i]+'.txt', 'w+')
        try :
            print('Removing .DS_Store')
            filelist.remove('.DS_Store')
        except ValueError:
            print('No .DS_Store...\nContinuing...')
        else :
            print('.DS_Store removed...\nContinuing...')
        print("In folder :", folder)
        print(filelist)
        for file in filelist:
            print("In file :", file)
            fd = open(DATA_DIR + folder + file)
            s = fd.readlines()
            fd.close()
            pos_sent, neg_sent, pos, neg = get_sentiment(s)
            outfd.write(file+' '+str(pos_sent)+' '+str(neg_sent)+'\npos:'+str(pos)+'\nneg:'+str(neg)+'\n\n')
        outfd.close()
    print("Exiting...")
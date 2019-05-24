#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:43:58 2019

@author: sethurishabh
"""

DATA_DIR = '../data/'
OUT_DIR = './textblob_data/'

from textblob import TextBlob
import sys
import os

def get_sentiment(s):
    pos_sent = 0
    neg_sent = 0
    for text in s:
        blob = TextBlob(text)
        for sentence in blob.sentences:
            sent = sentence.sentiment.polarity
            if sent > 0:
                pos_sent += sent
            else:
                neg_sent += sent
    return pos_sent, neg_sent

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
            pos_sent, neg_sent = get_sentiment(s)
            outfd.write(file+' '+str(pos_sent)+' '+str(neg_sent)+'\n')
        outfd.close()
    print("Exiting...")
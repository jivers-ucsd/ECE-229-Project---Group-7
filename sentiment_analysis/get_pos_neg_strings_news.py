#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:43:58 2019

@author: sethurishabh
"""

DATA_DIR = '../data/news/'
OUT_DIR = './textblob_data/news/'

import sys
import os

def get_sentiment(file):
    from textblob import TextBlob
    pos_str = ''
    neg_str = ''
    with open(file,'r',encoding='utf8') as f:
        for text in f:
            blob = TextBlob(text)
            for sentence in blob.sentences:
                sent = sentence.sentiment.polarity
                a = sentence.lower()
                if sent > 0:
                    if 'trump' in a:
                        pos_str = pos_str + ' ' + str(a)
                else:
                    if 'trump' in a:
                        neg_str = neg_str + ' ' + str(a)
        return (pos_str,neg_str)


#def get_sentiment(s):
#    pos_sent = 0
#    neg_sent = 0
#    pos_str = ''
#    neg_str = ''
#    
#    for text in s:
#        blob = TextBlob(text)
#        for sentence in blob.sentences:
#            sent = sentence.sentiment.polarity
#            a = sentence.lower().words
#            if sent > 0:
#                pos_sent += sent
#                if 'trump' in a:
#                    pos_str = pos_str + ' ' + str(a)
#            else:
#                neg_sent += sent
#                if 'trump' in a:
#                    neg_str = neg_str + ' ' + str(a)
#    return pos_sent, neg_sent, pos_str, neg_str

#if __name__ == "__main__":
#    for i in range(1, len(sys.argv)):
#        folder = sys.argv[i] + '/'
#        path = DATA_DIR + folder
#        
#        if not os.path.exists(OUT_DIR):
#            os.makedirs(OUT_DIR)
#        filelist = os.listdir(path)
#        outfd = open(OUT_DIR+sys.argv[i]+'.txt', 'w+')
#        try :
#            print('Removing .DS_Store')
#            filelist.remove('.DS_Store')
#        except ValueError:
#            print('No .DS_Store...\nContinuing...')
#        else :
#            print('.DS_Store removed...\nContinuing...')
#        print("In folder :", folder)
#        print(filelist)
#        for file in filelist:
#            print("In file :", file)
#            fd = open(DATA_DIR + folder + file,'r',encoding='utf8')
#            s = fd.readlines()
#            fd.close()
#            pos_sent, neg_sent, pos, neg = get_sentiment(s)
#            outfd.write(file+' '+str(pos_sent)+' '+str(neg_sent)+'\npos:'+str(pos)+'\nneg:'+str(neg)+'\n\n')
#        outfd.close()
#    print("Exiting...")
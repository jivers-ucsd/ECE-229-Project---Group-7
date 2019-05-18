# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:59:01 2019

@author: Jessica
"""
'''
Description
    Takes a list of youtube content creators from a file and writes a file 
    listing links to videos from that content creators channel.
    
Inputs
    fname(str)
        String file name to file containing list of content creators
        
Outputs
    Writes a file of links to videos
    
'''
##imports
from bs4 import BeautifulSoup as bs
import requests
import sys
import os

SRC_DIR = '../source_links/'

##body
def get_links(user, t):
    
    if t == 'u':
        content = 'https://www.youtube.com/user/'+user+'/videos'
    elif t == 'p':
        content = 'https://www.youtube.com/playlist?list='+user
    elif t == 'c':
        content = 'https://www.youtube.com/channel/'+user+'/videos'
    
    r = requests.get(content)
    
    soup = bs(r.text,'html.parser')
    
    vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
    
    videolist = []
    for v in vids:
        tmp = 'https://www.youtube.com' + v['href']
        videolist.append(tmp)

    return videolist

if __name__ == '__main__':
    d = sys.argv[1]
    user = sys.argv[2]
    t = sys.argv[3]
    links = get_links(user, t)
    if not os.path.exists(SRC_DIR + d):
        os.makedirs(SRC_DIR + d)
    fd = open(SRC_DIR+d+'/'+user+'.txt', 'w+')
    fd.write('\n'.join(links))
    fd.close()
    print("Number of links :", len(links))
    
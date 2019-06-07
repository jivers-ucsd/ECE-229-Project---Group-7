# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:59:01 2019

@author: Jessica

Gets video links in from users.
Used as:
    python get_video_links.py <name> <type>
"""
##imports
from bs4 import BeautifulSoup as bs
import requests
import sys
import os

SRC_DIR = '../source_links/'

##body
def get_links(user, t):
    """
    Gets video links user.

    Parameters
    ----------
    user : str
        creator's username
    t : char
        type of content creator i.e., user, playlist, channel

    Output
    -------
    Writes video links into file in source_links folder

    """
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
    """
    Gets video links for user, type when called on terminal.
    """
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
    
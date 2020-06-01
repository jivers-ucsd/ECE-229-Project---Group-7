# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:59:01 2019

@author: Jessica

Gets video links in from users.
Used as:
    python get_video_links.py <name> <type>
"""
##imports
from selenium import webdriver
from bs4 import BeautifulSoup as bs
#import os
import time
#import sys

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
    driver=webdriver.Firefox()
    
    if t == 'u':
        content = 'https://www.youtube.com/user/'+user+'/videos'
        classAttr = 'yt-simple-endpoint style-scope ytd-grid-video-renderer'
        scrollCount = 5
    elif t == 'p':
        content = 'https://www.youtube.com/playlist?list='+user
        classAttr = 'yt-simple-endpoint style-scope ytd-playlist-video-renderer'
        scrollCount = 10
    elif t == 'c':
        content = 'https://www.youtube.com/channel/'+user+'/videos'
        classAttr = 'yt-simple-endpoint style-scope ytd-grid-video-renderer'
        scrollCount = 5
    
    print("Getting links :", user)
    driver.get(content)
    driver.maximize_window()
    time.sleep(7)

    driver.execute_script('window.scrollTo(0, 500);')
    SCROLL_PAUSE_TIME = 5


    # Get scroll height
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    for count in range(scrollCount):
        #now wait let load the comments
        time.sleep(SCROLL_PAUSE_TIME)
        driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if last_height == new_height:
            break
        last_height = new_height    
   
    r = driver.page_source
    soup = bs(r,'html.parser')
    vids = soup.findAll('a',attrs={'class':classAttr})
        
    videolist = []
    for v in vids:
        tmp = 'https://www.youtube.com' + v['href']
        videolist.append(tmp)

    driver.close()
    return videolist
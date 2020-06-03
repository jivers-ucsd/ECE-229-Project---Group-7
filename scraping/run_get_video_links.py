# -*- coding: utf-8 -*-
"""
Gets video links for user, type when called on terminal.
"""  
##imports
from scraping.get_video_links import get_links
from selenium import webdriver
from bs4 import BeautifulSoup as bs
#import os
import time
#import sys

#constants
SRC_DIR = './data/source_links/'

#execute
fd = open('scraping/users.txt','r')
r = fd.read().splitlines()
fd.close()

for item in r:
    user = item.split()[0]
    t = item.split()[1]
    g = item.split()[2]

    links = get_links(user, t)
    fd = open(SRC_DIR+g+'/'+user+'.txt', 'w+')
    fd.write('\n'.join(links))
    fd.close()
    print("Number of links :", len(links))
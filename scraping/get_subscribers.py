#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:04:27 2019

@author: sethurishabh
"""

##imports
from bs4 import BeautifulSoup as bs
import requests
import re

SRC_DIR = '../source_links/'

##body
def get_subs(user, t):
    
    if t == 'u':
        content = 'https://www.youtube.com/user/'+user+'/videos'
    elif t == 'p':
        print("Can't handle playlists.. Skipping..")
        return
    elif t == 'c':
        content = 'https://www.youtube.com/channel/'+user+'/videos'
    
    r = requests.get(content)
    
    soup = bs(r.text,'html.parser')
    s = str(soup)
    pattern = '[0-9,]+ subscribers'
    m = re.search(pattern, s)
    n = m[0].split()[0]
    n = int(''.join(n.split(',')))
    del s
    return n    

if __name__ == '__main__':
    read_fd = open('users.txt')
    userlist = read_fd.readlines()
    read_fd.close()
    fd = open('subscriber_count.txt', 'w+')
    for line in userlist:
        user, t, category = line.split()
        print("On User :", user)
        n = get_subs(user, t)
        fd.write(str(user)+" "+str(n)+" "+str(category)+"\n")
    fd.close()
    print("Exiting...")

    
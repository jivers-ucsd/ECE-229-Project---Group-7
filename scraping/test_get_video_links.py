# -*- coding: utf-8 -*-
"""
Pytest test for get_video_links.py
"""

from scraping.get_video_links import get_links

#constants
SRC_DIR = './data/source_links/'


def test_get_video_links():
    
    #execute
    fd = open('scraping/test_users.txt','r')
    r = fd.read().splitlines()
    fd.close()
    
    user = r[0].split()[0]
    t = r[0].split()[1]

    links = get_links(user, t)
    
    assert(links == ['https://www.youtube.com/watch?v=2tDmuNu_1FQ'])
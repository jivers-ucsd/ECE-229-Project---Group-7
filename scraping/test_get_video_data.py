# -*- coding: utf-8 -*-
"""
Pytest test for get_video_links.py
"""

from scraping.get_video_data import get_vid_data
import os

SRC_DIR = './data/source_links/'

def test_get_video_data():
            
    folder_list = ['test']
    
    folder = folder_list[0]
        
    print("On Folder :", folder)
    file_list = os.listdir(os.path.join(SRC_DIR,folder))
    file = file_list[0]

    d = get_vid_data(folder,file)

    assert(list(d.columns) == ['title','date','likes','dislikes','views','description'])
    assert(all(d.title == 'Group 48 Video Presentation'))
    assert(all(d.date == 'Mar 19, 2020'))
    assert(all(d.description == 'Group 48 video presentation for UCSD ECE271B Winter2020.'))
            
      
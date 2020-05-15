#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:04:27 2019

@author: sethurishabh

Script to get subscriber of all users in users.txt.
"""

##imports
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import os
import time
import pdb
import traceback
import sys

SRC_DIR = '../source_links/'

##body
def get_vid_data(folder, file):
    """
    For each video in a list in a file, scrape the video name, description, 
    number of likes, number of dislikes, date posted, and number of view.

    Parameters
    ----------
    folder : str
        folder where files are stored with video link information, i.e - 'cooking'
    file : str
        file name of file holding the video links

    Returns
    -------
    df : pandas DataFrame
        data frame of scraped data for all videos

    """
    assert isinstance(folder, str)
    assert isinstance(file, str)
    p = os.path.join(SRC_DIR,folder,file)
    #assert os.path.exists(p)
    
    fd = open(p)
    links = fd.read().splitlines()
    fd.close()
    
    df = pd.DataFrame()
    titles = list()
    views = list()
    dates = list()
    descriptions = list()
    likes = list()
    dislikes = list()    
    
    c = 1   
    for link in links:
        print('Link %(l)d of %(Llen)d.' %
                  {'l': c, 'Llen': len(links)})
        
        for attempt in range(10):
            try:
                r = requests.get(link)
                if r.status_code == 404:
                    print('Channel/User information Unavailable')
                    continue
                soup = bs(r.text,'html.parser')
        
                t = soup.find("meta",property={'og:title'})["content"]
                v = soup.find('span', class_='stat view-count').text
                v = int(v[0:-6].replace(',',''))
                date_info = soup.find('strong', 'watch-time-text').get_text()
                date = date_info.replace('Published on ','')
                date = date.replace('Premiered ','')
                date = date.replace('Streamed live on ','')
                like = soup.find("span", class_="like-button-renderer").span.button.text
                if like == '':
                    like = 0
                else:
                    like = int(like.replace(',',''))
                dis = soup.find("button",attrs={"title": "I dislike this"}).get_text()
                if dis == '':
                    dis = 0
                else:
                    dis = int(dis.replace(',',''))
                desc = soup.find("p", {"id": "eow-description"}).text
                
            except:
                continue
            else:
                titles.append(t)
                views.append(v)
                dates.append(date)
                likes.append(like)
                dislikes.append(dis)
                descriptions.append(desc)
                break
        else:
            print('Failed 10 times')
            
        #time.sleep(0.5) #slow program to let links load
        c = c+1
        
    df['title'] = titles
    df['date'] = dates
    df['likes'] = likes
    df['dislikes'] = dislikes
    df['views'] = views
    df['description'] = descriptions
    
    return df 

if __name__ == '__main__':
    """
    Automatically gets video data for all lists in SRC_DIR
    """
    try:
        folder_list = os.listdir(SRC_DIR)
        folder_list.remove('test')
        
        
        
        for folder in folder_list:
            df = pd.DataFrame()
            
            print("On Folder :", folder)
            fd = open(folder+'_dataFrame.txt', 'w+')
            file_list = os.listdir(os.path.join(SRC_DIR,folder))
            f = 1
            for file in file_list:
                print('On File %(f)d of %(flen)d.' %
                      {'f': f, 'flen': len(file_list)})
                d = get_vid_data(folder,file)
                df = df.append(d,ignore_index=True)
                f = f+1
                
            df.to_csv(folder+'_dataFrame.txt',index=False)
            #read with 
            #df = pd.read_csv(folder+'_dataFrame.txt')
        
        print("Exiting...")
    except:
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        pdb.post_mortem(tb)
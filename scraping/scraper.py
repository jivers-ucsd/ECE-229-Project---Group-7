#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 23:35:22 2019

@author: sethurishabh

Scrapes comments from links in directories given.
Used as:
    python scraper.py <name of folders>
"""

from selenium import webdriver
import os
import time
import sys

SRC_DIR = '../source_links/'
DATA_DIR = '../data/'

def scrape(folder, file):
    """
    Scrapes comments from all links in the folder/file path.

    Parameters
    ----------
    folder : str
        folder of file with links
    file : str
        file containing links

    Output
    -------
    Writes comments into file of given filename in data folder

    """
    assert isinstance(folder, str)
    assert isinstance(file, str)
    p = SRC_DIR + folder + file
    assert os.path.exists(p)
    driver=webdriver.Chrome()

    fd = open(p)
    links = fd.read().splitlines()
    fd.close()
    
    if not os.path.exists(DATA_DIR + folder):
        os.makedirs(DATA_DIR + folder)
    fd = open(DATA_DIR + folder + file, "w+")

    c = 0
    for link in links:
        if c >= 20 :
            break
        c += 1
        print("Getting link :", link)
        driver.get(link)
        driver.maximize_window()
        time.sleep(7)

        count = 0

        driver.execute_script('window.scrollTo(0, 500);')
        SCROLL_PAUSE_TIME = 5


        # Get scroll height
        last_height = driver.execute_script("return document.documentElement.scrollHeight")

        while count < 200:
            #now wait let load the comments
            time.sleep(SCROLL_PAUSE_TIME)
            driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
            count+=1
            new_height = driver.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height    

        count = 0
        print('Outputted to :', path+file)
        comment_div=driver.find_element_by_xpath('//*[@id="contents"]')
        comments=comment_div.find_elements_by_xpath('//*[@id="content-text"]')
        for comment in comments:
            fd.write(comment.text + "\n")
            count += 1
        time.sleep(5)
        print('Comments scraped :', count)
    fd.close()


if __name__ == '__main__':
    """
    Automatically gets all comments from link in directories given in source_links/
    """
    for i in range(1, len(sys.argv)):
        folder = sys.argv[i] + '/'
        path = SRC_DIR + folder
        filelist = os.listdir(path)
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
            scrape(folder, file)
    print("Exiting...")


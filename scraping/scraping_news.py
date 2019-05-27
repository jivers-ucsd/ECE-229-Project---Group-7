#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 23:35:22 2019

@author: sethurishabh
"""

from selenium import webdriver
import os
import time
import sys

SRC_DIR = '../source_links/'
DATA_DIR = '../data/'

def scrape(folder, file):
    driver=webdriver.Chrome()

    fd = open(SRC_DIR + folder + file)
    data = fd.read().splitlines()
    fd.close()
    
    c = 0
    for d in data:
        if c >= 20 :
            break
        c += 1
        
        fname, link = d.split(' - ')
        
        if not os.path.exists(DATA_DIR + folder + file + '/'):
            os.makedirs(DATA_DIR + folder + file + '/')
        fd = open(DATA_DIR + folder + file + '/' + fname, "w+")

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


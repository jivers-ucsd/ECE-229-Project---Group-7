#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:02:49 2019

@author: sethurishabh
"""

import sys
import os

blob = ''
DATA_DIR = '../data/'
for i in range(1, len(sys.argv)):
    folder = sys.argv[i] + '/'
    path = DATA_DIR + folder
    
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
        fd = open(DATA_DIR + folder + file)
        s = fd.read()
        blob += s
        fd.close()

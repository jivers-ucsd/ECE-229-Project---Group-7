# -*- coding: utf-8 -*-
"""
Automatically gets video data for all lists in SRC_DIR
"""

##imports
from scraping.get_video_data import get_vid_data
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import os
#import time
import pdb
import traceback
import sys

#execute
try:
    folder_list = os.listdir(SRC_DIR)
    folder_list.remove('test')
    
    
    
    for folder in folder_list:
        df = pd.DataFrame()
        
        print("On Folder :", folder)
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
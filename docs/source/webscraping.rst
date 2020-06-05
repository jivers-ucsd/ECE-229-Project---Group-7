Webscraping
============


Below are function definitions used to perform the webscraping from youtube and the respective test functions   



.. py:function:: get_vid_data(folder,file):

   
   For each video in a list in a file, scrape the video name, description, number of likes, number of dislikes, date posted, and number of view.

   
   :param str folder: folder where files are stored with video link information, i.e - 'cooking'
   :param str file: file name of file holding the video links
   :return: data frame of scraped data for all videos
   :rtype: df : pandas DataFrame
   :raises TypeError: if folder or file is not a basestring


Below is an example code of how to run get_vid_data
   

.. code-block:: python
   
   """
   The following code automatically gets video data for all lists in SRC_DIR using get_vid_data
   """
	
   #imports
   from scraping.get_video_data import get_vid_data
   from bs4 import BeautifulSoup as bs
   import requests
   import pandas as pd
   import os
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
    
        print("Exiting...")
    except:
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        pdb.post_mortem(tb) 



.. py:function:: get_links(user, t):

   Gets video links user

   :param str user: creator's username i.e. - 'bgfilms'
   :param char t: type of content creator i.e. 'u' - user, 'p' - playlist, 'c' - channel
   :return: list of links to videos
   :rtype: videolist : list   
   :raises TypeError: if user or t is not a basestring 
   :raises TypeError: if length of t is not equal to 1
   :raises assertionError: if t is not equal to 'u', 'p', 'c'

Below is an example code of how to use get_links
  
.. code-block:: python
   
   """
   The following code gets video links for user, type when called on terminal
   """
   from scraping.get_videeo_links import get_links
   from selenium import webdriver
   from bs4 import BeautifulSoup as bs
   import time

   
   SRC_DIR = './data/source_links/'
   
   fd = open('scraping/users.txt','r')
   r = fd.read().splitlines()
   fd.close()

   for item in r:

      user = item.split()[0]
      t = item.split()[1]
      g = item.split()[2]

      links = get_links(user, t)
      fd = open(SRC_DIR+g+'/'+user+'.txt','w+')
      fd.write('\n'.join(links))
      fd.close()
      print("Number of links :", len(links))


   
.. py:function:: test_get_video_data():
   
   Pytest test for get_vid_data function

   :raises assertionError: if d.columns do not all contain 'title','date','likes','dislikes','views','description'
   :raises assertionError: if d.title is not equal to 'Group 48 Video Presentation'
   :raises assertionError: if d.date is not equal to 'Mar 19,2020'
   :raises assertionError: if d.description is not equal to 'Group 48 video presentation for UCSD ECE271B Winter2020.'

.. py:function:: test_get_video_links():

   Pytest test for get_links function

   :raises assertionError: if links does not equal 'https://www.youtube.com/watch?v=2tDmuNu_1FQ'


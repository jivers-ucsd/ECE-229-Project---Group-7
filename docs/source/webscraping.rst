Webscraping Functions
=====================


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

   Gets all the video links for a specific user

   :param str user: creator's username i.e. - 'bgfilms'
   :param char t: type of content creator i.e. 'u' - user, 'p' - playlist, 'c' - channel
   :return: list of links to videos
   :rtype: videolist : list   
   :raises TypeError: if user or t is not a basestring 
   :raises TypeError: if length of t is not equal to 1
   :raises assertionError: if t is not equal to 'u', 'p', 'c'

Below is an example code of how to use get_links
  
.. code-block:: python

   >>>video_list = get_links('chefsteps', 'u')
   >>>video_list = ['https://www.youtube.com/watch?v=G8FplJ1BJyA', 'https://www.youtube.com/watch?v=LVXWSIjhAOc', 'https://www.youtube.com/watch?v=iNSc2sixyWQ', 'https://www.youtube.com/watch?v=RFA_RptDR4w', 'https://www.youtube.com/watch?v=giA5iA_6qGM', 'https://www.youtube.com/watch?v=NDm7Fo71kow', 'https://www.youtube.com/watch?v=Phtn7C62G0E', 'https://www.youtube.com/watch?v=xkoU3fzXnFg', 'https://www.youtube.com/watch?v=tUCtMYmKjfY', 'https://www.youtube.com/watch?v=KfQqEV6erqM', 'https://www.youtube.com/watch?v=7BMb4FMtvec', 'https://www.youtube.com/watch?v=mCkeZb6tN-c', 'https://www.youtube.com/watch?v=qkwPd8cyXSI', 'https://www.youtube.com/watch?v=jonmvu9yicE', 'https://www.youtube.com/watch?v=NWBdRRW4oCE', 'https://www.youtube.com/watch?v=KPoxKFmNs5E', 'https://www.youtube.com/watch?v=smyFpZQz-50', 'https://www.youtube.com/watch?v=nRHaZoI-Bhc', 'https://www.youtube.com/watch?v=VB_fsszLDvY', 'https://www.youtube.com/watch?v=nk6tzT-m8gQ', 'https://www.youtube.com/watch?v=Tf_eSMpNgh8', 'https://www.youtube.com/watch?v=21xmT4Jc3yM', 'https://www.youtube.com/watch?v=OLMWqoQP2pI', 'https://www.youtube.com/watch?v=4qKASRi7iJs', 'https://www.youtube.com/watch?v=owgPVAHdRpg', 'https://www.youtube.com/watch?v=liRwZsw3cq4', 'https://www.youtube.com/watch?v=eBF5DwJPH00', 'https://www.youtube.com/watch?v=-XGyf5bpOdg', 'https://www.youtube.com/watch?v=P1Ncswxv4QU']




   
.. py:function:: test_get_video_data():
   
   Pytest test for get_vid_data function

   :raises assertionError: if d.columns do not all contain 'title','date','likes','dislikes','views','description'
   :raises assertionError: if d.title is not equal to 'Group 48 Video Presentation'
   :raises assertionError: if d.date is not equal to 'Mar 19,2020'
   :raises assertionError: if d.description is not equal to 'Group 48 video presentation for UCSD ECE271B Winter2020.'

.. py:function:: test_get_video_links():

   Pytest test for get_links function

   :raises assertionError: if links does not equal 'https://www.youtube.com/watch?v=2tDmuNu_1FQ'


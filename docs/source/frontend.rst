Front End
=========

Function for front-end part I is given as below.

.. py:function:: wordscloud(x,Genre):
  
   This function is to plot word cloud over all time.

   :param Timestamp x: Input timestamp from the slider which indicates the time of the word cloud
   :param str Genre: scalar depicting the genre of the content: "cooking", "gaming", "influencers"
   :return: none, but a word cloud should be shown in the graph
   :rtype: none
   :raises TypeError: none

Below is an example showing how to use the function.


.. code-block:: python

    import os
    from random import shuffle
    from front_end.wordscloud import wordscloud
    
    year_end=2019
    year_start=2015
    Genre=['cooking', 'influencers', 'gaming']
    time_idx=pd.date_range(start=str(year_start)+'0101',end=str(year_end)+'1231',freq='M')
    fmt='%Y-%m'
    options = [(item.strftime(fmt),item) for item in time_idx]
    shuffle(options)
    optionstest=[i[0] for i in options]
    for j in range(2):
        testx=optionstest[j]
        for i in Genre:
            wordscloud(testx,i)
            
Function for front-end part II is given as below.


.. py:function:: P_N_cloud(x,Genre):

   
   This function is to plot word cloud for both positive and negative over all time.

   
   :param Timestamp x: Input timestamp from the slider which indicates the time of the word cloud
   :param str Genre: scalar depicting the genre of the content: "cooking", "gaming", "influencers"
   :return: none, but a word cloud should be shown in the graph
   :rtype: none
   :raises TypeError: none

Below is an example showing how to use the function.

.. code-block:: python

    import numpy as np
    from random import shuffle
    import pandas as pd
    import os
    from front_end.P_N_cloud import P_N_cloud
    
    
    
    year_end=2019
    year_start=2015
    Genre=['cooking', 'influencers', 'gaming']
    time_idx=pd.date_range(start=str(year_start)+'0101',end=str(year_end)+'1231',freq='M')
    fmt='%Y-%m'
    options = [(item.strftime(fmt),item) for item in time_idx]
    shuffle(options)
    optionstest=[i[0] for i in options]
    for j in range(2):
        testx=optionstest[j]
        for i in Genre:
            P_N_cloud(testx,i)

Below are function definitions used to perform the front end part three
Function analyze_text_color

.. py:function:: analyze_text_color(text, genre, metric):

   
   Analyze the given text and produce color labels for the words 

   
   :param str text: scalar depicting the text that needs to be analyzed
   :param str genre: scalar depicting the genre of the content: "cooking", "gaming", "influencers"
   :param str metric: scalar depicting the metric to base the analysis on: "likes_mean", "likes_median", "dislikes_mean", "dislikes_median", "views_mean", "views_median", "polarity", "subjectivity"
   :return: a list with the same number of elements as number of words in given text, with each corresponding element being the color for that word: "red" means bad, "yellow" means okay, "green" means good and "white" means "Not found" (in database)
   :rtype: list
   :raises TypeError: none
   
Function color_changer

.. py:function:: color_changer(x,Genre,Metric)
   
   change the color of input text instantly
   
   :param str x: scalar depicting the text that needs to be analyzed
   :param str genre: scalar depicting the genre of the content: "cooking", "gaming", "influencers"
   :param str metric: scalar depicting the metric to base the analysis on: "likes_mean", "likes_median", "dislikes_mean", "dislikes_median", "views_mean", "views_median", "polarity", "subjectivity"
   :return: none
   
Below is an example showing how to use the function.

.. code-block:: python

    from front_end.function_partIII import analyze_text_color,color_changer
    assert analyze_text_color('today we will cook delicious beef', 'cooking', 'subjectivity')==['yellow', 'white', 'yellow', 'yellow', 'green', 'yellow']
    assert analyze_text_color('amazing social skills', 'influencers', 'likes_mean')==['yellow', 'yellow', 'yellow']
    assert analyze_text_color('funny lives in splatoon', 'gaming', 'likes_mean')==['yellow', 'yellow', 'yellow', 'white']

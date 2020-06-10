Front End 
===================

Below are the functions and test functions used to make the front end part of the website


.. py:function:: analyze_text_color(text,genre,metric)


   Analyze the given text that needs to be analyzed


   :param str text: scalar depicting the text that needs to be analyzed
   :param str genre: scalar depicting the genre of the content: "cooking", "gaming", "influencers"
   :param str metric: scalar depicting the metric to base the analysis on: "likes_mean", "likes_median", "dislikes_mean", "dislikes_median", "views_mean", "views_median", "polarity", "subjectivity"
   :return: analysis - a list with same number of elements as number of words in given text, with each corresponding element being the color for that word: "red" means bad, "yellow" means okay, "green" means good and "white" means "Not found" (in database) 
   :rtype: list




.. py:function:: wordscloud(x,Genre)

   This function is to plot graph for the first section: Cloud Map Over Time

   :param x: input time
   :param Genre: different topics


.. py:function:: P_N_cloud(x,Genre)

   This function is to plot graph for section II: Like and Dislike words over time

   :param x: input time
   :param Genre: different topics like: positive or negative results


.. py:function:: color_changer(x,Genre,Metric)

   Change the color of inputed text instantly

   :param str x: scalar depicting the text that needs to be analyzed
   :param str Genre: scalar depicting the genre of the content: "cooking", "gaming", "influencers"
   :param str Metric: scalar depicting the metric to base the analysis on : "likes_mean", "likes_median", "dislikes_mean", "dislikes_median", "views_mean", "views_median", "polarity", "subjectivity"
   





   


   

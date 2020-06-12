Analysis Functions
==================

Below are the functions for generating word sentiment for the text obtained from Youtube


.. py:function:: analyze_text(database_path = 'data', database='data_combined', text="default", genre="cooking", metric="likes")

   Analyzes the given text and produce color labels for the words as well as generate an overall score based on the given genre and metric

   :param str database_path: scalar depicting the path of the database
   :param str database: scalar depicting the name of the pickled database used to conduct analysis
   :param str text: scalar depicting the text that needs to be analyzed
   :param str genre: scalar depicting the genre of the content: "cooking", "gaming", "influencers"
   :param str metric: scalar depicting the metric to base the analysis on: "likes_mean","dislikes_mean", "dislikes_median", "likes_median", "views_mean", polarity", "subjectivity"
   :return: analysis - a list with the same number of elements as number of words in a given text, with each corresponding element being the color for that word: "red" means bad, "yellow" means okay
   	"green" means good and "white" means "Not found" (in database)
   :rtype: list
   :return: score_avg - average value of the score
   :rtype: float or "Not applicable" (if none of the words matched the database

Below is an example code of how to use this function: 

.. code-block:: python
   
   >>> categorization, overall_score = analyze_text("Hi, today we will cook pork", "cooking", "likes_mean")
   >>> categorization
   ['white', 'yellow', 'white', 'yellow', 'yellow', 'yellow']
   >>> overall_score
   29914.25


.. py:function:: generate_DF(year_begin=2015, year_end=2019, output_path = 'data', output_name = 'data_combined',dir_raw_data='data')

   Generating the dataframes for the genres and various features based on the raw text files


   :param int year_begin: numerical year from which the analysis is to start
   :param int year_end: numerical year at the end of which the analysis is to terminate
   :param str output_path: scalar depicting the path where the output file should be stored
   :param str output_name: scalar depicting the name of the output file in which the database is pickled
   :param str dir_raw_data: scalar depicting the directory from where the raw data needs to be picked up

After generating a pickle file with the dataframes stored into it, we can load it like this:

.. code-block:: python

   >>> import pickle
   >>> data = pickle.load(open('data_project.p', 'rb'))

so 'data' is a dictionary where the keys are the genres and the values are the corresponding dataframes

.. code-block:: python

   >>> data.keys()
   dict_keys(['cooking', 'influencers', 'gaming'])


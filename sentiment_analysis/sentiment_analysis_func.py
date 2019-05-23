# -*- coding: utf-8 -*-
def sentiment_analysis(text,bank):
    '''
    Takes in a text file path 'text' and reads in a word bank/dictionary  from 
    'bank' and returns a single score for the general sentiment of that file as
    well as the count and frequency for each word. 
    
    Positive numbers are positive sentiment (the larger positive, the better).
    Negative numbers are negative sentiment (the more negative, the worse).
    
    Inputs
        text(str)
            File name to load from "". File should contain the text to be graded.
        bank(str)
            File name to load from "". File should contain a list of words and 
            scores which will be turned into a dictionary.
            
    Outputs
        score(tuple - float)
            Score is the average sentiment for the text file 
            (total sum score/number of wordsin file) in three parts:
                (positive score, negative score, combined score)
            
        word_freq(pandas DataFrame)
            Pandas DataFrame mapping words in the text under analysis (index) to
            each word's count and frequency (count/total).
    '''
    ##imports
    import pandas as pd
    import itertools as it
    import string
    import re
    
    ##input assertions
    #text
    
    #bank
    
    ##make word dictionary - not all keys are a single word!!!
    #Do we want to remove the non-singletons?
    with open(bank,'r',encoding='utf8') as f_bank:
        word_bank = f_bank.readlines()
        word_bank = word_bank[2:]
        
    tmp = [tuple(i.split('\t')) for i in word_bank]
    word_bank = {i[0]:int(i[1]) for i in tmp}
    
    ##make word data structure
    #read in file
    with open(text,'r',encoding='utf8') as f_data:
        txt = f_data.readlines()
        
    #make all lower case
    txt = [i.lower() for i in txt]
    
    #flatten list and remove punctuation
    txt = [i for j in txt for i in j]
    txt = [i.translate(str.maketrans('', '', string.punctuation)) for i in txt]
    
    #strip useless word
    
    #make data series
    a = pd.Series(txt)
    
    #convert to data frame
    df = a.groupby(by = a.values).count()
    df.name = 'count'
    df = pd.DataFrame(df)
    
    #add freq column
    df['freq'] = df['count']/df['count'].sum()
    
    #add score column from dict if applicable
    
    word_freq = df
    
    ##score 
    score_pos   = 1
    score_neg   = -1
    score_combo = 0
    score = (score_pos, score_neg, score_combo)
    
    ##output assertions
    return score, word_freq
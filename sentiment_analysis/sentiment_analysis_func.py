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
        score(float)
            Average sentiment for the text file (total sum score/number of words
            in file).
            
        word_freq(pandas DataFrame)
            Pandas DataFrame mapping words in the text under analysis (index) to
            each word's count and frequency (count/total).
    '''
    ##imports
    import pandas as pd
    
    ##input assertions
    #text
    
    #bank
    
    
    ##body
    with open(text,'r',encoding='utf8') as f_data:
        txt = f_data.readlines()
        
    with open(bank,'r',encoding='utf8') as f_bank:
        word_bank = f_bank.readlines()
        word_bank = word_bank[2:]
        
    
        
    
    
    ##output assertions
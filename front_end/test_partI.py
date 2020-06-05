import pandas as pd
#!/usr/bin/env python
# coding: utf-8

# In[7]:

#import module
def test_partI():
    """This is the test function for Part I"""
    import os
    os.system("__init__.py")
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
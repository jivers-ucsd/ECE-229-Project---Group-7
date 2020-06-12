def test_partII():
    """This function will test part II """
    #import modules
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

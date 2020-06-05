def test_partII():
    """This function will test part II """
        #import modules
    from ipywidgets import interact, interactive, fixed, interact_manual

    import ipywidgets as widgets

    from ipywidgets import FloatSlider

    from ipywidgets import VBox, HBox, interactive_output

    from ipywidgets import Dropdown
    from matplotlib.image import imread
    from ipywidgets import Button
    import pickle

    from matplotlib import pyplot as plt
    from matplotlib.pylab import subplots
    from wordcloud import WordCloud
    import numpy as np
    from random import shuffle
    from ipywidgets import IntSlider
    import pandas as pd
    from matplotlib.image import imread

    from ipywidgets import AppLayout, Layout
    
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
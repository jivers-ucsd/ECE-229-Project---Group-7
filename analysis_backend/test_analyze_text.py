from analyze_text import analyze_text

def test_analyze_text():
    '''
    Purpose:
    Testing function for analyze_text
    '''
    import pickle
    import os
    import pandas as pd
    analysis_test, score_avg_test = analyze_text(database=os.path.join(os.getcwd()[0: -16], 'data', 'data_combined'), text='I hate pasta but I love pizza', genre='cooking', metric='subjectivity')
    assert all([analysis_test==['white', 'green', 'yellow', 'yellow', 'white', 'green', 'yellow'], score_avg_test == 0.3])

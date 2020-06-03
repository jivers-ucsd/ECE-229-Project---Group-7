from analysis_backend.generate_DF import generate_DF

def test_generate_DF():
    '''
    Purpose:
    Testing function for generate_DF
    '''
    import pickle
    import os
    import pandas as pd
    generate_DF(output_name='test_estimate', dir_raw_data=os.path.join('data', 'test_DF'))
    df_test = pickle.load(open(os.path.join('data', 'test_estimate' + '.p'), 'rb'))
    df_truth = pickle.load(open(os.path.join('data', 'test_groundtruth' + '.p'), 'rb'))
    assert all([df_truth[i].equals(df_test[i]) for i in df_truth.keys()])

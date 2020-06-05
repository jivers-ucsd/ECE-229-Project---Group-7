def test_color():
    '''test_text_colors'''
    from function_partIII import analyze_text_color,color_changer
    assert analyze_text_color('today we will cook delicious beef', 'cooking', 'subjectivity')==['yellow', 'white', 'yellow', 'yellow', 'green', 'yellow']
    assert analyze_text_color('amazing social skills', 'influencers', 'likes_mean')==['yellow', 'yellow', 'white']
    assert analyze_text_color('funny lives in splatoon', 'gaming', 'likes_mean')==['yellow', 'yellow', 'yellow', 'white']
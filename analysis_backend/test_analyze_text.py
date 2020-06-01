def analyze_text(database, text, genre, metric):
    '''
    Purpose: 
    Analyze the given text and produce color labels for the words as well as generate an overall score based on the
    given genre and metric
    
    Input:
    database = str; scalar depicting the name of the pickled database used to conduct analysis
    text = str; scalar depicting the text that needs to be analyzed
    genre = str; scalar depicting the genre of the content: "cooking", "gaming", "influencers"
    metric = str; scalar depicting the metric to base the analysis on: "likes_mean", "likes_median",
             "dislikes_mean", "dislikes_median", "views_mean", "views_median", "polarity", "subjectivity"
    
    Output:
    analysis = list; a list with the same number of elements as number of words in given text, with each
               corresponding element being the color for that word: "red" means bad, "yellow" means okay, "green"
               means good and "white" means "Not found" (in database)
    score_avg = float; average value of the score: float or "Not applicable" (if none of the words matched the
                database)
               
    '''
    from textblob import TextBlob
    import pickle
    import os
    data = pickle.load(open(os.path.join(os.getcwd()[0: -16], 'data', database + '.p'), 'rb'))
    Blob = TextBlob(text)
    scores = []
    df_genre = data[genre]
    score_avg = 0
    counter = 0
    for word in list(Blob.words):
        if word in list(df_genre.words):
            word_index = df_genre.words[df_genre.words==word].index[0]
            scores.append(df_genre[metric][word_index])
            score_avg += df_genre[metric][word_index]
            counter += 1
        else:
            scores.append("Not found")
    if counter > 0:
        score_avg = score_avg/counter
    else:
        score_avg = "Not Applicable"
    intervals = [df_genre[metric].mean()-df_genre[metric].std(), df_genre[metric].mean()+df_genre[metric].std()]
    analysis = []
    for score in scores:
        if score=="Not found":
            analysis.append("white")
            continue
        if score<=intervals[0]:
            analysis.append("red")
        elif score>intervals[0] and score<=intervals[1]:
            analysis.append("yellow");
        elif score>intervals[1]:
            analysis.append("green")
    return analysis, score_avg

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
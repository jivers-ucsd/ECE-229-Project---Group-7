import ipywidgets as widgets
def analyze_text_color(text, genre, metric):
    '''
    Purpose: 
    Analyze the given text and produce color labels for the words 
    Input:
    text = str; scalar depicting the text that needs to be analyzed
    genre = str; scalar depicting the genre of the content: "cooking", "gaming", "influencers"
    metric = str; scalar depicting the metric to base the analysis on: "likes_mean", "likes_median",
             "dislikes_mean", "dislikes_median", "views_mean", "views_median", "polarity", "subjectivity"
    Output:
    analysis = list; a list with the same number of elements as number of words in given text, with each
               corresponding element being the color for that word: "red" means bad, "yellow" means okay, "green"
               means good and "white" means "Not found" (in database)
    '''
    from textblob import TextBlob
    import pickle
    import os
    #load data
    path=os.path.abspath(os.path.dirname(os.getcwd()))+'\\'
    data = pickle.load(open(path+'data_project.p', 'rb'))
    
    path=os.path.abspath(os.path.dirname(os.getcwd()))+'\\'
    pickle.load(open(path+'data_project.p', 'rb'))
    Blob = TextBlob(text)
    scores = []
    df_genre = data[genre]
    for word in list(Blob.words):
        if word in list(df_genre.words):
            word_index = df_genre.words[df_genre.words==word].index[0]
            scores.append(df_genre[metric][word_index])
        else:
            scores.append("Not found")
    intervals = [df_genre[metric].mean()-df_genre[metric].std(), df_genre[metric].mean()+df_genre[metric].std()]
    analysis = []
    for score in scores:
        if score=="Not found":
            analysis.append("white")#not found
            continue
        if score<=intervals[0]:
            analysis.append("red")#bad words
        elif score>intervals[0] and score<=intervals[1]:
            analysis.append("yellow")#okay words
        elif score>intervals[1]:
            analysis.append("green")#good words
    return analysis
w=widgets.Textarea(
    value='',
    placeholder='Type to analyze',
    description='Text box:',
    disabled=False,
    continuous_update=False
)
print(analyze_text_color('funny lives in splatoon', 'gaming', 'likes_mean'))
def color_changer(x,Genre,Metric):
    stat3.value='Now loading...'
    categorization = analyze_text_color(x,Genre,Metric)
    words = x.split()
    for word in words:
        color = analyze_text_color(word,Genre,Metric)
        if color[0] == "red":
            print('\033[31m %s' %word, end = "")
        elif color[0] == "yellow":
            print('\033[33m %s' %word, end = "")
        elif color[0] == "green":
            print('\033[32m %s' %word, end = "")
        else:
            print('\033[37m %s' %word, end = "")
    stat3.value='Complete!'
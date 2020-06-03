def generate_DF(year_begin=2015, year_end=2019, output_path='data', output_name='data_combined', dir_raw_data='data'):
    '''
    Description:
    Generating the dataframes for the genres and various features based on the raw text files
    
    Input:
    year_begin = int; numerical year from which the analysis is to start
    year_end = int; numerical year at the end of which the analysis is to terminate
    output_path = str; scalar depicting the path where the output file should be stored
    output_name = str; scalar depicting the name of the output file in which the database is pickled
    dir_raw_data = str; scalar depicting the directory from where the raw data needs to be picked up
    '''
    import os
    import pandas as pd
    from textblob import TextBlob
    from datetime import datetime
    from statistics import mean, median
    from textblob import Word
    import pickle
    genre_list = os.listdir(dir_raw_data)
    genre_list_clean = [element for element in genre_list if "dataFrame" in element]
    month_categories = list(range(1, (year_end-year_begin+1)*12 + 1)) # 2015 - 2019 (both inclusive)
    data = dict()
    for genre in genre_list_clean:
        name = genre[0: genre.find('_dataFrame.txt')]
        df_input = pd.read_csv(os.path.join(dir_raw_data, genre))
        df = pd.DataFrame(columns=["words", "frequency_time", "likes", "likes_mean", "likes_median", "dislikes",
                                   "dislikes_mean", "dislikes_median", "views", "views_mean", "views_median",
                                   "polarity", "subjectivity"])
        for n in range(0, len(df_input)):
            try:
                date = datetime.strptime(df_input.date[n], "%b %d, %Y")
            except:
                continue
            date_score = (date.year - year_begin)*12 + date.month
            total_text = str(df_input.title[n]) + " " + str(df_input.description[n])
            Blob = TextBlob(total_text)
            Blob = Blob.lower()
            for word in Blob.words:
                if len(Word(word).define())==0:
                    continue
                if date_score > month_categories[-1] or date_score < month_categories[0]:
                    continue
                if word in list(df.words):
                    word_index = df.words[df.words==word].index[0]
                    df.frequency_time[word_index][date_score-1]+=1
                    df.likes[word_index].append(df_input.likes[n])
                    df.dislikes[word_index].append(df_input.dislikes[n])
                    df.views[word_index].append(df_input.views[n])
                else:
                    freq_t = [0]*len(month_categories)
                    freq_t[month_categories.index(date_score)] += 1
                    likes = [df_input.likes[n]];
                    dislikes = [df_input.dislikes[n]]
                    views = [df_input.views[n]]
                    df = df.append(pd.DataFrame([[word, freq_t, likes, 0, 0, dislikes, 0, 0, views,
                                                   0, 0, TextBlob(word).polarity, TextBlob(word).subjectivity]],
                                                 columns=list(df.columns)), ignore_index=True)
        for n in range(0, len(df)):
            df.loc[n, 'likes_mean'] = mean(df.likes[n])
            df.loc[n, 'likes_median'] = median(df.likes[n])
            df.loc[n, 'dislikes_mean'] = mean(df.dislikes[n])
            df.loc[n, 'dislikes_median'] = median(df.dislikes[n])
            df.loc[n, 'views_mean'] = mean(df.views[n])
            df.loc[n, 'views_median'] = median(df.views[n])
        df.drop(columns=['likes', 'dislikes', 'views'], inplace=True)
        data[name] = df
        pickle.dump(data, open(os.path.join(output_path, output_name + '.p'), 'wb'))

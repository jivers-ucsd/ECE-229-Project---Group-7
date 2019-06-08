# Sentiment Analysis on YouTube comments
## Team Members
- Rishabh Sethunathan (rsethuna@)
- Jessica Ivers (jivers@)
- Cyrus Shen (cys005@)

## Problem Statement
- **Demographic Analysis** : Does the demographics of the content creator affect the negativity of the comments they receive?
- **News Channel Analysis** : Does political affiliation of a channel affect the positivity/negativity of the comments being made?

## Methodology
- **Dataset Generation** 
  - Demographic Analysis : Selected three categories to represent type of YouTube channels: Cooking (for instructional), Gaming (for entertainment) and Influencers (a broad survey of the field) and chose recent videos from their channels.
  - News Channel Analysis : Selected six channels with different political affiliations and then chose news stories that were covered by all the channels.
- **Scraping**
  - Used Beautiful Soup to get video links and subscriber counts from channel page.
  - Used Selenium to scrape comments from each video.
- **Sentiment Analysis**
  - Used TextBlob to determine the polarity of each comment, ranging between -1 to +1.
  - Normalized the polarity to a percentage and then averaged it per YouTuber per category.

## Required Packages
- beautifulsoup4
```
pip install beautifulsoup4
```
- selenium
```
pip install selenium
```
Then download the driver and follow further instructions from <a href="https://selenium-python.readthedocs.io/installation.html">here</a>.

- textblob
```
pip install textblob
python -m textblob.download_corpora
```
- wordcloud
```
pip install wordcloud
```
- numpy
- pandas
- matplotlib

## File Structure
```
Root
|
+------ source_links
+------ data
+------ channel_sentiments
+------ scraping
|       |   get_subscribers.py
|       |   get_video_links.py
|       |   scraper.py
|       |   scraping_new.py
|
+------ sentiment_analysis
|       |   text_blob_sentiment.py
|       |   text_blob_sentiment_news.py
|
+------ plotting
|       |   category_graph_functions.py
|       |   news_graph_functions.py
| 
|   Graphing Notebook.ipynb
```

## Runing the code
### Scraping
Script for scraping youtube links is in <code>scraping</code>.

Create folders for content types in <code>source_links</code> and maintain text files for each content creator with links to their videos in them.<br>
Ex: <code>source_links/gaming/pewdiepie</code> would contain links to videos made by pewdiepie.

This can be done by using the <code>get_video_links</code> script followed by the category, username and type command line arguments. Type can be 'u' for user, 'p' for playlist or 'c' for channel.<br>
Ex:
```
python get_video_links.py gaming pewdiepie u
```
will give us video links from pewdiepie's channel and are stored in <code>source_links/gaming/pewdiepie.txt</code>.

For news channels, links were obtained manually, so we could choose stories being covered by both

For scraping subscriber counts, <code>get_subscribers</code>. The users need to be stored in <code>scraping/users.txt</code> in the format : [username] [type] [category]. <br>
Ex: pewdiepie u gaming
```
python get_subscribers.py
```
Script can't get subscribers of channel types, subscriber count was collected manually for those.

Comments scraped will be outputted in folder <code>data</code> under the directory corresponding to the content type, in a text file with name corresponding to file in <code>source_links</code>

Run the script for scraping with the content type directory passed as a command line arguments. <br>
Ex: 
```
python scraper.py gaming
```
for scraping all links in files in directory <code>source_links/gaming/</code>. Scraped comments will be available in <code>data/gaming/</code>.

For news, we have to run the file <code>scraping_news.py</code>.<br>
Ex:
```
python scraping_news.py news
```
for scraping links in files <code>/source_links/news/CNN</code>,<code>/source_links/news/BBC</code>, <code>/source_links/news/Fox</code> etc. Scraped comments will be available in <code>data/news/CNN</code>, <code>data/news/BBC</code>, <code>data/news/Fox</code> etc.

**Note**: Run the scripts from the scraping folder.

### Sentiment Analysis
Code for sentiment analysis is in <code>sentiment_analysis</code>. It uses output structure from scraping. 
Run the script with categories passed as command line arguments. <br>
Ex:
```
python text_blob_sentiment.py gaming
```
will output total sentiment polarity for each creator in the category and output it to <code>sentiment_analysis/textblob_data/gaming.txt</code>

For news,
we have to run the file <code>text_blob_sentiment_news.py</code> with names of the channels passed as command line arguments.<br>
Ex:
```
python text_blob_sentiment_news.py CNN BBC Fox
```
will output sentiment polarities to <code>sentiment_analysis/textblob_data/news/CNN</code>, <code>sentiment_analysis/textblob_data/news/BBC</code> and <code>sentiment_analysis/textblob_data/news/Fox</code>

**Note**: Run the scripts from the sentiment_analysis folder.

### Plotting
Code for plotting is kept in scripts in the plotting directory. The <code>Graphing Notebook</code> has the visualizations from the data. <br>
For news, sentiment polarity data was moved from <code>sentiment_analysis/textblob_data/news</code> to <code>channel_sentiments</code>

### Dataset
Videolinks are available in <code>source_links</code>.<br>
Subscriber count is available in <code>scraping/subscriber_count</code>.<br>
Comments are available in <code>data/</code>.<br>
Sentiment polarities are available in <code>sentiment_analysis/textblob_data</code>.

## Note
The code has been run using:
- Python 3.6.6
- MacOS
May not work with other configurations.

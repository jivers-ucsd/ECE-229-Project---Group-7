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

## Scraping
Create folders for content types in <code>/source_links</code> and maintain text files for each content creator with links to their videos in them.<br>
Ex: <code>/source_links/gaming/pewdiepie</code> would contain links to videos made by pewdiepie.

Comments scraped will be outputted in folder <code>/data</code> under the directory corresponding to the content type, in a text file with name corresponding to file in <code>/source_links</code>

Script for scraping youtube links is in <code>/scraping</code>. Run the script for scraping with the content type directory passed as a command line parameter. <br>
Ex: <code>python scraper.py gaming</code> for scraping all links in files in directory <code>/source_links/gaming/</code>

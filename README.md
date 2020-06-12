# Enabling Content Creators to Fine-Tune Content Descriptions

## Team Members
- Jessica Ivers
- Kanha Batra
- Zichao Li
- Guangjun Xue
- Rui Zhong
- Yuchen Zang


## Problem Statement
How insane is it that sometimes you see the most amazing video on youtube, and yet it took nearly a decade for it to be popular? Or a subpar video which hits a million views within a week? A lot of it has to do with the way you market your content. Sponsoring advertisements for your posts helps, but it depends heavily on the textual supporting descriptions that you add. Google’s page ranking works on that: serving as an excellent example. But an even deeper question is: what makes certain words more popular than others? What receives more hate by the public? Are certain topics more active during election years or during a pandemic? All these questions can help provide a content maker that extra edge they need to push their content to maximum popularity. That’s the aim of our project. We’re trying to create a simple platform which serves as a proof of concept for how sentiment analysis can be extended to utility on a daily basis, with a very wide customer demographic. Obviously, this can be scaled up using a bigger dataset, which is something we would look into if we were to deploy it.

Intallation and Setup
---------------------
This code was run using Python 3.6.6 and is configured for using the Chrome browser. Alternate configurations are not guaranteed to work.

The following pacakages are required for scraping data, analyzing the data, and displaying the results:

**Webscraping**

* beautifulsoup4
* selenium (Then download the driver and follow further instructions from [here](https://selenium-python.readthedocs.io/installation.html).)
* requests


**Analysis**

* textblob (Download the corpora after installing the package with <code>python -m textblob.download_corpora</code>)
* statistics

**Displaying Results**

* ipywidgets
* wordcloud
* matplotlib

**Common to All**

* pickle
* os
* pandas
* datetime
* sys
* time
* numpy


## Runing the code
### Scraping
1. Make sure <code>scraping/users.txt</code> is up to date with desired user list. Each line in the user list must be in the format "Genre type user>. 'Genre' is the fa mily or type of user content (analysis is grouped by this genre!!), such as cooking or gaming.  'Type' can be 'u' for user, 'p' for playlist or 'c' for channel. 'User' is the username the content creator uploads to YouTube under.

2. Run <code>scraping/run_get_video_links</code> to get links to 100+ videos for all the users in <code>scraping/users.txt</code>. This code creates one folder per genre in <code>data/source_links</code> and in each genre-folder creates one text file per user.

3. Run <code>scraping/run_get_video_data</code> to get the meta data for each video link. The script automatically finds all folders and in <code>data/source_links</code> and scrapes each video linked in the text files.

### Sentiment Analysis
1. Make sure that all the scraped data is stored as a `.txt` file with the format `<name>_dataFrame.txt` in the `data/` directory.

2. Run `analysis_backend/generate_DF` to process all such files simultaneously from a given directory (default: `data/`) and into a pickled dictionary of dataframes, each of which is indexed with a key described by the corresponding `<name>`. This program cleans the data, controls the duplicates and removes the garbage elements. It also looks at the distributions of their various attributes across a genre.

3. Run `analysis_backend/analyze_text` to analyze a given piece of text based on the dataframes generated using `generate_DF` to produce a colour coded output as well as an overall score.

### Visualisations 
1. Install package <code>wordcloud</code>.

2. Make sure you have <code>data_combined.p</code> inside the <code>data</code> folder.

3. Open <code>front_end/front-end_Group7-Copy1.ipynb</code> and run the code. You will get the interactive output.

## Note
The code has been run using:
- Python 3.6.6
- Firefox Browser
May not work with other configurations.

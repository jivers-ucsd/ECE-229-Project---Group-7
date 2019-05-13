# Sentiment Analysis on YouTube comments
Project for ECE 143 SP19, done by Rishabh Sethunathan, Jessica Ivers, Cyrus Shen.

## Setup
Selenium webdriver -- To Do

## Scraping
Create folders for content types in <code>/source_links</code> and maintain text files for each content creator with links to their videos in them.<br>
Ex: <code>/source_links/gaming/pewdiepie</code> would contain links to videos made by pewdiepie.

Comments scraped will be outputted in folder <code>/data</code> under the directory corresponding to the content type, in a text file with name corresponding to file in <code>/source_links</code>

Script for scraping youtube links is in <code>/scraping</code>. Run the script for scraping with the content type directory passed as a command line parameter. <br>
Ex: <code>python scraper.py gaming</code> for scraping all links in files in directory <code>/source_links/gaming/</code>

"""
Created on 2021-05-24
@author: ab
Project to test sklearn library for LDA analysis

Data source:
Processing tweets scraped with TweeterScraper:
https://github.com/jonbakerfish/TweetScraper

Script ran as:

$ scrapy crawl TweetScraper -a query="biorefinery OR biorefineries AND lang:en"
For biorefineries tweets

Reference material to merge JSON tweets to DF:
https://medium.com/@shahparthvi22/merge-multiple-json-files-to-a-dataframe-5e5421c40d06



Topic Modeling based on this basic tutorial:
https://omdena.com/blog/topic-modeling-tutorial/
By Jessica Becerra Formoso (https://www.linkedin.com/in/jessicabefor/)
Not a very good post, but I'm interested in the sklearn lybrary
"""
# %% IMPORTS

import os  # for file listing and retrieval
from typing import List  # for type
import pandas as pd  # for data handling


import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA

# %% PATH

data_path = "./data/"
tweets_jason_filename = ""
user_json_filename = ""

# %% FUNCTIONS
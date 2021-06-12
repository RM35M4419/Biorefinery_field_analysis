import pandas as pd
import os

twitter_data_path = './data/twitter_biorefinery_scraped_raw_data/tweet/'
users_data_path = './data/twitter_biorefinery_scraped_raw_data/user/'

test_tweet_file = '425574962'

with open(twitter_data_path + test_tweet_file, 'r') as test_file:
    single_tweet_df = pd.read_json(test_file)

test_user_file = str(single_tweet_df.loc['user_id', 'raw_data'])

with open(users_data_path + test_user_file, 'r') as test_file:
    single_user_df = pd.read_json(test_file)

tweet_file_list = os.listdir(twitter_data_path)

tweet_file_list_sorted = sorted(sorted(tweet_file_list), key=len)  # sorted twice, as we need first the shorted ids

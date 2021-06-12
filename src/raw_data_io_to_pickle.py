import pandas as pd
import os

# %% DATA PATHS

twitter_data_path = './data/twitter_biorefinery_scraped_raw_data/tweet/'
users_data_path = './data/twitter_biorefinery_scraped_raw_data/user/'

tweet_file_list = os.listdir(twitter_data_path)
tweet_file_list_sorted = sorted(sorted(tweet_file_list), key=len)  # sorted twice, as we need first the shorted ids

user_file_list = os.listdir(users_data_path)
user_file_list_sorted = sorted(sorted(user_file_list), key=len)  # sorted twice, as we need first the shorted ids

del tweet_file_list
del user_file_list


# %% METHODS
def tweets_to_df(data_files_list, data_path):
    """Combines all tweet json files in path to a single DF."""

    tweets_count = len(data_files_list)  # to count remaining diles to process
    df = pd.DataFrame()

    counter = tweets_count - 1
    for f in data_files_list:
        data = pd.read_json(data_path + f, orient='index')
        raw_data = data.at['raw_data', 0]
        raw_data_values = pd.DataFrame(list(raw_data.values()))
        index = list(data.index) + list(raw_data.keys())
        data = data.append(raw_data_values)
        data = data.transpose()
        data.columns = index
        data.drop(columns=['id_', 'raw_data'], inplace=True)
        df = df.append(data)

        print(f"\r{counter} tweets remaining to incorporate...", end="")
        counter -= 1
    return df



# %% TEST IMPORTING & COMBINING TWEETS JSON

tweets_df = tweets_to_df(tweet_file_list_sorted, twitter_data_path)

# TEST OK
# %% TEST IMPORTING & COMBINING USERS JSON

users_df = tweets_to_df(user_file_list_sorted, users_data_path)

# TEST OK
# %% EXPORT

tweets_df.to_pickle('./data/biorefinery_tweets_df.pkl')
users_df.to_pickle('./data/biorefinery_user_df.pkl')
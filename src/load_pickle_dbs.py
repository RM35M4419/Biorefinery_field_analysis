# Importing and combining tweets and users DBs
import pandas as pd

def load_pickle_and_combine(tweets_pkl, users_pkl, on_column, rename_cols):
    tweets = pd.read_pickle(tweets_pkl)
    tweets_df = pd.DataFrame(tweets)  # sequence suggested by Albert

    users = pd.read_pickle(users_pkl)
    users_df = pd.DataFrame(users)

    del tweets
    del users

    users_df['user_id'] = users_df.index
    tweets_df['id'] = tweets_df.index
    biorefinery_df = pd.merge(tweets_df, users_df, on=on_column)
    biorefinery_df.rename(columns=rename_cols, inplace=True)
    biorefinery_df.set_index('id', inplace=True)

    del tweets_df
    del users_df

    return biorefinery_df



if __name__ == "__main__":
    tweets_pkl_file = './data/biorefinery_tweets_df_cleaned.pkl'
    users_pkl_file = './data/biorefinery_user_df_cleaned.pkl'
    join_on_column = 'user_id'
    columns_renaming = {
        'created_at_x': 'tweet_created_at',
        'created_at_y': 'user_created_at',
        'favourites_count': 'user_favourites_count'
    }

    df = load_pickle_and_combine(tweets_pkl_file, users_pkl_file, join_on_column, columns_renaming)

    del tweets_pkl_file
    del users_pkl_file
    del join_on_column
    del columns_renaming

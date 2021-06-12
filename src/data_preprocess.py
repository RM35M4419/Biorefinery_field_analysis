import pandas as pd


# %% METHODS

def cleanup_df(df, index_column, date_label, column_types, columns_to_drop):
    """Cleans up the full tweets DF"""

    clean_df = df.copy()

    # Dropping columns not to be used
    clean_df = clean_df.drop(columns_to_drop, axis=1, inplace=False)

    # Type setting. Could be done semi automatically with pd, but I'll do it explicitly

    # Setting predefined types, from a dict
    clean_df = clean_df.astype(column_types)
    # There's only one date column for both tweets & users (created_at)
    clean_df[date_label] = pd.to_datetime(clean_df[date_label], infer_datetime_format=True)

    # Setting the index straight
    clean_df.set_index(index_column, inplace=True)

    return clean_df


# %% TWEETS DATA LOAD
tweets_df = pd.read_pickle('data/biorefinery_tweets_df.pkl')
# users_df = pd.read_pickle('data/biorefinery_user_df.pkl')

# %% TEST TWEETS DF CLEANUP

tweets_index_column = 'id'
date_column = 'created_at'

# I comment out the relevant columns
tweets_columns_to_drop = [
    # 'created_at',
    # 'id',
    'id_str',  # same as 'id'
    # 'full_text',
    'truncated',  # none are truncated, and if it where, we need the full text
    # 'display_text_range',
    'entities',
    'source',  # an URL. App that the user tweeted from. Irrelevant for RQ
    # 'in_reply_to_status_id',
    'in_reply_to_status_id_str',  # same as previous
    # 'in_reply_to_user_id',
    'in_reply_to_user_id_str',  # same as previous
    'in_reply_to_screen_name',  # if I need it, I'll fin it through the id
    # 'user_id',
    'user_id_str',  # same as previous
    'geo',  # only 134 of 30k have geo info, not significant enough
    'coordinates',  # same as above
    'place',  # only 505 of 30k have place info
    'contributors',  # all null
    # 'is_quote_status',
    # 'retweet_count',
    # 'favorite_count',
    # 'reply_count',
    # 'quote_count',
    # 'conversation_id',
    'conversation_id_str',  # same as previous
    'favorited',  # all False
    'retweeted',  # all False
    'lang',  # all EN, as per search filter
    'supplemental_language',  # do I have an use for this?
    'possibly_sensitive',  # irrelevant for RQ and topic, and refers to the link, not the tweet text
    'possibly_sensitive_editable',  # irrelevant for RQ and topic
    'card',  # usually an image or video, irrelevant for RQ and scope
    'extended_entities',
    'quoted_status_id',
    'quoted_status_id_str',
    'quoted_status_permalink',
    'self_thread',
    'scopes'  # all except one are NaN
]

# Column types, only for the kept columns
tweets_column_types = {
    'full_text': str,
    'display_text_range': str,  # verify if I'll use it as a str or list
    'in_reply_to_status_id': 'Int64',
    'in_reply_to_user_id': 'Int64',
    'user_id': int,
    'is_quote_status': bool,
    'retweet_count': int,
    'favorite_count': int,
    'reply_count': int,
    'quote_count': int,
    'conversation_id': 'Int64'
}

tweets_df_cleaned = cleanup_df(tweets_df, tweets_index_column, date_column, tweets_column_types, tweets_columns_to_drop)
tweets_df_cleaned.info()

# %% USERS DATA LOAD
users_df = pd.read_pickle('data/biorefinery_user_df.pkl')

# %% TEST USERS DF CLEANUP

users_index_column = 'id'
users_date_column = 'created_at'

# Dropping lots of useless columns
users_columns = users_df.columns.values.tolist()
user_useful_columns = [
    'id',
    'name',
    'screen_name',
    'location',
    'description',
    'url',
    'followers_count',
    'friends_count',
    'listed_count',
    'created_at',
    'favourites_count',
    'geo_enabled',
    'verified',
    'advertiser_account_type',  # might be relevant to know who pays, but I need to check this var
    'advertiser_account_service_levels'  # idem
]

users_columns_to_drop = [column for column in users_columns if column not in user_useful_columns]  # list comprehension!

# Column types, only for the kept columns. See social-metric.org/twitter-user-data/ for some descriptions
users_column_types = {
    'followers_count': int,  # the number of followers this account has
    'friends_count': int,  # the number of user this account is following
    'listed_count': int,  # number of public list this user us member of
    'favourites_count': int,  # number of tweets this user has favorited in the account lifetime
    'geo_enabled': bool,
    'verified': bool,
}

users_df_cleaned = cleanup_df(users_df, users_index_column, users_date_column, users_column_types,
                              users_columns_to_drop)
users_df_cleaned.info()

# %% EXPORT

tweets_df_cleaned.to_pickle('./data/biorefinery_tweets_df_cleaned.pkl')
users_df_cleaned.to_pickle('./data/biorefinery_user_df_cleaned.pkl')

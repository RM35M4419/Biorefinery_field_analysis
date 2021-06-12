import load_pickle_dbs  # only if not done allready
from matplotlib import pyplot as plt
import numpy as np

df = load_pickle_dbs.load_pickle_and_combine(
    './data/biorefinery_tweets_df_cleaned.pkl',
    './data/biorefinery_user_df_cleaned.pkl',
    'user_id',
    {
        'created_at_x': 'tweet_created_at',
        'created_at_y': 'user_created_at',
        'favourites_count': 'user_favourites_count'
    })

percentiles = list(range(10, 100, 10))
percentiles = [x / 100 for x in percentiles]


description = df.describe(percentiles=percentiles, include='all', datetime_is_numeric=True)

df_grupped_year = df.groupby(df['tweet_created_at'].dt.year)['full_text'].count()

twitter_MAU = {
    "2007": np.NaN,
    "2008": np.NaN,
    "2009": np.NaN,
    "2010": 54,
    "2011": 117,
    "2012": 185,
    "2013": 241,
    "2014": 288,
    "2015": 305,
    "2016": 318,
    "2017": 330,
    "2018": 321,
    "2019": 330,
    "2020": 353
}  # source: https://backlinko.com/twitter-users accessed on 2021-05-30

df_grupped_year.append(twitter_MAU, ignore_index=True)

df_grupped_year.plot()
plt.show()
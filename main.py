import pandas as pd
from auth import connect_to_twitter_oauth


# connect to twitter api
api = connect_to_twitter_oauth()
musk_tweets = api.user_timeline(screen_name='elonmusk')


columns = ['User', 'Tweet']
data = []

# iterate through the tweets and add to list
for tweet in musk_tweets:
    data.append([tweet.user.screen_name, tweet.text])

# add this -> public_metrics to get tweet impressions

# create a data frame of the data, ie. transform the data to column format
df = pd.DataFrame(data, columns=columns)

print(df)

# df.to_csv('tweets.csv')


# TODO
#
# Create a third column for tweet engagement count?
#
# Create Read Update Delete MySQL database and connect to database.
#    mysql_create.py - create database and table(s)
#    mysql_update.py - write data to the table(s)
#    tweek-db -> mysql db name(tweet kapture)

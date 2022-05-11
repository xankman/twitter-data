import pandas as pd
from auth import connect_to_twitter_oauth

api = connect_to_twitter_oauth()
musk_tweets = api.user_timeline(screen_name='elonmusk')

columns = ['User', 'Tweet']
data = []

for tweet in musk_tweets:
    data.append([tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data, columns=columns)

print(df)

df = pd.DataFrame(data, columns=columns)

#df.to_csv('tweets.csv')

print(df)
"""
# TODO
# Create Read Update Delete MySQL database and connect to database.
#    mysql_create.py - create database and table(s)
#    mysql_update.py - write data to the table(s)
import pandas as pd
import tweepy
import configparser
import pandas

#read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['TWITTER']['api_key']
api_key_secret = config['TWITTER']['api_key_secret']

access_token = config['TWITTER']['access_token']
access_token_secret = config['TWITTER']['access_token_secret']

#authentication to twitter api
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

print(public_tweets[0].text)
print(public_tweets[0].user.screen_name)

columns = ['Time', 'User', 'Tweet']
data = []
for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data, columns=columns)

df.to_csv('tweets.csv')

print(df)

#TODO
# Create Read Update Delete MySQL database and connect to database.
#    mysql_create.py - create database and table(s)
#    mysql_update.py - write data to the table(s)

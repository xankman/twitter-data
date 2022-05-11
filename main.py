import pandas as pd
from auth import connect_to_twitter_oauth
"""
musk_tweets = api.user_timeline('elonmusk')

for tweet in musk_tweets:
    print(tweet.text)

"""

api = connect_to_twitter_oauth()
public_tweets = api.home_timeline()

print(public_tweets[0].text)
print(public_tweets[0].user.screen_name)

columns = ['Time', 'User', 'Tweet']
data = []
for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data, columns=columns)

#df.to_csv('tweets.csv')

print(df)
"""
# TODO
# Create Read Update Delete MySQL database and connect to database.
#    mysql_create.py - create database and table(s)
#    mysql_update.py - write data to the table(s)
"""
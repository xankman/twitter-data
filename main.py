import pandas as pd
import pymysql
from auth import connect_to_twitter_oauth
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine


# Connect to Twitter API
api = connect_to_twitter_oauth()
musk_tweets = api.user_timeline(screen_name='elonmusk')

# Create column headings for twitter data
columns = ['User', 'Tweet']
data = []

# Iterate through the tweets and add to list
for tweet in musk_tweets:
    data.append([tweet.user.screen_name, tweet.text])

# Create a data frame of the data, ie. transform the data to column format
df = pd.DataFrame(data, columns=columns)
# print(df)

print("\nConnecting to MySQL...\n")
# Create engine. Need to work on using config.ini for password so no hardcoding here.
engine = create_engine('mysql://root:cryptomake@localhost/tweetdb')
print("Connected.\n")
print("Writing Data...")

# Create the connection and close it (whether successfully connected or failed).
with engine.begin() as connection:
    df.to_sql(name='tweets_table', con=connection, if_exists='replace', index=False)

print("Data written. Now closing connection...")

# df.to_csv('tweets.csv')

# TODO
# Need to check if data already in table. Append only new data.
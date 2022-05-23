import pandas as pd
import pymysql
from auth import connect_to_twitter_oauth
from sqlalchemy import create_engine

pymysql.install_as_MySQLdb()

# Connect to Twitter API. Pick a user. I used Elon but it can be any Twitter user
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
# Create engine. Replace with your own input where applicable
engine = create_engine('mysql://<INSERT USERNAME>:<INSERT DB PASSWORD>@<INSERT HOSTNAME>/<INSERT DB NAME>')
print("Connected.\n")
print("Writing Data...")

# Create the connection and close it (whether successfully connected or failed).
with engine.begin() as connection:
    df.to_sql(name='<INSERT TABLE NAME>', con=connection, if_exists='replace', index=False)

print("Data written. Now closing connection...")

# You can also write to a CSV file with the following function
# df.to_csv('tweets.csv')

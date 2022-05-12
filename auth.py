import tweepy
import configparser


# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['TWITTER']['api_key']
api_key_secret = config['TWITTER']['api_key_secret']

access_token = config['TWITTER']['access_token']
access_token_secret = config['TWITTER']['access_token_secret']

# auth to twitter
def connect_to_twitter_oauth():
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api
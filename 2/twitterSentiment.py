import tweepy
from textblob import TextBlob

consumer_key = 'qyteOqVRBGLRxZ2d70cxi7j38'
consumer_secret = '3CLZrG4t995aWXGfqQEbLCbIhMN4OHhrou3UceEinAlOnr7wDV'

access_token = '243840868-vvkyQ3TqgUgDAOsPYAqj1En8y4bOPh2gsVCKBRH1'
access_token_secret = 'rY4rRj50NkorRXWOomawbl8U6X0eplJXYi4lKjBJqrTdW'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
  print(tweet.text)
  analysis = TextBlob(tweet.text)
  print(analysis.sentiment)
  print()
# app/resources/streamer.py

# third-party imports
from dotenv import load_dotenv
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import tweepy
from flask_restful import Resource
from flask import request, jsonify
from textblob import TextBlob

# inbuilt imports
import os
import re
import json

# local imports
from app.models import Search

# load env variables
load_dotenv()

# variable declarations
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')

# authenticate twitter api
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# setup twitter api
api = tweepy.API(auth)

# function to clean tweets
def clean_tweet(tweet):
  return ''.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
  analysis = TextBlob(tweet)
  return analysis.sentiment.polarity

class Tweets(Resource):

  def get(self):
    '''
    get previous searches and the results
    '''

  def post(self):
    '''
    get the search phrase for the tweets and return the tweets
    '''
    hashtag = request.get_json().get('hashtag');
    if hashtag is not None:
      parsed_tweets = []
      raw_tweets = tweepy.Cursor(api.search, q=hashtag, result_type="recent", lang="en", tweet_mode='extended').items(1000)
      for tweet in raw_tweets:
        parsed_tweet = {}
        if (tweet.user.location is not ""):
          parsed_tweet['id'] = tweet.id
          parsed_tweet['name'] = tweet.user.name
          parsed_tweet['body'] = tweet.full_text
          parsed_tweet['location'] = tweet.user.location
          parsed_tweet['retweets'] = tweet.retweet_count
          parsed_tweet['likes'] = tweet.favorite_count
          parsed_tweet['polarity'] = get_tweet_sentiment(tweet.full_text)
          parsed_tweet['image'] = tweet.user.profile_image_url
          parsed_tweets.append(parsed_tweet)
      try:
        response = {
          'status': 'Success',
          'data': parsed_tweets,
          'message': 'Successfully searched and found tweets'
        }
        return response, 200
      except Exception as e:
        response = {
          'status': 'Error',
          'data': str(e)
        }
        return response, 400

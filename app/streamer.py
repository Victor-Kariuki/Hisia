# streamer.py

# third-party imports
from dotenv import load_dotenv
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# inbuilt imports
import os

# load env variables
load_dotenv()

# variable declarations
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')

class StdOutListener(StreamListener):
  def on_data(self, data):
    print(data)
    return True

  def on_error(self, status):
    print(status)

if __name__ == '__main__':
  listener = StdOutListener()

  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  stream = Stream(auth, listener)
  try:
    print('Starting stream ...')
    stream.filter(track=['Donald Trump'])
  except KeyboardInterrupt:
    print('Stopping streamer ...')
  finally:
    print('Streaming session ended')



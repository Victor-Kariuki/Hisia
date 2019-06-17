# streamer.py

# third-party imports
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# inbuilt imports
import os


# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
  '''
    streaming & processing live tweets
  '''

  def __init__(self):
    pass


  def stream_tweets(self, fetched_tweets_filename, hash_tag_list):

    # twitter authentication & connection to the twitter streaming api
    listener = StdOutListener(fetched_tweets_filename)
    auth = OAuthHandler(
      os.getenv('TWITTER_CONSUMER_API_KEY'),
      os.getenv('TWITTER_CONSUMER_API_SECRET_KEY')
    )

    auth.set_access_token(
      os.getenv('TWITTER_ACCESS_TOKEN'),
      os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    )

    # filter twitter streams to capture data by keywords
    Stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
  '''
    prints recieved tweets to stdout
  '''

  def __init__(self, fetched_tweets_filename):
    self.fetched_tweets_filename = fetched_tweets_filename

  def on_data(self, data):
    try:
      print(data)
      with expression as target:
        pass
    except BaseException as e:
      print("Error on_data %s" % str(e))
    return True

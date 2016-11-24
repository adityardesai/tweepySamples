import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import json

consumer_key = 'bxIxQJdzLK8G6SEOZjJtgKdyk'
consumer_secret = '0enunQeFCFWsm1xRYmgpgXmHQMpCociNzJITiK41RdRTc3fzV8'
access_token = '59079232-my7quqCEl0nydcar3AJoGrkJgrMfVuwLRlP2qJ5J2'
access_secret = 'LxdqwJrF9nWOK6Vl9SBkwVtXvgo0r4IEOKiX6clWphcQN'


class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)
    def on_status(self, status):
        if 'weather' in status.text.lower():
            print(status.text)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    stream = Stream(auth, l)
    stream.filter(locations=[-86.33,41.63,-86.20,41.74])
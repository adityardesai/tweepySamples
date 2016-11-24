import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import json
 


class TwitterCrawler:
    
    def __init__(self):
     self.consumer_key = 'bxIxQJdzLK8G6SEOZjJtgKdyk'
     self.consumer_secret = '0enunQeFCFWsm1xRYmgpgXmHQMpCociNzJITiK41RdRTc3fzV8'
     self.access_token = '59079232-my7quqCEl0nydcar3AJoGrkJgrMfVuwLRlP2qJ5J2'
     self.access_secret = 'LxdqwJrF9nWOK6Vl9SBkwVtXvgo0r4IEOKiX6clWphcQN'
     self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
     self.auth.set_access_token(self.access_token, self.access_secret)

     self.api = tweepy.API(self.auth,wait_on_rate_limit=True)
     
     self.myListIDs=[34373370, 26257166, 12579252]
     self.FriendsList=[]
     self.FollowersList=[]
     
    def getUser(self,userID):
        u = self.api.get_user(userID)
        return u
    def getFriendsList(self,ID):
        fListObj=self.api.friends_ids(ID)
        self.FriendsList=fListObj
        #return fList
    def getFollowersList(self,ID):
        foList=self.api.followers_ids(ID)
        self.FollowersList=foList
    def getTweetsofWord(self,word):
        print(tweepy.Cursor(self.api.search, q='trump', geocode="-86.33,41.63,-86.20,41.74").items())
 
if __name__ == "__main__":
    myTwitter = TwitterCrawler()
    for i in myTwitter.myListIDs:
        #myTwitter.getFollowersList(i)
        #myTwitter.getFriendsList(i)
        pass
    for i in myTwitter.FollowersList:
        #print("Followers " +str(myTwitter.getUser(i)))
        pass
    for i in myTwitter.FriendsList:
        #print("Friends " +str(myTwitter.getUser(i)))
        pass
    myTwitter.getTweetsofWord('word')
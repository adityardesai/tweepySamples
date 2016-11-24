import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'bxIxQJdzLK8G6SEOZjJtgKdyk'
consumer_secret = '0enunQeFCFWsm1xRYmgpgXmHQMpCociNzJITiK41RdRTc3fzV8'
access_token = '59079232-my7quqCEl0nydcar3AJoGrkJgrMfVuwLRlP2qJ5J2'
access_secret = 'LxdqwJrF9nWOK6Vl9SBkwVtXvgo0r4IEOKiX6clWphcQN'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True)
# for status in tweepy.Cursor(api.home_timeline).items(10):
#     print(status._json) 
#     pass
# for status in tweepy.Cursor(api.home_timeline).items(10):
#     print(status._json)
#     pass
# for friend in tweepy.Cursor(api.friends).items():
#     print(friend._json)
#     pass
# for tweet in tweepy.Cursor(api.user_timeline).items():
#     print(tweet._json)
#     pass


#Collecting user's profile information: 
#u = api.get_user(13334762)
#print(u.screen_name)#github
myList = [34373370, 26257166, 12579252]

for i in myList:
    #u = api.get_user(i)
    #print(u.screen_name)
    pass

myList = [34373370, 26257166, 12579252] 
for i in myList:
    u = api.get_user(i)    
    for user in tweepy.Cursor(api.followers, screen_name=u.screen_name).items(20):
        print("Followers "+user.screen_name)
        
for i in myList:
    u = api.get_user(i)    
    for user in tweepy.Cursor(api.friends, screen_name=u.screen_name).items(20):
        print("Friends "+user.screen_name)
        
        
        
        
        
        
        
        
        
        
        
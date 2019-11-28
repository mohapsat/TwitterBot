import tweepy
import conf
import time
import requests


auth = tweepy.OAuthHandler(conf.API_KEY, conf.API_SECRET)
auth.set_access_token(conf.ACCESS_TOKEN, conf.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

user = 'mohapsat'  # Me

u = api.get_user(user)
MY_ID = u.id_str

# following = set(api.friends_ids(MY_ID))  # people am follwoing
followers = api.followers_ids(MY_ID)  # people who are following me

print(f"followers count = {len(followers)}")

# get most recent tweet by followers

test_follower_ids = followers[:10]

print(f"test_follower_ids = {test_follower_ids}")

follower_tweets = list()
hashtags = list()

for follower_id in test_follower_ids:
    new_tweets = api.user_timeline(user_id=follower_id, count=1, tweet_mode="extended",)
    tweet = [[tweet.full_text] for tweet in new_tweets]
    hashtag = [[tweet.entities.get('hashtags')] for tweet in new_tweets]
    follower_tweets.append(tweet)
    hashtags.append(hashtag)

print(f"follower_tweets = {follower_tweets}")
print(f"hashtags = {hashtags}")

'''
followers count = 147
test_follower_ids = [2201679912, 1035066713669337093]
follower_tweets = [
    ['Digital Trends Ecommerce 2017 via @brightvessel https://t.co/SKLGRhnlKd'], 
    ['While damaged, this creature has attack +3.\nhttps://t.co/KNgX6nb7WC\nhttps://t.co/8deex4dZKs']
]
'''
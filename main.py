import tweepy
import conf
import time
import requests


auth = tweepy.OAuthHandler(conf.API_KEY, conf.API_SECRET)
auth.set_access_token(conf.ACCESS_TOKEN, conf.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

### GET id_str for tweeter users to follow

user_ids = [] # empty list to hold ids

users = ['OpenAI', 'GitHubGameOff', 'SalesforceDevs', 'GoogleAI', 'techreview',
         'distillpub', 'github', 'scratch', 'TensorFlow', 'godotengine', 'ARKInvest',
         'ForbesTech', 'TechCrunch', 'awscloud', 'a16z', 'NASA', 'ProductHunt', 'Google',
         'mwseibel', 'ycombinator', 'ThePSF', 'djangoproject', 'restframework', 'pycon', 'E3', 'PlayStation',
         'IndieHackers', 'MIT', 'TEDTalks', 'MSFTResearch']

# users = []

for user in users:
    u = api.get_user(user)
    user_ids.append(u.id_str)

# print(user_ids)
# ['4398626122', '3524101993', '7834512', '4783690002', '33838201', '15808647']


### Fetch their latest tweets from the timeline, favorite and retweet

# https://tweepy.readthedocs.io/en/v2.3.0/api.html?highlight=user_timeline#API.user_timeline
for user_id in user_ids:
    tweet = api.user_timeline(user_id=user_id, count=1)
    try:
        # tweet[0].favorite() # favorite the tweet
        tweet[0].retweet()  # retweet
        print("still here")
        pass
    except:
        print('already retweeted status.')
    # print(tweet[0].text)
    time.sleep(2)   # sleep 2 seconds

# extend to do more cool stuff later...

##-------------------->

############ Post top story from HackerNews ##############

##-------------------->

# 1. get r_topstory_id  from https://hacker-news.firebaseio.com/v0/topstories.json

hn_topstory_uri = 'https://hacker-news.firebaseio.com/v0/topstories.json'

# Get top 10 stories
r_topstory_10 = requests.get(hn_topstory_uri).json()[:10]

for r_topstory_id in r_topstory_10:
    # 2. Get contents of the r_topstory_id from https://hacker-news.firebaseio.com/v0/item/<id>.json
    topstory_dtl_uri = 'https://hacker-news.firebaseio.com/v0/item/' + str(r_topstory_id) + '.json'
    topstory_dtl_title = requests.get(topstory_dtl_uri).json()['title']
    topstory_dtl_url = requests.get(topstory_dtl_uri).json()['url']
    hn_topstory_tweet = topstory_dtl_title + ' ' + topstory_dtl_url + ' ' + '#AI #news #tech'

    print('tweeting - > %s' % hn_topstory_tweet)
    try:
        api.update_status(status=hn_topstory_tweet)
    except:
        print('already tweeted status from hn')
    time.sleep(2)  # sleep 2 seconds between each tweet

# Tweeted top 10




############ --> PRESBOT


auth = tweepy.OAuthHandler(conf.PRESBOT_API_KEY, conf.PRESBOT_API_SECRET)
auth.set_access_token(conf.PRESBOT_ACCESS_TOKEN, conf.PRESBOT_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

### GET id_str for tweeter users to follow

user_ids = [] # empty list to hold ids

users = ['OpenAI', 'GitHubGameOff', 'SalesforceDevs', 'GoogleAI', 'techreview',
         'distillpub', 'github', 'scratch', 'TensorFlow', 'godotengine', 'ARKInvest',
         'ForbesTech', 'TechCrunch', 'awscloud', 'a16z', 'NASA', 'ProductHunt', 'Google',
         'mwseibel', 'ycombinator', 'ThePSF', 'djangoproject', 'restframework', 'pycon', 'E3', 'PlayStation',
         'IndieHackers', 'MIT', 'TEDTalks', 'MSFTResearch', 'mohapsat']

# users = []

for user in users:
    u = api.get_user(user)
    user_ids.append(u.id_str)

# print(user_ids)
# ['4398626122', '3524101993', '7834512', '4783690002', '33838201', '15808647']


### Fetch their latest tweets from the timeline, favorite and retweet

# https://tweepy.readthedocs.io/en/v2.3.0/api.html?highlight=user_timeline#API.user_timeline
for user_id in user_ids:
    tweet = api.user_timeline(user_id=user_id, count=1)
    try:
        # tweet[0].favorite() # favorite the tweet
        tweet[0].retweet()  # retweet
        print("still here")
        pass
    except:
        print('already retweeted status.')
    # print(tweet[0].text)
    time.sleep(2)   # sleep 2 seconds

# extend to do more cool stuff later...

##-------------------->

############ Post top story from HackerNews ##############

##-------------------->

# 1. get r_topstory_id  from https://hacker-news.firebaseio.com/v0/topstories.json

hn_topstory_uri = 'https://hacker-news.firebaseio.com/v0/topstories.json'

# Get top 10 stories
r_topstory_10 = requests.get(hn_topstory_uri).json()[:10]

for r_topstory_id in r_topstory_10:
    # 2. Get contents of the r_topstory_id from https://hacker-news.firebaseio.com/v0/item/<id>.json
    topstory_dtl_uri = 'https://hacker-news.firebaseio.com/v0/item/' + str(r_topstory_id) + '.json'
    topstory_dtl_title = requests.get(topstory_dtl_uri).json()['title']
    topstory_dtl_url = requests.get(topstory_dtl_uri).json()['url']
    hn_topstory_tweet = topstory_dtl_title + ' ' + topstory_dtl_url + ' ' + '#technews #chatbots #automation #AI #ML '

    print('tweeting - > %s' % hn_topstory_tweet)
    try:
        api.update_status(status=hn_topstory_tweet)
    except:
        print('already tweeted status from hn')
    time.sleep(2)  # sleep 2 seconds between each tweet

# Tweeted top 10


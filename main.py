import tweepy
import conf
import time


auth = tweepy.OAuthHandler(conf.API_KEY, conf.API_SECRET)
auth.set_access_token(conf.ACCESS_TOKEN, conf.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

### GET id_str for tweeter users to follow

user_ids = [] # empty list to hold ids

users = ['OpenAI', 'GitHubGameOff', 'SalesforceDevs', 'DeepMindAI', 'GoogleAI', 'techreview',
         'distillpub', 'github', 'scratch', 'TensorFlow', 'godotengine', 'ARKInvest',
         'ForbesTech', 'TechCrunch', 'awscloud', 'a16z', 'NASA', 'ProductHunt', 'Google',
         'mwseibel', 'ycombinator', 'ThePSF', 'djangoproject', 'restframework', 'pycon', 'E3', 'Xbox',
         'IndieHackers', 'MIT', 'TEDTalks', 'MSFTResearch']

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
        tweet[0].favorite() # favorite the tweet
        tweet[0].retweet()  # retweet
    except:
        print('already retweeted status.')
    # print(tweet[0].text)
    time.sleep(2)   # sleep 2 seconds

# extend to do more cool stuff later...


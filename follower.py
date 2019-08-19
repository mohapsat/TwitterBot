import tweepy
import conf
import time
import requests


auth = tweepy.OAuthHandler(conf.API_KEY, conf.API_SECRET)
auth.set_access_token(conf.ACCESS_TOKEN, conf.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# ========>> Follow Thee followers

# https://github.com/tweepy/tweepy/blob/master/docs/code_snippet.rst


# def limit_handled(cursor):
#     while True:
#         try:
#             yield cursor.next()
#         except tweepy.RateLimitError:
#             time.sleep(15 * 60)
#
#
# i = 0
# for follower in limit_handled(tweepy.Cursor(api.followers).items()):
#     follower.follow()
#     # print(f"Follower {i} = {follower.name} ")
#     i+=1
#     print(f"Follower {i} = {follower.name} followed")
#
#

try:

    user = 'mohapsat'     # Me

    u = api.get_user(user)
    MY_ID = u.id_str

    following = set(api.friends_ids(MY_ID))     # people am follwoing
    followers = set(api.followers_ids(MY_ID))   # people who are following me
    not_following = followers - following       # people my bot needs to follow

    # print(f"people my bot needs to follow: {not_following}")

    for item in list(not_following)[:1]:
        api.create_friendship(item)
        time.sleep(2)
        print(f"now following: {item}")

except tweepy.error.TweepError:
    print("tweepy.error.TweepError ")


## My Personal Tweeter (HN TOP 10) + Re-tweeter Bot

Hacked together in a couple hrs.

### Pre-requisites:

- [x] Signup for a twitter developers account
- [x] Wait a couple hours or upto a day for approval
- [x] Create an APP

### Setup
- [x] Procure API creds from your account
- [x] Create config.py and set the following env variables
    - API_KEY
    - API_SECRET
    - ACCESS_TOKEN
    - ACCESS_TOKEN_SECRET
    
- [x] in `Main.py` replace users inside users list with the twitter handles of the users you'd like to retweet

    ```For example:
    users = ['OpenAI', 'GitHubGameOff', 'SalesforceDevs', 'DeepMindAI', 'GoogleAI', 'techreview']
    ``` 

- [x] Schedule to run on a desired interval

- [x] Follow me on twitter [@mohapsat](https://twitter.com/mohapsat)

- [x] Support Open Source and [Tweepy](https://tweepy.readthedocs.io/en/3.7.0/index.html) 

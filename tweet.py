

import twitter

access_token = 'afsdafsdfdaadadsffasdadsfafds'
access_secret = 'fajndskjldasnfckldsjjfasldkcalkcnas'
"""
api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token, access_token_secret=access_secret)

api.PostUpdate('hello world') """

import tweepy

CONSUMER_KEY = consumer_key
CONSUMER_SECRET = consumer_secret

"""auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()
print 'Please authorize: ' + auth_url
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
print "ACCESS_KEY = '%s'" % auth.access_token.key
print "ACCESS_SECRET = '%s'" % auth.access_token.secret """

class tweet_mama:
	def __init__(self):
		CONSUMER_KEY = '4qhVwgXY2ZZvbEN2qGTzdw'
		CONSUMER_SECRET = 'OdfyJE3NUpckodvGDw3fJmzivSz2xDdKd7ZDsNsf0Q'
		ACCESS_KEY = '510800394-Zep39CczM0HKUGYKC5R5G2vlLzWyA2aJZxVx9Dx5'
		ACCESS_SECRET = 'hHZdSFabzArRNQ0cQwrNGXcbCIdGNcUgGQ7qCD3c0'
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
		self.api = tweepy.API(auth)

	def tweet(self,text):
		self.api.update_status(text)



tm = tweet_mama()

tm.tweet('hello world')

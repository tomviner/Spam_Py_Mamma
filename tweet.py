import tweepy
import twitter


class tweet_mama:
	def __init__(self):
		self.CONSUMER_KEY = '4qhVwgXY2ZZvbEN2qGTzdw'
		
		self.CONSUMER_SECRET = 'OdfyJE3NUpckodvGDw3fJmzivSz2xDdKd7ZDsNsf0Q'
		#self.ACCESS_KEY = '510800394-Zep39CczM0HKUGYKC5R5G2vlLzWyA2aJZxVx9Dx5'
		#self.ACCESS_SECRET = 'hHZdSFabzArRNQ0cQwrNGXcbCIdGNcUgGQ7qCD3c0'
		
		self.ACCESS_KEY = '510800394-Z7eeQiLIZOCccMbjyPElbSRyQb9SiezBax2C4tHq'
		self.ACCESS_SECRET = 'ioVceYgrfaPJ1sYCSXhdOqLef9przgmRCBhDg9Q'
		
		auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
		auth.set_access_token(self.ACCESS_KEY, self.ACCESS_SECRET)
		self.api = tweepy.API(auth)
	
	def register(self):	
		auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
		auth_url = auth.get_authorization_url()
		print 'Please authorize: ' + auth_url
		verifier = raw_input('PIN: ').strip()
		auth.get_access_token(verifier)
		print "ACCESS_KEY = '%s'" % auth.access_token.key
		print "ACCESS_SECRET = '%s'" % auth.access_token.secret


	def tweet(self,text):
		self.api.update_status(text)

# search for 'hammer' 
# respond to roman numerals

tm = tweet_mama()
#tm.register()
#tm.tweet('hello world')
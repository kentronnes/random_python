import tweepy
import twitter_auth as ta

auth = tweepy.OAuthHandler(ta.consumer_key, ta.consumer_secret)
auth.set_access_token(ta.access_token, ta.access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#  	print(tweet.text)

# Get the User object for twitter...
user = api.get_user('stripe')

print("Handle: @" + user.screen_name)
print("Description: " + user.description)
print("Followers: " + str(user.followers_count))
print("Following: " + str(user.friends_count))
print("Number of Tweets: " + str(user.statuses_count))


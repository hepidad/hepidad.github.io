
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "798059385578733568-zcqhOYrVsOn565QLsvV0iotWRWYdAYr"
access_token_secret = "pOF57UTQBvI0kwpNFi6Bbnzr52um7IynrfNlYvYrAEW6Z"
consumer_key = "xp5d8RWCriseZdtukAQqUmMaK"
consumer_secret = "XxaQNA9GVRtcqiKcF2ZbKjZDUUYrlk3RUtk3kGR8HuG7PkgtqF"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'java'])

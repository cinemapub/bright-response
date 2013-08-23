from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import ConfigParser
import os.path
from pprint import pprint

Config = ConfigParser.ConfigParser()
cfile="../../config/config.ini"
cexist=os.path.exists(cfile)
print ("%s exists: %r" % (cfile,cexist))
Config.read("../../config/config.ini")
twcred="credentials:twitter"

consumer_key=Config.get(twcred,"consumer_key")
consumer_secret=Config.get(twcred,"consumer_secret")

access_token=Config.get(twcred,"access_token")
access_token_secret=Config.get(twcred,"access_token_secret")

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    pprint (vars(auth))
    auth.set_access_token(access_token, access_token_secret)

    pprint (vars(auth))
    print auth.get_username()
    

    stream = Stream(auth, l)
    stream.filter(track=['basketball'])

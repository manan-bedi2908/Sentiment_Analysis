from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


api_key = '###'
api_secret = '###'
access_token = '###'
access_secret = '###'



class StdOutListener(StreamListener):

    def on_data(self, data):
        with open('data/tweetdata.txt','a') as tf:
            tf.write(data)
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)
    stream.filter(track=['depression', 'anxiety', 'mental health', 'suicide', 'stress', 'sad', 'sadness', 'unhappy'])
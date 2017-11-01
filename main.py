import tweepy
from kafka import KafkaProducer


consumer_key ='wd9IGU1w1KGLmuNsgih9Kmnlx'
consumer_secret = 'AwOI8JR6K17iO3dTLjZsJN9ny2Eswc6Z3VUFHPqv7oCK4QO5ZM'
access_token = '42989180-zyBKiGiMyft5O5hSR6vG4W1G2h1yYWvYl6Lr2xueJ'
access_token_secret = 'MIqKTwuL5HDWoNjQ301JtUKLpc3z6VPSGv0dojVqrUphJ'


class MyStreamListener(tweepy.StreamListener):

    def __init__(self):
        super().__init__()
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092')



    def on_status(self, status):
        self.producer.send('test', status.text.encode('UTF-8'))
        print(status.text)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=["Hammersmith", "Fulham", "Shepherd's Bush", "Brook Green", "Parson's Green"])

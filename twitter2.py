import tweepy
import os
from dotenv import load_dotenv

load_dotenv()



class Bot:
    def __init__(self):
        # Authenticate to Twitter
        auth = tweepy.OAuth1UserHandler(os.getenv("API_KEY"), os.getenv("API_SECRET"), os.getenv("ACCESS_TOKEN"),
                                        os.getenv("ACCESS_SECRET"))
        # Create API object
        self.api = tweepy.API(auth)

    def test(self):
        public_tweets = self.api.home_timeline()
        for tweet in public_tweets:
            print(tweet.text)

    def tweet(self, text=False, img=False):
        return self.api.update_status_with_media(status=text, filename=img)


if __name__ == '__main__':
    t = Bot()
    #t.test()
    print(t.tweet("Hello ca tweet ici ? (python)  📌","./img.jpeg"))

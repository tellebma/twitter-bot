import json
import os

import requests
from dotenv import load_dotenv
import oauth2 as oauth

load_dotenv()


class Bot:

    def __init__(self):
        self.URL = "https://api.twitter.com/2/"
        self.oauth_token()
        exit()

    def oauth_token(self):
        consumer = oauth.Consumer(key=os.getenv("API_KEY"), secret=os.getenv("API_SECRET"))
        access_token = oauth.Token(key=os.getenv("ACCESS_TOKEN"), secret=os.getenv("ACCESS_SECRET"))
        client = oauth.Client(consumer, access_token)
        print(client.token)


    def tweet(self, text=False, img=False):
        """

        :param text:
        :param img:
        :return:
        """
        url = self.URL + "tweets"
        #header
        header = {**self.header, **{"oauth_token":"a"}}

        #payload
        payload = {}
        if text:
            payload['text'] = text
        if img:
            if type(img) == str:
                payload['media_id'] = self.upload_media(loacl_path_media=img)
            elif type(img) == int:
                payload['media_id'] = img
            else:
                print(f"No img added - not understood \n {img}")
        response = requests.request("POST",url, headers=header, data=json.dumps(payload))
        """if response.status_code != 200:
            print(response.text)
            return False"""
        return response

    def upload_media(self, loacl_path_media: str) -> int:
        """
        Je comprends pas pk il garde pas la meme url...
        https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-upload

        :param loacl_path_media:
        :return:
        """
        exit("FUCK Les media pr le moment.")
        url = ""
        payload = {}
        response = requests.request("POST", url, headers=self.header, data=json.dumps(payload))
        if response.status_code != 200:
            print(response.text)
            return False
        return response


if __name__ == '__main__':
    t = Bot()
    print(t.tweet("Hello ca tweet ici ? (python)  📌"))

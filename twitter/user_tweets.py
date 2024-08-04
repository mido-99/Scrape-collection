import requests
import json
import jmespath
from dotenv import get_variable


COOKIES = get_variable('.env', 'COOKIES')

# https://x.com/Scrapfly_dev
class UserTweets:
    
    def __init__(self, profile_url):
        self.username = profile_url.split('/')[-1]
        self.user_id = self.get_id()

    def get_id(self):
        pass
    
    def get_tweets(self):
        return self.username, self.user_id

user = UserTweets('https://x.com/Scrapfly_dev')
print(user.get_tweets())
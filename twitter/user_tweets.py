import requests
import json
import jmespath
from dotenv import get_variable


COOKIES = get_variable('.env', 'COOKIES')

# https://x.com/Scrapfly_dev
class UserTweets:
    """Collect any data you want from twitter!"""

    def __init__(self, profile_url):
        self.username = profile_url.split('/')[-1]
        self.profile_data = None
    
    def get_profile_data(self):
        """Get all interesting data about X.com user"""

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'cookie': 'des_opt_in=Y; dnt=1; guest_id=v1%3A172130542309363976; night_mode=2; guest_id_marketing=v1%3A172130542309363976; guest_id_ads=v1%3A172130542309363976; g_state={"i_l":0}; kdt=hBXbJG7ZcXtmGD9UPoULxuaOfCDp1EINzrfQxzkQ; auth_token=1a057101daf2960459a8ef655d813f5b11f27ff2; twid=u%3D900594828018409472; ct0=7eb78511619661d262e738930f15c27c414c618d9ab183f0cc4d26f11bffae0d929b7ab0253af92aa8e71ab6f4d4ec4a5e19c9ee4c447808477d2ef1e9a781b4e2e703270cb4c72acace3064740c8e05; lang=en; external_referer=padhuUp37zjSzNXpb3CVCQ%3D%3D|0|8e8t2xd8A2w%3D; personalization_id="v1_vxhH81wZEfL+/9sib+ATWg=="',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://x.com/Scrapfly_dev',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'x-client-transaction-id': 'W5XaUtO8scgL8nSq3NUxAYSJAhb8K2393hHKGBQB9cfWe3ynjjV6tGqBrQRZR8qxGn1WO1l8Eiio46NoCrRzGC8/VGlNWA',
            'x-csrf-token': '7eb78511619661d262e738930f15c27c414c618d9ab183f0cc4d26f11bffae0d929b7ab0253af92aa8e71ab6f4d4ec4a5e19c9ee4c447808477d2ef1e9a781b4e2e703270cb4c72acace3064740c8e05',
            'x-twitter-active-user': 'yes',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-twitter-client-language': 'en',
        }

        params = {
            'variables': json.dumps({'screen_name': self.username, 'withSafetyModeUserFields': True}),
            'features': '{"hidden_profile_subscriptions_enabled":true,"rweb_tipjar_consumption_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"subscriptions_verification_info_is_identity_verified_enabled":true,"subscriptions_verification_info_verified_since_enabled":true,"highlights_tweets_tab_ui_enabled":true,"responsive_web_twitter_article_notes_tab_enabled":true,"subscriptions_feature_can_gift_premium":true,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
            'fieldToggles': '{"withAuxiliaryUserLabels":false}',
        }
        # print(params)
        response = requests.get(
            'https://x.com/i/api/graphql/Yka-W8dz7RaEuQNkroPkYw/UserByScreenName',
            params=params,
            headers=headers,
        )
        if response.status_code == 200:
            self.profile_data = self._parse_profile_data(response.json()['data']['user']['result'])
            return self.profile_data
        else:
            return None
    
    def _parse_profile_data(self, data):
        """Parse json data fetched by api in get_profile_data()"""

        parsed_data = jmespath.search('''{
            user_id: rest_id,
            blue_verified: is_blue_verified,
            created: legacy.created_at,
            description: legacy.description,
            bio_urls: legacy.entities.url.urls[].expanded_url,
            followers: legacy.followers_count,
            following: legacy.friends_count,
            location: legacy.location,
            media_count: legacy.media_count,
            name: legacy.name,
            pinned_tweet_ids: legacy.pinned_tweet_ids_str,
            sensitive_account: legacy.possibly_sensitive,
            profile_banner: legacy.profile_banner_url,
            profile_image: legacy.profile_image_url_https,
            username: legacy.screen_name,
            posts_number: legacy.statuses_count,
            site_url: legacy.url
        }''', data)
        return parsed_data

    def get_user_id(self):
        """Returns internal X.com user id"""

        if not self.profile_data:
            self.profile_data = self.get_profile_data()
        return self.profile_data['user_id']

    def get_tweets(self):
        return self.username, self.user_id


user = UserTweets('https://x.com/Scrapfly_dev')
# print(user.get_tweets())
print(user.get_profile_data())
print(user.get_user_id())
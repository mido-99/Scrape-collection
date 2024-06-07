from bs4 import BeautifulSoup
import httpx
import json
import pandas as pd
from time import sleep

import requests


class MakeScraper:
    
    def __init__(self):
        self.final = []
    
    def main(self):
        pass
        
    def fetch_all_plugin_ranked(self):
        
        search_api = "https://www.make.com/pw-api/integrations/search-apps"
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'content-type': 'application/json',
            'referer': 'https://www.make.com/en/integrations?community=1&verified=1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        }

        params = {
            'name': '',
            'limit': '3000', # high limit to get all plugins
            'offset': '0',   # starting point
            'sort': 'Most Popular',
            'category': '',
            'addOnApps': 'true',
            'nativeApps': 'true',
            'isCategory': 'false',
            'isSubCategory': 'false',
        }
        with httpx.Client(headers=headers, params=params) as client:
            response = client.get(search_api)
            if response.status_code == 200:
                self.entities = response.json()['entities']
            else:
                print("Error occured in search api in fetch_all_plugin_ranked()")
                return response.raise_for_status()

    def plugin_page(self):
        
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        }

        with httpx.Client(headers=headers) as client:
            self.df['Description'] = self.df['slug'].apply(lambda x: self.extract_description(client, x))

    def extract_description(self, session, plugin_slug, plugin_name):

        base_url = "https://www.make.com/en/integrations/"
        attemps = 3
        for attempt in range(attemps):
            response = session.get(base_url + plugin_slug)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                json_str = soup.find('script', id="__NEXT_DATA__").text
                json_data = json.loads(json_str)
                description = json_data['props']['pageProps']['appDetails']['description'].replace(r"{name}", plugin_name)
                return description
            else:
                sleep(5)
                if attempt == attemps -1:
                    print(response.status_code, response.text)
                    print(f"Error in plugin page: {plugin_name}")
                    return None

    def category(self):
        cookies = {
            'last_touch_gclid': 'undefined',
            'first_touch_gclid': 'undefined',
            'first_touch_landing_page': 'https%3A//www.make.com/en',
            'gb_anonymous_id': '4d967744-c4b8-41b6-9f90-d802fdb6bd2e',
            'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX1%2FCz9PRIUWfpw55RZZzB90hnV2RmGpzB%2Bc%3D',
            'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX18Buyn6d3%2B%2FZ%2BdkINFvxspfeXihCa3tEmk%3D',
            '_ga': 'GA1.1.1543941994.1716808364',
            'poptin_old_user': 'true',
            'poptin_user_id': '0.83emxpg2gfb',
            'poptin_user_ip': '156.207.60.19',
            'poptin_user_country_code': 'false',
            'poptin_session_account_b242bb2954926': 'true',
            'poptin_c_visitor': 'true',
            '_gcl_au': '1.1.13046725.1716808366',
            '_fbp': 'fb.1.1716808367190.548965802',
            'first_touch_landing_page_query': '%3Fcommunity%3D1%26verified%3D1',
            'OptanonAlertBoxClosed': '2024-05-27T11:12:55.793Z',
            '_hjSessionUser_2919042': 'eyJpZCI6IjgwNmJiZjg5LTY1OTMtNWY5MS1iYjNjLTUwZDQ1ZmU4ZGNlYiIsImNyZWF0ZWQiOjE3MTY4MDgzNjQ4NDcsImV4aXN0aW5nIjp0cnVlfQ==',
            'last_touch_landing_page_query': '',
            'first_touch_referral_url': 'http%3A//localhost%3A8888/',
            'poptin_referrer': '',
            'last_touch_landing_page': 'https%3A//www.make.com/en/integrations/google-sheets',
            'last_touch_referral_url': '',
            'referral_url': '',
            'visitor_id1009662': '179264686',
            'visitor_id1009662-hash': '1519c6c73d563505d3864a715df232c09d12f131ebe0cd353812b4f58d2c6c0d06c659c3e81d67c117cb2ec8215ee459825eaa67',
            '__cf_bm': '1kTgSA4sIMaW0D3T75liMBg5ZxRIxmWW7b_0DF0LTXQ-1716836483-1.0.1.1-uWF4cAaHH6BQEgatTwbESQ__oIBXbWuCkay8YUiPfiswxwA9loQjfPXvLPeWGK76UHod9WxnaSwmJJViQmUFMA',
            'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2BCCgdB42kQJtAjWsRJozHOuk0iMPy5wjQ%3D',
            'rl_trait': 'RudderEncrypt%3AU2FsdGVkX1%2Bg6ToT1Ywws2w%2BLullpd8BXty5QNALWUo%3D',
            'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX1%2BL2H9TPM%2Be8Vf0OFQYEAJWhLtI%2B5n4Yck%3D',
            'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX18SuOz9gHkxMUdJTn7tGaf%2BVJ1xwJfJTe0%3D',
            'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1913wNUN4YLhOjZxyk4j%2FhDA0lqzJLqGyi4MbY0tjnvpaBsv0gKI1T1OtVEbO3Ki%2FCwbyF9ifk89Q%3D%3D',
            'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+May+27+2024+22%3A06%3A41+GMT%2B0300+(Eastern+European+Summer+Time)&version=202306.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=758c16f0-df45-4741-813f-b146c2926d1d&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=EG%3BKN',
            'rl_session': 'RudderEncrypt%3AU2FsdGVkX1%2BehoyhNrQ8XjNmBJS4C20m8ZbMk7WpBM5Z70ZInV8TRDUWJzRewaOErFW5ukLAdpdO%2Fk0HXvujRL6zjo6JnO4HdmCeaS7AIhFY3anWcoWEXDe68pDhruhDa%2BGOA3R8uXmi7rCt4Y4MEw%3D%3D',
            '_ga_MY0CJTCDSF': 'GS1.1.1716836799.6.1.1716836809.50.0.0',
            'make_session_id': '1716836799',
            '_uetsid': '0c5498001c1a11efbdf0954c2b28279f',
            '_uetvid': '0c54bd001c1a11ef99362fa261b0d15d',
            '_hjSession_2919042': 'eyJpZCI6IjY0ZWFhN2JkLTVjYTctNDQ1YS05NTQ0LTQzMmZjMTE1ZGZhOCIsImMiOjE3MTY4MzY4MTYzMDYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
            '_rdt_uuid': '1716808366676.355e1e32-bf41-4c7d-87c5-36507b532296',
            'poptin_session': 'true',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        }

        with requests.Session() as session:
            session.headers.update(headers)
            session.cookies.update(cookies)
            
            self.df['Description'] = self.df.apply(
                lambda row: self.extract_description(session, row['slug'], row['name']),
                axis=1)


    def process_response(self):
        
        self.df = pd.DataFrame(self.entities)
        cols_to_keep = ['Rank', 'Category', 'Name', 'Description', ]
        
    
    def rank(self):
        self.df['Rank'] = self.df.index + 1
    
    def category(self):
        def extract_category(cat_col):
            try:
                cat = cat_col['items'][0]['slug'].title()
            except (IndexError, KeyError):
                cat = "Not specified"
            return cat
        
        cat_col = self.df['categoriesCollection']
        self.df['Category'] = cat_col.apply(extract_category)

    def name(self):
        self.df['Name'] = self.df['name']
        
    def link(self):
        self.df['url'] = "https://www.make.com/en/integrations/" + self.df['slug']
        

    def rank(self):

    def ranking(self):
        """
        Global popularity ranking of the plugin as found in 
        https://www.make.com/en/integrations?community=1&verified=1
        """
        url = "https://www.make.com/en/integrations?community=1&verified=1"
        
        

        """        
        - Category: Categories (separated by a comma) where the plugin can be found (e.g., Google Sheet plugin found in "Productivity" https://www.make.com/en/integrations/category/productivity?community=1&verified=1)
        - Plugin Name: Name of the plugin
        - Plugin Description: Description of the plugin as found when clicking on it (ex: https://www.make.com/en/integrations/google-sheets)
        - Readme : Markdown version of the plugin documentation (e.g., https://www.make.com/en/help/app/google-sheets) -- You can find it in HTML and use an HTML to Markdown converter or use chatgpt
        - Type: Type of action (Action/Trigger/Search/etc.) (ex: https://www.make.com/en/integrations/google-sheets)
        -  Name: Name of the action found on the list of the plugin in make
        -  Description: High-level description of the action
        - Parameter : JSON of all the parameter of the action  as found in the documentation in the correct action (e.g., https://www.make.com/en/help/app/google-sheets#actions-964718)
        """
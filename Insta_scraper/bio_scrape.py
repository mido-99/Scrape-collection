import jmespath
import requests
import json


url = "https://www.instagram.com/leomessi/?hl=en"

class InstaScraper:
    '''Scrape data from about instgram accounts. Expects a list of urls or single url.\n
    
    Typical use:\n
    : Construct an <InstaScraper> obj from url: insta = InstaScraper(url=url)\n
    Available data for export:\n
    - General profile data: insta.export_profile_data_json(): general info like name, 
    bio, bio urls, followers, following, etc..\n
    
    
    
    '''
    
    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-ig-app-id': '936619743392459',
    }

    def __init__(self, urls):
        if isinstance(urls, str):    # Since all the logic of the class works on lists
            self.urls = [urls]
        elif isinstance(urls, (list, set, tuple)):
            self.urls = urls
        else:
            raise Exception("Unsupported DataType passed! Expects either str, list, dict, tuple or set.")
    
    def construct_profile_api_url(self, url):
        '''Construct api url from the username in the link passed by user
        '''

        username = url.split('/')[3]
        api_url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}&hl=en"
        return api_url

    def request_profile_api(self):
        '''Sends requests to instgram endpoint api that sends us back all data\n
        Returns a generator for each url's data
        '''
        
        for url in self.urls:
            url = self.construct_profile_api_url(url)
            response = requests.get(url, headers=self.headers)
            if response.status_code == 400:
                raise Exception("HTTP status code 400. Request Blocked!")
            else:
                print(f'Successful request: {url}')
            
            yield response.json()['data']['user']
        
    def parse_profile_data(self):
        '''Parse profile general data returned by api into more organized form
        '''

        for data in self.request_profile_api():
            result = jmespath.search(                
                '''{
                name: full_name,
                username: username,
                bio: biography,
                bio_links: bio_links[].url,
                category: category_name,
                followers: edge_followed_by.count,
                follows: edge_follow.count,
                posts: edge_owner_to_timeline_media.count,
                profile_pic_url: profile_pic_url_hd,
                private: is_private,
                verified: is_verified,
                business_account: is_business_account,
                joined_recently: is_joined_recently
                }''', data)
            yield result

    def export_profile_data_json(self):
        '''Export instgram profile general data as json file
        '''
        
        for result in self.parse_profile_data():
            username = result['username']
            print(f"Exporting to {username}.json")
            with open(f"{username}.json", 'w') as j:
                json.dump(result, j)


insta = InstaScraper(url)
insta.export_profile_data_json()

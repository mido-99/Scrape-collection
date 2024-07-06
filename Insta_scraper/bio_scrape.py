import jmespath
import requests
import json


class InstaProfile:
    '''Scrape instagram accounts data. This class has 2 main uses: 
    - To get main profile data
    - Data about all user posts
    ## Usage:
    ### Profile data
    - Construct an <InstaProfile> obj from url:\n
    insta = InstaProfile(https://www.instagram.com/world_record_egg)\n
    (It accepts instagram usernames too)\n
    - Get profile data like bio & bio links, followers & following, number
    & more..:\n
    data = insta.get_profile()
    - Export general profile data 
    insta.export_profile_data_json(data)

    '''
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-asbd-id': '129477',
        'x-ig-app-id': '936619743392459',
        'cookie': '''csrftoken=cpBvgDRGLIQ4j3RgScGvH24w9R6cQffX; ds_user_id=18519728814; ps_n=1; ps_l=1; mid=Zl0FuQALAAHWLneH1O51KnPmZbQO; ig_did=8F185B9B-0018-4D2C-9C8B-5861E8826960; dpr=0.8640000224113464; datr=fid7ZoVfi9JAdPRsF4AUt5H9; shbid="19508\05418519728814\0541751227322:01f71e1583bc74deb0cf35aadeef14cbf22516af31cc981c85d6a595394c0fc9c9797cbb"; shbts="1719691322\05418519728814\0541751227322:01f797a9ebf1355c2fe47a789c2fca5f528433508e5c351bbb67dc69bcb3920b918ea3d3"; sessionid=18519728814%3A8CptQEBMl6lstb%3A29%3AAYfPHfaU0TD5O2F2otwE2BteTZDIh3lS8N5qbid1QQ; rur="RVA\05418519728814\0541751409798:01f7914db0d124d7da5a7af3e8dbeca4c2fc69e72380836ba0862459726e5ae2d6f8640f"; wd=1582x268'''
        }

    def __init__(self, url):
        self.url = url if 'https' in url else f"https://www.instagram.com/{url}"
        self.username = self.url.split('/')[3]
        
    
    def get_profile(self):
        ''' Scrape an instagram profile, returns useful data like: \n
        id, bio links, business or not, follow & followers numbers, & more..
        '''
        
        profile_api = self._construct_profile_api_url()
        user_data = self._request_profile_api(profile_api)
        parsed_data = self._parse_profile_data(user_data)
        return parsed_data

    def _construct_profile_api_url(self):
        '''Construct api url from the username in the link passed by user
        '''

        profile_api = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={self.username}&hl=en"
        return profile_api

    def _request_profile_api(self, profile_api):
        '''Sends requests to instgram endpoint api that sends us back all data\n
        Returns a generator for each url's data
        '''
        
        response = requests.get(profile_api, headers=self.headers)
        if response.status_code != 200:
            raise Exception(f"HTTP status code {response.status_code}. Request Failed!")
        else:
            print(f'Successful request: {url}')
            
        return response.json()['data']['user']
        
    def _parse_profile_data(self, user_data):
        '''Parse profile general data returned by api into more organized form
        '''

        result = jmespath.search(
            """{
            name: full_name,
            username: username,
            id: id,
            category: category_name,
            business_category: business_category_name,
            phone: business_phone_number,
            email: business_email,
            bio: biography,
            bio_links: bio_links[].url,
            homepage: external_url,        
            followers: edge_followed_by.count,
            follows: edge_follow.count,
            facebook_id: fbid,
            is_private: is_private,
            is_verified: is_verified,
            profile_image: profile_pic_url_hd,
            video_count: edge_felix_video_timeline.count,
            videos: edge_felix_video_timeline.edges[].node.{
                id: id, 
                title: title,
                shortcode: shortcode,
                thumb: display_url,
                url: video_url,
                views: video_view_count,
                tagged: edge_media_to_tagged_user.edges[].node.user.username,
                captions: edge_media_to_caption.edges[].node.text,
                comments_count: edge_media_to_comment.count,
                comments_disabled: comments_disabled,
                taken_at: taken_at_timestamp,
                likes: edge_liked_by.count,
                location: location.name,
                duration: video_duration
            },
            image_count: edge_owner_to_timeline_media.count,
            images: edge_felix_video_timeline.edges[].node.{
                id: id, 
                title: title,
                shortcode: shortcode,
                src: display_url,
                url: video_url,
                views: video_view_count,
                tagged: edge_media_to_tagged_user.edges[].node.user.username,
                captions: edge_media_to_caption.edges[].node.text,
                comments_count: edge_media_to_comment.count,
                comments_disabled: comments_disabled,
                taken_at: taken_at_timestamp,
                likes: edge_liked_by.count,
                location: location.name,
                accesibility_caption: accessibility_caption,
                duration: video_duration
            },
            saved_count: edge_saved_media.count,
            collections_count: edge_saved_media.count,
            related_profiles: edge_related_profiles.edges[].node.username
            }""", user_data)
        self._set_user_id(result)    
        return result
    
    def _set_user_id(self, parsed_data):
        '''Fetche user id (instagram internal id)'''
        self.id = parsed_data['id']

    def export_profile_data_json(self, profile_data):
        '''Export instgram profile data into json file.\n
        Expects the data in format returned by this class method: get_profile()
        '''
        
        print(f"Exporting to {self.username}.json")
        with open(f"{self.username}.json", 'w') as j:
            json.dump(profile_data, j, indent=2)
    
    def get_all_posts(self, username, session, max_pages: int =1, page_size = 12):
        
        username = username or self.username
        with requests.Session as session:
            session.headers.update(self.headers)

            _page_num = 1
            while _page_num >= max_pages:
                # Variables for each posts page
                variables = {'data': {'count': page_size,
                    'include_relationship_info': True,
                    'latest_besties_reel_media': True,
                    'latest_reel_media': True},
                    'username': username,
                    '__relay_internal__pv__PolarisFeedShareMenurelayprovider': False
                }
                data = {
                    'variables': json.dumps(variables),
                    'doc_id': '8721952884485930',
                }
                resp_json = self._request_all_posts_graphql(session, data=data)
                # Handle posts
                posts = resp_json['data']['xdt_api__v1__feed__user_timeline_graphql_connection']['edges']
                print(f'Scraping {len(posts)} posts on page: {_page_num}')
                

                # Handle pagination
                if not resp_json['page_info']['has_next_page']:
                    break
                variables['data']['after'] = resp_json['page_info']['end_cursor']
                
                _page_num += 1
    
    def _request_all_posts_graphql(self, session, data):
        
        response = session.post('https://www.instagram.com/graphql/query', headers=self.headers, data=data)
        if response.status_code != 200:
            raise Exception(f"HTTP status code {response.status_code}. Request Failed!")        
        return response.json()['data']['xdt_api__v1__feed__user_timeline_graphql_connection']
    
    def _parse_post(self, post):
        
    



if __name__ == '__main__':
    
    url = "https://www.instagram.com/leomessi/?hl=en"
    url = "https://www.instagram.com/cristiano/?hl=en"
    url = "https://www.instagram.com/world_record_egg"

    insta = InstaProfile(url)
    data = insta.get_profile()
    insta.export_profile_data_json(data)

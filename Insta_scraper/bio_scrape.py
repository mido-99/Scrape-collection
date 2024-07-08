import jmespath
import requests
import json
from dotenv import get_variable


class InstaProfile:
    '''Scrape instagram accounts data. This class has 2 main uses: 
    - To get main profile data
    - Data about all user posts
    # Usage:
    - Construct an <InstaProfile> obj from url:\n
    (It accepts an instagram username too)\n
    ```
    insta = InstaProfile(https://www.instagram.com/world_record_egg)
    ```
    ### Profile data
    - Get profile data like bio text & bio links, followers & following, number
    & more..:\n
    - Export data into .json\n
    ```
    data = insta.get_profile()
    insta.export_profile_data_json(data)
    ```
    ### All user's posts
    - Get general data about all user's posts like caption, likes, comment count, image or video url if present.\n
    - Export data into .json\n
    ``` 
    posts = insta.get_all_posts(2, 14)
    insta.export_user_posts_json(posts)
    ```
    '''
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-asbd-id': '129477',
        'x-ig-app-id': '936619743392459',
        'cookie': get_variable('.env', 'cookie')
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
        with open(f"{self.username}.json", 'w') as f:
            json.dump(profile_data, f, indent=2, ensure_ascii=False)
    
    def get_all_posts(self, max_pages: int =1, page_size = 12):
        
        all_posts = []
        with requests.Session() as session:
            session.headers.update(self.headers)

            _page_num = 1
            while _page_num <= max_pages:
                # Variables for each posts page
                variables = {'data': {'count': page_size,
                    'include_relationship_info': True,
                    'latest_besties_reel_media': True,
                    'latest_reel_media': True},
                    'username': self.username,
                    '__relay_internal__pv__PolarisFeedShareMenurelayprovider': False
                }
                data = {
                    'variables': json.dumps(variables),
                    'doc_id': '8721952884485930',
                }
                resp_json = self._request_all_posts_graphql(session, data=data)

                # Handle posts
                posts = resp_json['edges']
                print(f'Scraping {len(posts)} posts on page: {_page_num}')
                all_posts.extend(self._parse_post(post) for post in posts)
                
                # Handle pagination
                if not resp_json['page_info']['has_next_page']:
                    break
                variables['data']['after'] = resp_json['page_info']['end_cursor']
                _page_num += 1
        return all_posts
    
    def _request_all_posts_graphql(self, session, data):

        response = session.post('https://www.instagram.com/graphql/query', headers=self.headers, data=data)
        if response.status_code != 200:
            raise Exception(f"HTTP status code {response.status_code}. Request Failed!")        
        return response.json()['data']['xdt_api__v1__feed__user_timeline_graphql_connection']
    
    def _parse_post(self, post):
        
        parsed_data = jmespath.search('''
            node.{
                id: id,
                url: code,
                caption: caption.{
                    text: text,
                    created_at: created_at,
                    has_translation: has_translation,
                    edited: caption_is_edited
                },
                media_type: media_type,
                image: image_versions2.candidates[0].url
                video: video_versions[0].url,
                is_paid: is_paid_partnership,
                sponsors: sponsor_tags,
                dimensions: [original_height, original_width],
                comment_count: comment_count,
                comments_disabled: comments_disabled,
                like_count: like_count,
                top_likers: top_likers,
                has_audio: has_audio
            }''', post)
        parsed_data['url'] = f"https://instagram.com/p/{parsed_data['url']}/?hl=en"
        parsed_data['media_type'] = 'video' if parsed_data['media_type'] == 2 else 'image'
        return parsed_data
    
    def export_user_posts_json(self, posts):

        print(f"Exporting to {self.username}_posts.json")
        with open(f'{self.username}_posts.json', 'w', encoding='utf-8') as f:
            json.dump(posts, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    
    url = "https://www.instagram.com/leomessi/?hl=en"
    url = "https://www.instagram.com/cristiano/?hl=en"
    url = "https://www.instagram.com/world_record_egg"

    insta = InstaProfile(url)
    # User Profile
    # data = insta.get_profile()
    # insta.export_profile_data_json(data)
    
    # All User Posts
    posts = insta.get_all_posts(2, 14)
    insta.export_user_posts_json(posts)

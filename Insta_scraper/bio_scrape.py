import jmespath
import requests
import json


class InstaProfile:
    '''Scrape general data about instgram accounts. Expects a single profile url.\n
    
    Typical use:\n
    : Construct an <InstaScraper> obj from url: insta = InstaScraper(url=url)\n
    Available data for export:\n
    - General profile data: insta.export_profile_data_json(): general info like name, 
    bio, bio urls, followers, following, etc..\n
    
    '''
    
    def __init__(self, url):
        self.url = url
    
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
        
        headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-asbd-id': '129477',
        'x-ig-app-id': '936619743392459',
        }
        api_url = self.construct_profile_api_url(self.url)
        response = requests.get(api_url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"HTTP status code {response.status_code}. Request Failed!")
        else:
            print(f'Successful request: {url}')
            
        return response.json()['data']['user']
        
    def parse_profile_data(self):
        '''Parse profile general data returned by api into more organized form
        '''

        data = self.request_profile_api()
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
            }""", data)
        return result

    def export_profile_data_json(self):
        '''Export instgram profile general data as json file
        '''
        
        result = self.parse_profile_data()
        username = result['username']
        print(f"Exporting to {username}.json")
        with open(f"{username}.json", 'w') as j:
            json.dump(result, j, indent=2)


url = "https://www.instagram.com/leomessi/?hl=en"
url = "https://www.instagram.com/cristiano/?hl=en"

insta = InstaProfile(url)
insta.export_profile_data_json()

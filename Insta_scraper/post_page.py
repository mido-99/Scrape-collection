import json
from urllib.parse import quote
import httpx
import jmespath


class InstaPost:
    
    def __init__(self, post_url):
        self.post_url = post_url
        
    def request_post_api(self, post_url):
        """Scrape single Instagram post data"""
        
        shortcode = post_url.split('/p/')[-1].split('/')[0] if 'http' in post_url else post_url
        self.shortcode = shortcode
        print(f"Scraping: {shortcode}")
        
        graph_api = "https://www.instagram.com/graphql/query/?query_hash=b3055c01b4b222b8a47dc12b090e4e64&variables="
        variables = {
            "shortcode": shortcode,  # post shortcode (from URL)
            "child_comment_count": 20,  
            "fetch_comment_count": 100,
            "parent_comment_count": 30,
            "has_threaded_comments": True
            }
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'x-asbd-id': '129477',
            'x-ig-app-id': '936619743392459',
            'cookie': '''csrftoken=cpBvgDRGLIQ4j3RgScGvH24w9R6cQffX; ds_user_id=18519728814; ps_n=1; ps_l=1; mid=Zl0FuQALAAHWLneH1O51KnPmZbQO; ig_did=8F185B9B-0018-4D2C-9C8B-5861E8826960; dpr=0.8640000224113464; datr=fid7ZoVfi9JAdPRsF4AUt5H9; shbid="19508\05418519728814\0541751227322:01f71e1583bc74deb0cf35aadeef14cbf22516af31cc981c85d6a595394c0fc9c9797cbb"; shbts="1719691322\05418519728814\0541751227322:01f797a9ebf1355c2fe47a789c2fca5f528433508e5c351bbb67dc69bcb3920b918ea3d3"; sessionid=18519728814%3A8CptQEBMl6lstb%3A29%3AAYfPHfaU0TD5O2F2otwE2BteTZDIh3lS8N5qbid1QQ; rur="RVA\05418519728814\0541751409798:01f7914db0d124d7da5a7af3e8dbeca4c2fc69e72380836ba0862459726e5ae2d6f8640f"; wd=1582x268'''
            }
        
        quoted_vars = quote(json.dumps(variables))
        final_url = graph_api + quoted_vars
        response = httpx.get(final_url, headers=headers)
        assert response.status_code == 200
        return response.json()['data']['shortcode_media']
    
    def scrape_post(self):
        data = self.request_post_api(self.post_url)
        parsed_data = jmespath.search(
            '''{
                id: id,
                shortcode: shortcode,
                dimentions: dimentions,
                url: shortcode,
                src_attached: edge_sidecar_to_children.edges[].node.display_url,
                has_audio: has_audio,
                video_url: video_url,
                views: video_view_count,
                plays: video_play_count,
                likes: edge_media_preview_like.count,
                location: location.name,
                taken_at: taken_at_timestamp,
                related: edge_web_media_to_related_media.edges[].node.shortcode,
                type: product_type,
                video_duration: video_duration,
                music: clips_music_attribution_info,
                is_video: is_video,
                tagged_users: edge_media_to_tagged_user.edges[].node.user.username,
                captions: edge_media_to_caption.edges[].node.text,
                related_profiles: edge_related_profiles.edges[].node.username,
                comments_count: edge_media_to_parent_comment.count,
                comments_disabled: comments_disabled,
                comments_next_page: edge_media_to_parent_comment.page_info.end_cursor,
                comments: edge_media_to_parent_comment.edges[].node.{
                    id: id,
                    text: text,
                    created_at: created_at,
                    viewer_has_liked: viewer_has_liked,
                    likes: edge_liked_by.count
                    owner: owner.{
                        username: username
                        is_verified: is_verified,
                        profile_pic: profile_pic_url
                    }
                }
                }''', data)
        parsed_data['url'] = f"https://instagram.com/p/{parsed_data['url']}/?hl=en"
        return parsed_data
    
    def export_data_json(self):
        
        result = self.scrape_post()
        print(f"Exporting to {self.shortcode}.json")
        with open(f"{self.shortcode}.json", 'w', encoding='utf-8') as j:
            json.dump(result, j, indent=2, ensure_ascii=False)


post_url = "https://www.instagram.com/p/C8djxnMiM9P/?hl=en&img_index=1"
insta = InstaPost(post_url)
insta.export_data_json()
'''This file is completely different from user_crawler.
Here users names are scraped on 2 stages.
First courses are obtained from an endpoint api, these data contain info about 
each course (fortunately we have course url!).
Then after visiting each course page, user link is obtained.
'''
from urllib.parse import parse_qs, urlparse, urlencode, urlunparse
import requests
import undetected_chromedriver as uc
from bs4 import BeautifulSoup


url = "https://www.udemy.com/api-2.0/discovery-units/all_courses/?p=1&page_size=48&subcategory=&instructional_level=&lang=&price=&duration=&closed_captions=&subs_filter_type=&category_id=300&source_page=category_page&locale=en_US&currency=egp&navigation_locale=en_US&skip_price=true&sos=pc&fl=cat"
url_no_p = "https://www.udemy.com/api-2.0/discovery-units/all_courses/?page_size=16&subcategory=&instructional_level=&lang=&price=&duration=&closed_captions=&subs_filter_type=&category_id=300&source_page=category_page&locale=en_US&currency=egp&navigation_locale=en_US&skip_price=true&sos=pc&fl=cat"

class UdemyUsersScraper():
    
    def __init__(self, url):
        self.url = url
        
    def validate_query(self, url):
        '''Validates that the url is passed in correct scheme. First page urls don't
        have 'p' params.'''

        parsed_url = urlparse(url)
        query = parse_qs(parsed_url.query)
        if 'p' not in query:
            query['p'] = ['1']
            query['page_size'] = ['48']
        else:
            curr_page = int(query['p'][0])
            query['p'] = [f"{curr_page + 3}"]
        
        new_query = urlencode(query, doseq=True)
        new_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, new_query, parsed_url.fragment))
        return new_url
    
    def get_api_data(self):
        '''Retrieves data by endpoint api. Can retrieve 16 result per page (default) 
        or up to 60. For efficacy and ability to devide by 16; 48 will be used'''
        
        new_url = self.validate_query(self.url)
        r = requests.get(new_url)
        #! Add exception for no more pages, and 16 default items if 48 was rejected
        
    
    
    def check_duplicates(self):
        '''Check for duplicate users before making a request to course page.'''

        pass
    
    def get_course_urls(self):
        '''Get courses urls from api endpoint -rather than making hundreds of requests-.'''

        pass
    
    def get_user_data(self):
        '''Get final user data from their page'''
        
        pass
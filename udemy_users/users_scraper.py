'''This file is completely different from user_crawler.
Here users names are scraped on 2 stages.
First courses are obtained from an endpoint api, these data contain info about 
each course (fortunately we have course url!).
Then after visiting each course page, user link is obtained.
'''
import undetected_chromedriver as uc
from bs4 import BeautifulSoup


class UdemyUsersScraper():
    
    def __init__(self):
        pass
    
    def get_api_data(self, url):
        '''Retrieves data by endpoint api. Can retrieve 16 result per page (default) 
        or up to 60. For efficacy and ability to devide by 16; 48 will be used'''
        
        pass
    
    def check_duplicates(self):
        '''Check for duplicate users before making a request to course page.'''

        pass
    
    def get_course_urls(self):
        '''Get courses urls from api endpoint -rather than making hundreds of requests-.'''
        
        pass
    
    def get_user_data(self):
        '''Get final user data from their page'''
        
        pass
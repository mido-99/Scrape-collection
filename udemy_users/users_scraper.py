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


class UdemyUsersScraper():
    """Extract all users page urls from a categoty on udemy.com. 
    #TODO: add main params & main method instructions"""

    BASE_SITE = "https://www.udemy.com/"
    
    def __init__(self, api):
        self.api = api
        
    def validate_query(self, api):
        '''Validates that the url is passed in correct scheme. First page urls don't
        have 'p' params.'''

        parsed_url = urlparse(api)
        query = parse_qs(parsed_url.query)
        if 'p' not in query:    #First page; first time setting valuew
            query['p'] = ['1']
            query['page_size'] = ['48']
        else:                   #changing page number
            curr_page = int(query['p'][0])
            query['p'] = [f"{curr_page + 3}"]

        return self.re_construct_url(query, parsed_url)

    def set_query(self, api, p: int, page_size:int):
        '''Sets the value of p (page) and page_size (itmes) in the api url'''

        parsed_url = urlparse(api)
        query = parse_qs(parsed_url.query)
        query['p'] = [f'{p}']
        query['page_size'] = [f'{page_size}']
        return self.re_construct_url(query, parsed_url)
    
    def re_construct_url(self, query, parsed_url):
        '''Reconstruct a full url out of its parts made by urllic.parse.urlparse()'''

        new_query = urlencode(query, doseq=True)
        new_url = urlunparse(
            (
                parsed_url.scheme,
                parsed_url.netloc,
                parsed_url.path,
                parsed_url.params,
                new_query,
                parsed_url.fragment,
            )
        )
        return new_url

    def get_api_data(self, pages:int):
        '''Retrieves data by endpoint api. Can retrieve 16 result per page (default) 
        or up to 60. For efficacy and ability to devide by 16; 48 will be used.\n
        Expects number of pages in category being scraped.'''
        
        all_users = []    #all courses; populated on each request
        all_requests, remainder = divmod(pages, 3) #requests to be made initially, remaining pages
        #*1 The idea of // and % below
        
        for _ in range(all_requests): 
            url = self.validate_query(self.api)
            r = requests.get(url).json()
            users = [r['unit']['items'][i]['visible_instructors'][0]['url']
                    for i in range(len(r['unit']['items']))]
            all_users.extend(users)

        for _ in range(remainder):  
            url = self.set_query(self.api, (all_requests*3) + 1, 16)    #req_made*3 = curr_page
            r = requests.get(url).json()
            users = [r['unit']['items'][i]['visible_instructors'][0]['url']
                    for i in range(len(r['unit']['items']))]
            all_users.extend(users)
            reqs +=1
        return set(all_users) #A set to drop duplicates
        
    def get_user_data(self):
        '''Get final user data from their page'''
        
        pass

example_cat = "https://www.udemy.com/courses/teaching-and-academics/"
api = "https://www.udemy.com/api-2.0/discovery-units/all_courses/?p=1&page_size=48&subcategory=&instructional_level=&lang=&price=&duration=&closed_captions=&subs_filter_type=&category_id=300&source_page=category_page&locale=en_US&currency=egp&navigation_locale=en_US&skip_price=true&sos=pc&fl=cat"
api_no_p = "https://www.udemy.com/api-2.0/discovery-units/all_courses/?page_size=16&subcategory=&instructional_level=&lang=&price=&duration=&closed_captions=&subs_filter_type=&category_id=300&source_page=category_page&locale=en_US&currency=egp&navigation_locale=en_US&skip_price=true&sos=pc&fl=cat"

teaching = UdemyUsersScraper(api = api_no_p)
teaching.get_api_data(7)

"""
#*1 The thing behind // and %
We initially devide the whole p number by 3 giving us a right number
say 10 pages; so 10 // 3 = 3
so 3 reqs to be made as each req brings data from 3 pages
now we have some remaining which is 10 % 3 = 1
so another 1 req is made WITH default query aka: page_size=16&p= correct p

"""
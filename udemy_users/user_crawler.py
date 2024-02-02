from bs4 import BeautifulSoup
import re
from collections import deque
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc
# from logTOtxt import setup_logging


# options.add_argument('--headless')
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

class UdemyUsers():
    '''Crawls internal links of udemy searching for users pages'''    
    
    def __init__(self, startURL: str):
        self.startURL = startURL
        self.pages_visited = set()   #Filled with pages that have been visited
        self.users = set()   #Users pages only
        self.queue = deque()   #list-like object; with the ability to add & remove at both ends
        options= uc.ChromeOptions()
        options.add_argument('--log-level=3')  # Set log level to ignore console errors
        self.driver = uc.Chrome(options, use_subprocess=True)


    def find_links(self):
        '''Find all elems with 'a' tag aka: links in a page'''

        currURL = self.queue.popleft()
        print(f"GETTING link: {currURL}")
        self.driver.get(currURL)
        # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="https://www.udemy.com"]')))

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        links = soup.find_all('a')
        return links

    def classify_link(self, links: list):
        '''Cllassify links to internal, users pages, or other non-useful, 
        depending on a regex pattern'''
        
        
        for link in links:     #For each link (a Tag)
            if 'href' in link.attrs and link.attrs['href'] not in self.pages_visited:
                new_page = link.attrs['href']
                print(new_page)

                UserLinkCriteria = [
                    re.compile(r"(https://www.udemy.com)?/user/.*").match(new_page), 
                    new_page not in self.users,
                ]
                InternalLinkCriteria = [
                    re.compile(r"udemy.com/.*").search(new_page),
                ]
        #! UNWANTED matches sometimes like www.instagram/udemy.com --> FIX using urlparse netloc in IntLinks
                
                if all(InternalLinkCriteria):
                    if all(UserLinkCriteria):  #New User page
                        self.users.add(new_page)
                        print(self.users)
                        with open('users.txt', 'a') as f:
                            f.writelines(url + '\n' for url in self.users)
                    else:
                        self.queue.append(new_page)  #Internal links searched again for probable user links
                        print(f"To queue: {new_page}")
                    
                self.pages_visited.add(new_page)     #Pages are marked visited 
                print(f'To pages_visited: {new_page}')

                print(f"Current sizes - pages_visited: {len(self.pages_visited)},"
                    f"users: {len(self.users)}, queue: {len(self.queue)}")

    def crawl_users(self):
        '''Main Class Method'''

        self.queue.append(self.startURL)
        while self.queue:    #While there's still pages not crawled
            links = self.find_links()
            self.classify_link(links)
            
        self.driver.quit()


# import logging
# setup_logging('script_log.txt')
# logging.info('This is an informational message.')
# logging.warning('This is a warning message.')

# url = "https://about.udemy.com/category/instructors/"
url = 'https://about.udemy.com/instructors/supercharge-your-delivery-6-tips-to-improve-your-on-camera-presence/'

crawler = UdemyUsers(url)
crawler.crawl_users()

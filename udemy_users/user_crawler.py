from bs4 import BeautifulSoup
import re
from collections import deque
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc
# from logTOtxt import setup_logging


options= uc.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
options.add_argument('--log-level=3')  # Set log level to ignore console errors
driver = uc.Chrome(options, use_subprocess=True)

pages_visited = set()   #Filled with pages that have been visited
users = set()   #Users pages only
queue = deque()   #list-like object; with the ability to add & remove at both ends


def find_links(driver):
    '''Find all elems with 'a' tag aka: links in a page'''

    global queue
    currURL = queue.popleft()
    print(f"GETTING link: {currURL}")
    driver.get(currURL)
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="https://www.udemy.com"]')))

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    links = soup.find_all('a')
    return links

def classify_link(links: list):
    '''Cllassify links to internal, users pages, or other non-useful, 
    depending on a regex pattern'''

    for link in links:     #For each link (a Tag)
        if 'href' in link.attrs and link.attrs['href'] not in pages_visited:
            new_page = link.attrs['href']
            print(new_page)
            
            #! UNWANTED matches sometimes like www.instagram/udemy.com --> FIX using urlparse netloc
            if re.compile(r"udemy.com/.*").search(new_page):
                if re.compile(r"(https://www.udemy.com)?/user/.*").match(new_page) \
                    and new_page not in users:  #New User page
                    users.add(new_page)
                    print(users)
                    with open('users.txt', 'a') as f:
                        f.writelines(url + '\n' for url in users)
                else:
                    queue.append(new_page)  #Internal links searched again for probable user links
                    print(f"To queue: {new_page}")
                
            pages_visited.add(new_page)     #Pages are marked visited 
            print(f'To pages_visited: {new_page}')

            print(f"Current sizes - pages_visited: {len(pages_visited)},"
                f"users: {len(users)}, queue: {len(queue)}")


def crawl_users(startURL: str, driver: uc.Chrome):
    '''Crawls internal links of udemy searching for users pages'''
    
    global queue
    queue.append(startURL)
    while queue:    #While there's still pages not crawled
        links = find_links(driver)
        classify_link(links)
        
    driver.quit()


import logging

# setup_logging('script_log.txt')
# logging.info('This is an informational message.')
# logging.warning('This is a warning message.')

# url = "https://about.udemy.com/category/instructors/"
url = 'https://about.udemy.com/instructors/supercharge-your-delivery-6-tips-to-improve-your-on-camera-presence/'
crawl_users(url, driver)

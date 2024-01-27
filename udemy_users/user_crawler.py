from bs4 import BeautifulSoup
import re
from collections import deque
from selenium import webdriver
from time import sleep
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import undetected_chromedriver as uc
from logTOtxt import setup_logging


options= uc.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
options.add_argument('--log-level=3')  # Set log level to ignore console errors

pages_visited = set()   #Filled with pages that have been visited
users = set()   #Users pages only


def crawl_users(startURL: str):
    '''Crawls internal links of udemy searching for users pages'''
    
    driver = uc.Chrome(options, use_subprocess=True)
    wait = WebDriverWait(driver, 5)
    queue = deque([startURL])   #list-like object; with the ability to add & remove elems at both ends
    while queue:    #While there's still pages not crawled
        
        currURL = queue.popleft()
        print(f"GETTING link: {currURL}")
        driver.get(currURL)
        # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="https://www.udemy.com"]')))
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        links = soup.find_all('a')
        for link in links:     #For each link (a Tag)
            if 'href' in link.attrs and link.attrs['href'] not in pages_visited:
                new_page = link.attrs['href']
                print(new_page)
                
                if re.compile(r"udemy.com/.*").search(new_page):
                    if re.compile(r"(https://www.udemy.com)?/user/.*").match(new_page) \
                        and new_page not in users:  #New User page
                        users.add(new_page)
                        print(users)
                    else:
                        queue.append(new_page)  #Internal links searched again for probable user links
                        print(f"To queue: {new_page}")
                    
                pages_visited.add(new_page)     #Pages are marked visited 
                print(f'To pages_visited: {new_page}')

                print(f"Current sizes - pages_visited: {len(pages_visited)}, users: {len(users)}, queue: {len(queue)}")
        # n += 1

    driver.quit()
    print(queue)


import logging

setup_logging('script_log.txt')
logging.info('This is an informational message.')
logging.warning('This is a warning message.')

# url = "https://about.udemy.com/category/instructors/"
url = 'https://about.udemy.com/instructors/supercharge-your-delivery-6-tips-to-improve-your-on-camera-presence/'
crawl_users(url)

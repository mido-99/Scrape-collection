from bs4 import BeautifulSoup
import re
from collections import deque
from selenium import webdriver
from time import sleep
from selenium.webdriver import ChromeOptions


options = ChromeOptions()
# options.add_argument('--headless')

pages = set()

def crawl_users(startURL: str):
    driver = webdriver.Chrome(options=options)
    
    queue = deque([startURL])
    while queue:
        currURL = queue.popleft()
        driver.get(currURL)
        sleep(.2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        for link in soup.find_all('a'):
            if 'href' in link.attrs and link.attrs['href'] not in pages:
                new_page = link.attrs['href']
                print(new_page)
                pages.add(new_page)
                queue.append(new_page)
    driver.close()

# url = "https://about.udemy.com/category/instructors/"
url = 'https://about.udemy.com/instructors/udemy-instructor-spotlight-amani-abbas/'
crawl_users(url)
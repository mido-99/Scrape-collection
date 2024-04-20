from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import sys
import csv


BASE_URL = 'https://assessment.winnipeg.ca/AsmtTax/English/Propertydetails/default.stm'
STREET_NUM, STREET_NAME = sys.argv[1:]
# args refer to street num, name respectively that will be added from cmd

# Setting up driver
options = ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options)
driver.implicitly_wait(5)

# Search for street
driver.get(BASE_URL)
street_num = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'StreetNumber')))
street_num.send_keys(str(STREET_NUM))
street_name = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'StreetName')))
street_name.send_keys(str(STREET_NAME))
search_address = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'SubmitAddress')))
search_address.click()

# parse html
doc = driver.page_source
soup = BeautifulSoup(doc, 'html.parser')

# prepare data
propHeader = soup.find('table', {'id': 'propSubheader'})

# Main data
title = propHeader.find('h3').text
roll_num = int(propHeader.find('h3').next_sibling.text.split(':')[1].strip())
print(title, '\n', roll_num)

# Extras
extra_tds = propHeader.select('#propSubheader tr:nth-of-type(n+2) td')
for td in extra_tds:
    head = td.find("b").text or 'Extra'     # Head item
    value = ''.join(td.find_all(string=True, recursive=False)).strip() or td.text.strip()   # value
    # print(f'Head: {head}')
    # print(f"Value: {value}")

# Export data
# with open('out.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
    
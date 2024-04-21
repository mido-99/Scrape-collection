from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import sys
import csv
from itertools import zip_longest


BASE_URL = 'https://assessment.winnipeg.ca/AsmtTax/English/Propertydetails/default.stm'
# STREET_NUM, STREET_NAME = sys.argv[1:]
STREET_NUM, STREET_NAME = 412, 'marion'
# STREET_NUM, STREET_NAME = 5, 'good'
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
street_name.send_keys(STREET_NAME)
search_address = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'SubmitAddress')))
search_address.click()

# parse html
doc = driver.page_source
soup = BeautifulSoup(doc, 'html.parser')

# prepare data
propHeader = soup.find('table', {'id': 'propSubheader'})
Headers = ['Title', "Roll Number"]
All_Data = []

# Main data
title = propHeader.find('h3').text
roll_num = int(propHeader.find('h3').next_sibling.text.split(':')[1].strip())
All_Data.append(title)
All_Data.append(roll_num)


# Extras
extra_tds = propHeader.select('#propSubheader tr:nth-of-type(n+2) td')
for td in extra_tds:
    head = td.find("b").text or 'Extra'     # Head item
    value = ''.join(td.find_all(string=True, recursive=False)).strip() or td.text.strip()   # fincal text
    Headers.append(head)
    All_Data.append(value)

# Data Tables
tables = soup.find_all('table', {'class': "tblAlign"})
#NOTE The first 2 tables are fixed 3 columns, Then there might be 1 or 2 tables with 2 columns
# # So we'll have a little different logic for each of 1st, 2nd, other tables

for table in tables[:2]:
    section_title = table.find('th', {'class': "sectiontitle"}).text
    section_headers = table.select('tr:nth-child(2) > th')
    section_data = table.select('tr:nth-child(3) > td')
    for i in range(len(section_headers)):
        head = f"{section_headers[i].text.strip()} {section_title}"
        Headers.append(head)
        All_Data.append(section_data[i].text.strip())


for table in tables[2:]:
    section_title = table.select('tbody > tr:nth-child(1)')[0].text
    section_data = table.select('tbody > tr')[1:]
    section_data = [data for data in section_data if not data.attrs]    # Exclude hidden rows that has no data
                                                                        # (I noticed data rows have no attrs)
    for data in section_data:   # iterate over rows dividing item from value
        item = data.select('th')[0].text.strip()
        value = data.select('td')[0].text.strip()
        Headers.append(item)
        All_Data.append(value)
        #! Split words in last table's row ex: Bus RouteHeavy TrafficExternal Corner

for x, y in zip_longest(Headers, All_Data):
    print(f"{x} ---> {y}")


# Export data
# with open('out.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
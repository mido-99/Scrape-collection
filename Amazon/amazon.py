import requests
from bs4 import BeautifulSoup


url = "https://www.amazon.sa/-/en/Apple-20W-USB-C-Power-Adapter/dp/B08L85KDV5/ref=zg_bs_g_electronics_d_sccl_1/260-1454209-2227524?psc=3"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.find_element(By.C)
driver.find_elements()
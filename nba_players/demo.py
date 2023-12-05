import requests
from bs4 import BeautifulSoup
import pandas as pd


df = pd.DataFrame() # Master Df
    
url = 'https://hoopshype.com/salaries/players/2021-2022/'

resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')

names = [name.text.strip() for name in soup.find_all('td', {'class': 'name'})]
salary = [sal.text.strip().replace('$', '') for sal in soup.find_all('td')[6::4]]

temp_df = pd.DataFrame({'Player': names[1:], "salary": salary})

df = pd.concat([df, temp_df], ignore_index=True)

df.to_csv('data.csv', index=False)
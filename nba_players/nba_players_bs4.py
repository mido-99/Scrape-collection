import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame() # Master Df

for year in range(2020, 2023):
    
    url = f'https://hoopshype.com/salaries/players/{year}-{year+1}/'

    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')

    names = [name.text.strip() for name in soup.find_all('td', {'class': 'name'})]
    salary = [sal.text.strip().replace('$', '') for sal in soup.find_all('td')[6::4]]

    temp_df = pd.DataFrame({'Player': names[1:], f"{year}/{year+1}": salary})
    
    df = pd.concat([df, temp_df])

df.to_csv('data.csv', index=False)
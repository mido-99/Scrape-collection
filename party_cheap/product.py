import requests
from bs4 import BeautifulSoup
import re
import csv


urls = ["https://www.partycheap.com/Day-Of-The-Dead-Tissue-Garland-p/00920.htm",
        "https://www.partycheap.com/Day-of-the-Dead-Mask-p/00927.htm",
        "https://www.partycheap.com/Jointed-Horse-p/50228.htm",
        "https://www.partycheap.com/Light-Up-Drinking-Cups-p/n960350-master.htm"
        ]

for url in urls:
    
    r = requests.get(url)
    assert r.status_code == 200
    soup = BeautifulSoup(r.text, 'html.parser')

    try:
        item_name = soup.find('span', {'itemprop': "name"}).text
        item_name = "".join(c for c in item_name if c.isalnum() or c in ['-', '_', '.'])
    except:
        i = 1
        item_name = f"final_{i}"
        i +=1
    
    with open(f'{item_name}.csv', 'w', newline='') as csvfile:
        csv.writer(csvfile).writerow(['ID', "Description"])

    # ID
    try:
        id = soup.find(string=re.compile(r"Product Code:"))
        id = id.replace("Product Code: ", '')
        print(id)
    except:
        id = None
    
    # Description
    try:
        color_description = soup.find('table', {'class': "colors_descriptionbox"})
    except:
        color_description = None
    try:
        text_description = soup.find('div', {'id': "ProductDetail_ProductDetails_div2"})
    except:
        text_description = None
    
    if color_description is None:
        full_description = str(text_description)
    elif text_description is None:
        full_description = str(color_description)
    else:
        full_description = str(color_description) + '\n' + str(text_description)

    with open(f'{item_name}.csv', 'a') as csvfile:
        csv.writer(csvfile).writerow([id, full_description])
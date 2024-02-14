import requests
import json
from urllib.parse import parse_qs
from time import sleep


url = r"https://www.udemy.com/api-2.0/discovery-units/all_courses/?p=600&page_size=16&subcategory=&instructional_level=&lang=&price=&duration=&closed_captions=&subs_filter_type=&category_id=300&source_page=category_page&locale=en_US&currency=egp&navigation_locale=en_US&skip_price=true&sos=pc&fl=cat"
users = set()

for p in range(1, 2):
    r = requests.get(
        f"https://www.udemy.com/api-2.0/discovery-units/all_courses/?p={p}&page_size=16&subcategory=&instructional_level=&lang=&price=&duration=&closed_captions=&subs_filter_type=&category_id=300&source_page=category_page&locale=en_US&currency=egp&navigation_locale=en_US&skip_price=true&sos=pc&fl=cat"
        )
    
    for i in range(15):
        try: 
            name = r.json()['unit']['items'][i]['visible_instructors'][0]['display_name']
        except:
            name = r.json()['unit']['items'][i]['visible_instructors'][0]['name']
        finally:
            if name not in users:
                users.add(name)
                print(name)
        sleep(.2)

with open("users_api.txt", 'w') as f:
    for user in users:
        f.write(user + '\n')
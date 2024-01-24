import requests
import json
import pandas as pd

BASE_URL = 'https://www.zillow.com/async-create-search-page-state'
# 2 requests were found, each with different payload
payloads = ['''
    {"searchQueryState":{"pagination":{},"isMapVisible":true,"mapBounds":{"west":-141.191414625,"east":-97.421883375,"south":35.04431931445853,"north":39.72064307616386},"mapZoom":5,"regionSelection":[{"regionId":9,"regionType":2}],"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isForSaleByAgent":{"value":false},"isNewConstruction":{"value":false},"isComingSoon":{"value":false},"isAuction":{"value":false},"isForSaleForeclosure":{"value":false}},"category":"cat2","isListVisible":true},"wants":{"cat2":["mapResults"]},"requestId":2,"isDebugRequest":false}
    ''',
    '''
    {"searchQueryState":{"pagination":{},"isMapVisible":true,"mapBounds":{"west":-141.191414625,"east":-97.42188337500001,"south":32.65410422977953,"north":41.8989428391672},"mapZoom":5,"regionSelection":[{"regionId":9,"regionType":2}],"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isForSaleByAgent":{"value":false},"isNewConstruction":{"value":false},"isComingSoon":{"value":false},"isAuction":{"value":false},"isForSaleForeclosure":{"value":false}},"category":"cat2","isListVisible":true},"wants":{"cat2":["mapResults"]},"requestId":3,"isDebugRequest":false}
    '''
]
HEADERS = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

responses = []
for payload in payloads:    #Populating results list from all requests with variant payloads
    r = requests.put(url=BASE_URL, json=json.loads(payload), headers=HEADERS)
    assert r.status_code == 200, f'Request failed. status code: {r.status_code}'
    
    try: 
        print("Found items:", len(r.json()['cat2']['searchResults']['mapResults']))
        responses.extend(r.json()['cat2']['searchResults']['mapResults'])
    except KeyError:
        print("Non-existing key. Available keys are:\n", r.json().keys())    
    #NO NEED to this part, I thought the site has different dict keys
    # elif 'cat1' in r.json().keys():
    #     print(len(r.json()['cat1']['searchResults']['mapResults']))

print(len(responses))
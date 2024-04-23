import requests
import csv
import json
import sys


url = sys.argv[1]
ID = url.split('/')[-2]
# https://vlaanderenkiest.be/verkiezingen2018/#/gemeente/24055/verkozenen
FULL_DATA = []

get_sections_api = f'https://vlaanderenkiest.be/verkiezingen2018/api/2018/lv/gemeente/{ID}/entiteitLijsten.json'

# Get numbers of sections, this number will be used to make specific request for that section
try:
    r = requests.get(get_sections_api).json()
except json.JSONDecodeError:
    print('Invalid url or non-existing ID!')
    sys.exit()
except requests.exceptions.ConnectionError as e:
    print(f"Request error! : {e}")
    sys.exit()
    
# Names & numbers of parties are returned in response
party_numbers = []
party_names = []
for key, value in r["G"].items():
    party_num_nr = value['nr']
    party_name = value['nm']
    party_numbers.append([party_num_nr, key]) #* Explained below: search #*
    party_names.append(party_name)

# Persons are identified by numbers(ids); in an api this id is used to get person's name
# In another api; it's used to get the number needed for scraping

for num, party_id in party_numbers:
    name_url = f"https://vlaanderenkiest.be/verkiezingen2018/api/2018/lv/gemeente/{ID}/{num}/lijst.json"
    number_url = f"https://vlaanderenkiest.be/verkiezingen2018/api/2018/lv/gemeente/{ID}/{num}/uitslag.json"

    # Get ids of people existing on page
    all_numbers = requests.get(number_url).json()['G'][str(ID)][str(party_id)]['kd']
    numbers_exist = []
    for item in all_numbers:
        key = next(iter(item.keys()))   # Since dict_keys don't support indexing or slicing
        if item[f"{key}"]['vk'] == "1": # I noticed those with vk='1' do exist on the page
            numbers_exist.append({key: {'votes': item[f"{key}"]['ns'], 'rank': item[f"{key}"]['vv']}})

    # Get names of people on page
    all_names = requests.get(name_url).json()[str(party_id)]
    names_exist = []
    for item in numbers_exist:
        key = next(iter(item.keys()))
        if key in all_names:
            name = all_names[key]['nm']
            names_exist.append({name: item[key]})
    FULL_DATA.append(party_names[party_numbers.index([num, party_id])])
    # This is Equivalent to party_names[i] if I used for in range(len(party_numbers)) loop
    FULL_DATA.extend(names_exist)

# Output file
with open(f"{ID}.csv", 'w', newline='') as csvfile:
    headers = ['Party', 'Rank', 'Name', "Votes"]
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for row in FULL_DATA:
        if isinstance(row, dict):
            name, data = next(iter(row.items()))
            votes, rank = data['votes'], data['rank']
            writer.writerow(['', rank, name, votes])
        else:
            writer.writerow([row])
print(f"Output file: {ID}.csv")

"""
#*
Party numbers differ when used for url or query:
    "-6": {
      "nr": 6,
      "nm": "Open Vld",
      "kl": "#005DAA",
      "lg": "img/lijsten/open_vld.png",
      "nl": 1
    },
    "4552": {
      "nr": 7,
      "nm": "KNV",
      "nl": 0
The key of dict number is used in queries; means this is the -id- of the party
The number "nr" is used when calling endpoint api so that's why it's important to save both as a pair

"""
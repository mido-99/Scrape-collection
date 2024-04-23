import requests
import csv


ID = '24045'
FULL_DATA = []

get_sections_api = f'https://vlaanderenkiest.be/verkiezingen2018/api/2018/lv/gemeente/{ID}/entiteitLijsten.json'

# Get numbers of sections, this number will be used to make specific request for that section
r = requests.get(get_sections_api).json()
# Numbers are returned negative, and we in requests they are positive
positive_headers = [- int(negative_head) for negative_head in r["G"].keys()]
party_names = [r['G'][key]['nm'] for key in r["G"].keys()]

# Persons are identified by numbers(ids); in an api this id is used to get person's name
# In another api; it's used to get the number needed for scraping
person_name_list = []
person_number_list = []

for num in positive_headers:
    name_url = f"https://vlaanderenkiest.be/verkiezingen2018/api/2018/lv/gemeente/{ID}/{num}/lijst.json"
    number_url = f"https://vlaanderenkiest.be/verkiezingen2018/api/2018/lv/gemeente/{ID}/{num}/uitslag.json"
    person_name_list.append(name_url)
    person_number_list.append(number_url)

    # Get ids of people existing on page
    all_numbers = requests.get(number_url).json()['G'][str(ID)][str(-num)]['kd']
    numbers_exist = []
    for item in all_numbers:
        key = next(iter(item.keys()))   # Since dict_keys don't support indexing or slicing
        if item[f"{key}"]['vk'] == "1": # I noticed those with vk='1' do exist on the page
            numbers_exist.append({key: {'votes': item[f"{key}"]['ns'], 'rank': item[f"{key}"]['vv']}})

    # Get names of people on page
    all_names = requests.get(name_url).json()[str(-num)]
    names_exist = []
    for item in numbers_exist:
        key = next(iter(item.keys()))
        if key in all_names:
            name = all_names[key]['nm']
            names_exist.append({name: item[key]})
    FULL_DATA.append(party_names[positive_headers.index(num)])
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
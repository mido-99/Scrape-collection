import requests
import csv


BASE_URL = 'https://vlaanderenkiest.be/verkiezingen2018/#/gemeente/24045/verkozenen'
ID = '24045'
FULL_DATA = []

get_sections_api = 'https://vlaanderenkiest.be/verkiezingen2018/api/2018/lv/gemeente/24045/entiteitLijsten.json'
get_person_name_api = 'https://vlaanderenkiest.be/verkiezingen2018/api/2018/lv/gemeente/24045/2/lijst.json'
get_person_num_api = 'https://vlaanderenkiest.be/verkiezingen2018/api/2018/lv/gemeente/24045/2/uitslag.json'

# Get numbers of sections, this number will be used to make specific request for that section
r = requests.get(get_sections_api).json()
# Numbers are returned negative, and we in requests they are positive
positive_headers = [- int(negative_head) for negative_head in r["G"].keys()]

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
            numbers_exist.append({key: item[f"{key}"]['ns']})

    # Get names of people on page
    all_names = requests.get(name_url).json()[str(-num)]
    names_exist = []
    for item in numbers_exist:
        key = next(iter(item.keys()))
        if key in all_names:
            name = all_names[key]['nm']
            names_exist.append({name: item[key]})
    FULL_DATA.extend(names_exist)
# print(FULL_DATA)

# Output file
with open(f"{ID}.csv", 'w', newline='') as csvfile:
    headers = ['Name', "Votes"]
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for row in FULL_DATA:
        name, votes = next(iter(row.items()))
        writer.writerow([name, votes])
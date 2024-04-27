import requests
from bs4 import BeautifulSoup
import re
import csv
from itertools import zip_longest
import time

start = time.time()

BASE_URL = 'http://establimentsturistics.gencat.cat/rtcwebguies/AppJava/guiesTuristics.jsp?pg=0&lg=en&pst=9&idio=null&amte=null&idregistral=#'
# last page = 323
Headers = [
    "Number", "Picture", "Full Name", 'T', "TM", "Email", 
    "Language 1", "Language 2", "Language n", "Speciality 1", "Speciality 2",
    "Speciality n", "Territory 1", "Territory 2", "Territory n"
    ]

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(Headers)


for i in range(100):
    URL = f'http://establimentsturistics.gencat.cat/rtcwebguies/AppJava/guiesTuristics.jsp?pg={i}&lg=en&pst=9&idio=null&amte=null&idregistral=#'
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'lxml')

    # Page Big Data
    table = soup.find('table', {'class': "taula_dades"})
    data_boxes = table.find_all('td', {'class': "ident"})
    
    #- Number
    trs = table.find_all('tr', {'class': "fons_vermell"})
    numbers = [tr.text.strip() for tr in trs]
    
    # Link to a photo
    imgs = table.find_all('img')
    img_links = [f"http://establimentsturistics.gencat.cat{img['src']}" for img in imgs]
    
    full_name_s = []
    phone_s = []
    mobile_s = []
    email_s = []
    language_1 = []
    language_2 = []
    language_n = []
    speciality_1 = []
    speciality_2 = []
    speciality_n = []
    territory_1 = []
    territory_2 = []
    territory_n = []

    for property in data_boxes:
        # Full name
        names = property.find_all('strong')
        names = [name.text.strip() for name in names]
        full_name = ' '.join(names)
        full_name_s.append(full_name)

        # Phone (T)
        try:
            num = property.find(string=re.compile(r'T: ')).strip()
            phone = re.sub(r'\D', '', num)
            phone_s.append(phone)
        except AttributeError:
            phone_s.append('...')
        
        # Mobile Phone (TM)
        try:
            num = property.find(string=re.compile(r'TM: ')).strip()
            mobile = re.sub(r'\D', '', num)
            mobile_s.append(mobile)
        except AttributeError:
            mobile_s.append('...')
        
        # Email
        try:
            mail = property.find('a', {'class': "enlace"}).text.strip()
            email_s.append(mail)
        except AttributeError:
            email_s.append('...')
        

        # Language (Idiomes)
        try:
            langs = property.find(string=re.compile(r'Idiomes: ')).strip().split(':')[1]
            if '|' in langs:
                langs = langs.split('|')
            if len(langs) >= 3:
                language_2.append('Y')
            else:
                language_2.append('N')
            language_1.append('Y')
            language_n.append('-')
        except AttributeError:
            language_1.append('Y')
            language_2.append('N')
            language_n.append('-')

        # Speciality (Especialitats)
        try:
            specs = property.find(string=re.compile(r'Especialitats: ')).strip().split(':')[1]
            if '|' in specs:
                specs = specs.split('|')
            
            if len(specs) >= 3:
                speciality_2.append('Y')
            elif len(specs) >= 1:
                speciality_1.append('Y')                    
            else:
                speciality_1.append('N')                    
                speciality_2.append('N')
            speciality_n.append('-')
        except AttributeError:
            speciality_1.append('N')                    
            speciality_2.append('N')
            speciality_n.append('-')
        
        # Territory (Àmbit Territorial)
        try:
            territory = property.find(string=re.compile(r'Àmbit Territorial: ')).strip().split(':')[1]
            if '|' in territory:
                territory_1.append('Y')
            else:
                territory_2.append('N')
            territory_n.append('N')
        except AttributeError:
            territory_1.append('N')
            territory_2.append('N')
            territory_n.append('N')

    with open('output.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        rows = zip_longest(numbers, img_links,  full_name_s, phone_s, mobile_s, email_s,
                         language_1, language_2, language_n,
                         speciality_1, speciality_2, speciality_n,
                         territory_1, territory_2, territory_n)
        writer.writerows(rows)

end = time.time()
print(f"Execution time: {end-start} s")
# Execution time: 86.97618675231934 s
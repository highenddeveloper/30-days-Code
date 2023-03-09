import requests
from bs4 import BeautifulSoup
import json


url = 'https://archive.ics.uci.edu/ml/datasets.php'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

table = soup.find('table', {'class': 'table table-striped table-bordered table-hover table-condensed'})

table_headers = [header.text.strip() for header in table.find_all('th')]
table_data = []
for row in table.find_all('tr')[1:]:
    row_data = [data.text.strip() for data in row.find_all('td')]
    table_data.append(dict(zip(table_headers, row_data)))

with open('uci_datasets.json', 'w') as f:
    json.dump(table_data, f, indent=4)

print('Data saved as uci_datasets.json')

url = 'http://www.bu.edu/president/boston-university-facts-stats/'

table = soup.find('table', {'class': 'table table-striped table-hover table-responsive'})

table_headers = [header.text.strip() for header in table.find_all('th')]

table_data = []
for row in table.find_all('tr')[1:]:
    row_data = [data.text.strip() for data in row.find_all('td')]
    table_data.append(dict(zip(table_headers, row_data)))

with open('bu_stats.json', 'w') as f:
    json.dump(table_data, f, indent=4)

print('Data saved as bu_stats.json')
 
table = soup.find('table', class_='wikitable')
rows = table.find_all('tr')[1:] 
presidents = []
for row in rows:
    cells = row.find_all('td')
    president = {
        'number': cells[0].text.strip(),
        'name': cells[1].text.strip(),
        'term': cells[2].text.strip(),
        'party': cells[3].text.strip(),
        'portrait': cells[4].find('img')['src'].strip(),
        'thumbnail': cells[4].find('img')['srcset'].split()[0].strip()
    }
    presidents.append(president)

with open('presidents.json', 'w') as f:
    json.dump(presidents, f)

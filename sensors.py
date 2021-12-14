import json
from json import JSONEncoder

import pandas as pd
import requests
import csv


import urllib, json
#Sensory

open('sensory.json', 'w').close()

stationId = str(0)
lista = ['4774']
for id in (lista):
    url = ("https://api.gios.gov.pl/pjp-api/rest/data/getData/" + id)
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    r = requests.get('https://api.gios.gov.pl/pjp-api/rest/data/getData/' + id)
    r.status_code
    r.headers['content-type']
    'application/json; charset=utf8'
    r.encoding
    'utf-8'
    r.text
    '{"type":"User"...'
    r.json()

    with open('sensory.json', 'a', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

with open('sensory.json') as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

key = jsonObject['key']
values = jsonObject['values']

print("Cząstka: " + key)
for i in data['values']:
        print("Data:", i['date'])
        print("Value:", i['value'])

'''
file = open('sensory.json')
message = file.read()
print(message)
'''


'''
class GetParam:
    def __init__(self ,data=None):
        self.key = ""
        self.values = []
        if data is not None:
            self.__dict__ = data

    def toJSON(self):
        return json.dumps(self, default=lambda o : o.__dict__, sort_keys=True, indent=4)

m = GetParam(data=message)
print(m.toJSON())
file.close()
'''

'''

    with open('sensory.json', 'a', encoding='utf-8') as file:
        if lista.index(id) == 0:
            file.writelines('')
        json.dump(data, file, ensure_ascii=False, indent=4)
        if lista.index(id) == len(lista) - 1:
            file.writelines('')
        else: file.writelines(',')


#konwertowanie do csv
with open('sensory.json', encoding='utf-8-sig') as f_input:
    df = pd.read_json(f_input)

df.to_csv('test3.csv', encoding='utf-8', index=False)
#csvData = pdObj.to_csv(index=False)
#print(csvData)




x = json.loads('sensory.json')
print(x)
f = csv.writer(open("test.csv", "a"))


f.writerow(['key', 'date', 'value'])

for x in x:
    f.writerow([x["key"],
                x["values"]["date"],
                x["values"]["value"]])


    with open("venv/sensory.json") as file:
        data = json.load(file)

    with open("venv/data.csv", "w") as file:
        csv_file = csv.writer(file)
        for item in data:
            fields = list(item['values'].values())
            csv_file.writerow([item['key']] + fields)

with open('sensory.json') as json_file_sensor:
    data = json.load(json_file_sensor)

sensors_data = data['key']

# now we will open a file for writing
data_file = open('data_sensors.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for sen in sensors_data:
    if count == 0:
        # Writing headers of CSV file
        header = sen.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(sen.values())

data_file.close()
'''
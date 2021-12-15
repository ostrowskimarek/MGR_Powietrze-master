import json

import matplotlib.pyplot as plt
import requests
import urllib
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
pd.options.mode.chained_assignment = None
import jupyter

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

'''
print("Cząstka: " + key)
for i in data['values']:
        print("Data:", i['date'])
        print("Value:", i['value'])
'''

with open('sensory.json') as jsonFile:
    jsonObject = json.load(jsonFile)
    df = pd.json_normalize(jsonObject['values'])
   # value_reformat = df['value'].round(decimals=2)

    sensors = pd.DataFrame(df.groupby(df['value'])['date'].sum().sort_values(ascending=False))
    o = sensors.iloc
    o = (len(values) -1)

    sensors_freq = df['value'] / o
    sensors_reformat = sensors_freq.round(decimals=2)
    df['Freq'] = sensors_reformat

    print(df)

    

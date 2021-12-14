import json
from urllib.request import urlopen

with urlopen("https://api.gios.gov.pl/pjp-api/rest/data/getData/4769") as response:
    source = response.read()

data = json.loads(source)


sensors_rates = dict()

for item in data ['values']:
    data2 = item['date']
    value = item['value']
    sensors_rates[data2] = value
    print(item)




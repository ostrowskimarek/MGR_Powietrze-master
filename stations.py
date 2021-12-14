import json
import requests

import urllib, json
#STACJE POMIAROWE

stationId = str(0)
lista = ['736','729']
for id in (lista):
    url = ("https://api.gios.gov.pl/pjp-api/rest/station/sensors/" + id)
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    r = requests.get('https://api.gios.gov.pl/pjp-api/rest/station/sensors/' + id)
    r.status_code

    r.headers['content-type']
    'application/json; charset=utf8'
    r.encoding
    'utf-8'
    r.text
    '{"type":"User"...'
    r.json()

    with open('stacje_pomiarowe.json', 'a', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

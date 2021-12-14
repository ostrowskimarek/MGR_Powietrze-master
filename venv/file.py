import json
import requests
response_api = requests.get('https://api.gios.gov.pl/pjp-api/rest/station/findAll')



data = response_api.text
parse_json = json.loads(data)
print(json.dumps(parse_json, indent=4))


with open("data1.json", "w") as f:
    json.dump(parse_json, f)


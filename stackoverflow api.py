from pprint import pprint
import requests
import json

URL = 'https://api.stackexchange.com/2.3/questions?fromdate=1651363200&order=desc&sort=activity&tagged=python&site=stackoverflow'


response = requests.get(URL)
# pprint(response.json())

if response.status_code == 200:
    with open("stc_api_python.txt", "w", encoding="utf-8") as f:
        i = 1
        for item in response.json()['items']:
            f.write(f'{i} {item["tags"][0]}\n{item["title"]} \n{item["link"]}\n\n')
            i += 1

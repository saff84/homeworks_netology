from pprint import pprint
import requests

URL = 'https://superheroapi.com/api/2619421814940190/search/'
SUPER_HEROES = ['Hulk', 'Captain America', 'Thanos']

def search_request(url, heroes):
    most_intelligence_hero = {'name':' ', 'intelligence':'0'}
    for hero in heroes:
        response = requests.get(url + hero)
        for i in range(len(response.json()['results'])):
            if response.json()['results'][i]['name'] == hero:
                if int(most_intelligence_hero['intelligence']) < int(response.json()['results'][i]['powerstats']['intelligence']):
                    most_intelligence_hero = {'name': response.json()['results'][i]['name'], 'intelligence': response.json()['results'][i]['powerstats']['intelligence']}
    print(most_intelligence_hero)

search_request(URL, SUPER_HEROES)



import requests
import random

class Data:
    def __init__(self):
        f = open('ACCESS_TOKEN', 'r')
        self.ACCESS_TOKEN = f.read().strip()

    def search(self, txt):
        response = requests.get('https://api.myanimelist.net/v2/anime',
                        params={  # Query parameters / query string
                            'q': txt,
                            'limit': 5,
                            'fields': 'id,title'
                        }, headers={
                            'Authorization': f'Bearer {self.ACCESS_TOKEN}'
                        })

        response.raise_for_status()
        result = response.json()
        response.close()

        return result

    def info(self, txt):
        id = self.search(txt)['data'][0]['node']['id']
        result = self.anime_large_info(id)

        return result

    def suggest(self, typ):
        result = self.anime_suggest(typ)

        animes = []

        for i in result['data']:
            anime.append(i['id'])

        id = random.choice(animes)
        anime = self.anime_large_info(id)

        return anime

    def anime_large_info(self, id):
        response = requests.get('https://api.myanimelist.net/v2/anime/{id}?fields=id,title,synopsis,statistics',
                        headers={
                            'Authorization': f'Bearer {self.ACCESS_TOKEN}'
                        })
        response.raise_for_status()
        result = response.json()
        response.close()

        return result

    def anime_suggest(self, typ):
        response = requests.get('https://api.myanimelist.net/v2/anime/ranking',
                        params={
                            'ranking_type': typ
                        },
                        headers={
                            'Authorization': f'Bearer {self.ACCESS_TOKEN}'
                        })

        response.raise_for_status()
        result = response.json()
        response.close()

        return result

dat = Data()


from asyncore import read
import requests


class Data:
    def __init__(self):
        f = open('ACCESS_TOKEN', 'r')
        self.ACCESS_TOKEN = f.read()

        self.response = requests.get('https://api.myanimelist.net/v2/anime',
                        params={  # Query parameters / query string
                            'q': 'Spy x Family',
                            'limit': 5,
                            'fields': 'id,title'
                        }, headers={
                            'Authorization': f'Bearer {self.ACCESS_TOKEN}'
                        })

        self.response.raise_for_status()
        self.result = self.response.json()
        self.response.close()


    

dat = Data()

dat.hello()

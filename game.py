import requests
import json
from time import sleep

from requests.models import codes

class Game:
    def __init__(self, link) -> None:
        self.code = link.split('lichess.org/')[-1][:8]
        self.link = f'https://lichess.org/{self.code}'
        while (request := requests.get(f'https://lichess.org/game/export/{self.code}?pgnInJson=true', headers={'accept': 'application/json'})).status_code != 200:
            print(request.status_code)
            sleep(60)
        self.data = json.loads(request.text)
        if self.data['status'] != 'started':
            self.result = {'white': 1, 'black': 0, None: 0.5}[self.data.get('winner', None)]
            if self.data['players']['white']['user']['name'] == 'PlixMax' and self.data['players']['black']['user']['name'] == 'ModernCapablanca':
                self.f_result = self.result
                self.v_result = 1 - self.result
            if self.data['players']['white']['user']['name'] == 'ModernCapablanca' and self.data['players']['black']['user']['name'] == 'PlixMax':
                self.v_result = self.result
                self.f_result = 1 - self.result
        else:
            raise Exception()
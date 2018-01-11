import requests
import json

class CryptonatorCource():
    def __init__(self, base, target):
        self.first = base
        self.second = target
        self.api_base_url = 'https://api.cryptonator.com/api/ticker'
        self.api_full_url = '/'.join([self.api_base_url,
                                      '-'.join([self.first, self.second])
                                      ])

    def cource(self):
        try:
            _rp = requests.get(self.api_full_url)
            _txt = json.loads(_rp.text)
            _cource = float(_txt['ticker']['price'])
            return _cource
        except Exception as ex:
            return ex

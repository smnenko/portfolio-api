import json
import logging
from datetime import datetime, timedelta
from random import choice
from typing import List

import requests


logging.basicConfig(level=logging.INFO)


class ProxyUtil:

    PATH = 'proxies.json'
    URL = 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_geolocation_anonymous/http.txt'
    EXPIRED_MIN = 30

    @staticmethod
    def convert_proxies_raw_to_list(raw_proxies: str):
        return list(map(lambda line: line.split('::')[0], raw_proxies.split('\n')))

    def get_proxies(self):
        response = requests.get(self.URL)
        logging.info('PROXY | Proxies has been received')
        return response.text

    def save_proxies_to_json(self, proxies: List):
        with open(self.PATH, 'w') as file:
            proxies_dict = dict()
            proxies_dict['proxies'] = proxies
            proxies_dict['updated_at'] = str(datetime.now())
            json.dump(proxies_dict, file, indent=4)
        logging.info('PROXY | Proxies has been converted to json')

    def update_proxies(self):
        raw_proxies = self.get_proxies()
        proxies_list = self.convert_proxies_raw_to_list(raw_proxies)
        self.save_proxies_to_json(proxies_list)
        logging.info('PROXY | Proxies has been updated')

    def get_random_proxy(self):
        with open(self.PATH, 'r') as file:
            proxies = json.load(file)
            updated_at = datetime.strptime(
                proxies['updated_at'],
                '%Y-%m-%d %H:%M:%S.%f'
            )
            expired_at = updated_at + timedelta(minutes=self.EXPIRED_MIN)

            if expired_at > datetime.now():
                proxy = choice(proxies['proxies'])
                try:
                    requests.get('https://api.ipify.org/', proxies={
                        'http': f'http://{proxy}',
                        'https': f'https://{proxy}'
                    }, timeout=10)
                except Exception as e:
                    logging.warning(f'PROXY | Proxy is invalid | Trying to get valid proxy | {e}')
                    return self.get_random_proxy()
                return proxy

        self.update_proxies()
        return self.get_random_proxy()

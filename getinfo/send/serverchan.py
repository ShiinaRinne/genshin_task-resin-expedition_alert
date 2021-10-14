import requests
from ..config import config


class ServerChan():
    def __init__(self):
        pass

    @staticmethod
    def send(title: str, status: str, desp: str) -> None:
        url = f'https://sc.ftqq.com/{config.SENDKEY}.send'
        data = {
            'title': f'{title} {status}',
            'desp': desp
        }
        requests.post(url, data)

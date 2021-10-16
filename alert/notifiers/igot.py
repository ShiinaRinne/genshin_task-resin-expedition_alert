from .basenotifier import BaseNotifier as Base
from ..config import config


class Igot(Base):
    def __init__(self):
        self.name = 'iGot'
        self.token = config.IGOT_KEY
        self.retcode_key = 'ret'
        self.retcode_value = 0

    def send(self, text, status, desp):
        url = f'https://push.hellyw.com/{config.IGOT_KEY}'
        data = {
            'title': f'{text} {status}',
            'content': desp
        }
        return self.push('post', url, data=data)

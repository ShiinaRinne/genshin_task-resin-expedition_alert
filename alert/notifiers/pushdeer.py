from .basenotifier import BaseNotifier as Base
from ..config import config


class Pushdeer(Base):
    def __init__(self):
        self.name = 'Pushdeer'
        self.token = config.PUSHDEER_KEY
        self.retcode_key = 'code'
        self.retcode_value = 0

    def send(self, text, status, desp):
        url = 'https://api2.pushdeer.com/message/push'
        data = {
            'pushkey': config.PUSHDEER_KEY,
            'text': f'{text} {status}',
            'desp': desp,
            'type': 'markdown'
        }
        return self.push('post', url, data=data)

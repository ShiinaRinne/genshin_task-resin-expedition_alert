from .basenotifier import BaseNotifier as Base
from ..config import config


class PushPlus(Base):
    def __init__(self):
        self.name = 'pushplus'
        self.token = config.PUSH_PLUS_TOKEN
        self.retcode_key = 'code'
        self.retcode_value = 200

    def send(self, text, status, desp):
        url = 'http://www.pushplus.plus/send'
        data = {
            'token': config.PUSH_PLUS_TOKEN,
            'title': f'{text} {status}',
            'content': desp,
            'template': 'markdown',
            'topic': config.PUSH_PLUS_USER
        }
        return self.push('post', url, data=data)

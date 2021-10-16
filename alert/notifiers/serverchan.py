from .basenotifier import BaseNotifier as Base
from ..config import config


class ServerChan(Base):
    def __init__(self):
        self.name = 'Server Chan'
        self.token = config.SCKEY
        self.retcode_key = 'errno'
        self.retcode_value = 0

    def send(self, text, status, desp):
        url = f'https://sc.ftqq.com/{config.SCKEY}.send'
        data = {
            'text': f'{text} {status}',
            'desp': desp
        }
        return self.push('post', url, data=data)

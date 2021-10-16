from .basenotifier import BaseNotifier as Base
from ..config import config


class ServerChanTurbo(Base):
    def __init__(self):
        self.name = 'Server Chan Turbo'
        self.token = config.SCTKEY
        self.retcode_key = 'errno'
        self.retcode_value = 0

    def send(self, text, status, desp):
        url = f'https://sctapi.ftqq.com/{config.SCTKEY}.send'
        data = {
            'title': f'{text} {status}',
            'desp': desp
        }
        return self.push('post', url, data=data)

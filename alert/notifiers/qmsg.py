from .basenotifier import BaseNotifier as Base
from ..config import config


class Qmsg(Base):
    def __init__(self):
        self.name = 'Qmsg'
        self.token = config.QMSG_KEY
        self.retcode_key = 'code'
        self.retcode_value = 0

    def send(self, text, status, desp):
        url = f'https://qmsg.zendee.cn/send/{config.QMSG_KEY}'
        data = {
            'msg': f'{text} {status}\n\n{desp}'
        }
        return self.push('post', url, data=data)
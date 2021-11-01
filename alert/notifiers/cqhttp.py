from .basenotifier import BaseNotifier as Base
from ..config import config


class Cqhttp(Base):
    def __init__(self):
        self.name = 'Cqhttp'
        self.token = config.CQHTTP_TOKEN
        self.retcode_key = 'retcode'
        self.retcode_value = 0

    def send(self, text, status, desp):
        url = f'http://{config.CQHTTP_IP}:5700/send_private_msg'
        data = {
            "access_token": config.CQHTTP_TOKEN,
            "user_id": config.CQHTTP_USER_ID,
            'message': f'{text} {status}\n\n{desp}'
        }
        return self.push('post', url, data=data)

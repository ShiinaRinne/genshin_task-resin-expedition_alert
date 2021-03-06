from .basenotifier import BaseNotifier as Base
from ..config import config


class Cqhttp(Base):
    def __init__(self):
        self.name = 'Cqhttp'
        self.token = config.CQHTTP_SEND_ID
        self.retcode_key = 'retcode'
        self.retcode_value = 0

    def send(self, text, status, desp):
        if config.CQHTTP_MESSAGE_TYPE == "group":
            url = f'{config.CQHTTP_URL}send_group_msg' if config.CQHTTP_URL.endswith('/') else f'{config.CQHTTP_URL}/send_group_msg'
            header = {'Authorization': 'Bearer ' + config.CQHTTP_TOKEN}
            data = {
                "group_id": config.CQHTTP_SEND_ID,
                "message": f'{text} {status}\n\n{desp}'
            }

        elif config.CQHTTP_MESSAGE_TYPE == "private":
            url = f'{config.CQHTTP_URL}send_private_msg' if config.CQHTTP_URL.endswith('/') else f'{config.CQHTTP_URL}/send_private_msg'
            header = {'Authorization': 'Bearer ' + config.CQHTTP_TOKEN}
            data = {
                "user_id": config.CQHTTP_SEND_ID,
                "message": f'{text} {status}\n\n{desp}'
            }

        return self.push('post', url, headers=header, data=data)

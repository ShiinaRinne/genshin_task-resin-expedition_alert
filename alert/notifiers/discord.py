
from .basenotifier import BaseNotifier as Base
from ..config import config


class Discord(Base):
    def __init__(self):
        self.name = 'Discord'
        self.token = config.DISCORD_WEBHOOK
        self.retcode_value = 204

    def send(self, text, status, desp):
        url = config.DISCORD_WEBHOOK
        data = {
            'embeds': [{
                'title': f'{text}{status}',
                'description': desp,
                'color': "15553898"
            }]
        }
        return self.push('post', url, json=data)
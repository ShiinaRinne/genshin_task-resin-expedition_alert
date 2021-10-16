from .basenotifier import BaseNotifier as Base
from ..config import config


class WechatWorkBot(Base):
    def __init__(self):
        self.name = 'Wechat Work Bot'
        self.token = config.WW_BOT_KEY
        self.retcode_key = 'errcode'
        self.retcode_value = 0

    def send(self, text, status, desp):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={config.WW_BOT_KEY}'
        data = {
            'msgtype': 'text',
            'text': {
                'content': f'{text} {status}\n\n{desp}'
            }
        }
        return self.push('post', url, json=data)

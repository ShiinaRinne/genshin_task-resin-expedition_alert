import base64
import hashlib
import hmac
import json
import time
from urllib import parse

from .basenotifier import BaseNotifier as Base
from ..config import config


class DingTalkBot(Base):
    def __init__(self):
        self.name = 'DingTalk Bot'
        self.token = config.DD_BOT_TOKEN
        self.retcode_key = 'errcode'
        self.retcode_value = 0

    # Fixed by wananing
    def send(self, text, status, desp):
        url = ''
        if config.DD_BOT_TOKEN:
            url = f'https://oapi.dingtalk.com/robot/send?access_token={config.DD_BOT_TOKEN}'
            if config.DD_BOT_SECRET:
                secret = config.DD_BOT_SECRET
                timestamp = int(round(time.time() * 1000))
                secret_enc = secret.encode('utf-8')
                string_to_sign = f'{timestamp}\n{secret}'
                string_to_sign_enc = string_to_sign.encode('utf-8')
                hmac_code = hmac.new(
                    secret_enc, string_to_sign_enc,
                    digestmod=hashlib.sha256).digest()
                sign = parse.quote_plus(base64.b64encode(hmac_code))
                url = f'https://oapi.dingtalk.com/robot/send?access_token={config.DD_BOT_TOKEN}&timestamp={timestamp}&sign={sign}'

        header = {'Content-Type': 'application/json ;charset=utf-8 '}
        data = {
            'msgtype': 'text',
            'text': {
                'content': f'{text} {status}\n\n{desp}'
            }
        }
        data = json.dumps(data)
        return self.push('post', url, data=data, headers=header)

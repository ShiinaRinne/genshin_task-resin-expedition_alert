from .basenotifier import BaseNotifier as Base
from ..config import config


class CoolPush(Base):
    def __init__(self):
        self.name = 'Cool Push'
        self.token = config.COOL_PUSH_SKEY
        self.mode = config.COOL_PUSH_MODE
        self.sendid = config.COOL_PUSH_SENDID
        self.retcode_key = 'code'
        self.retcode_value = 200

    def send(self, text, status, desp):
        if (config.COOL_PUSH_SENDID != ""):
            if ("send" in config.COOL_PUSH_MODE):
                url = f'https://push.xuthus.cc/{config.COOL_PUSH_MODE}/{config.COOL_PUSH_SKEY}?userId={config.COOL_PUSH_SENDID}'
            elif ("group" in config.COOL_PUSH_MODE) :
                url = f'https://push.xuthus.cc/{config.COOL_PUSH_MODE}/{config.COOL_PUSH_SKEY}?groupId={config.COOL_PUSH_SENDID}'
        else:
            url = f'https://push.xuthus.cc/{config.COOL_PUSH_MODE}/{config.COOL_PUSH_SKEY}'

        data = f'{text} {status}\n\n{desp}'.encode('utf-8')
        return self.push('post', url, data=data)

from .exceptions import NotificationError
from .utils import log, request


class BaseNotifier(object):
    def __init__(self):
        self.name = None
        self.token = None
        self.retcode_key = None
        self.retcode_value = None

    def send(self):
        ...

    def push(self,
             method,
             url,
             params=None,
             data=None,
             json=None,
             headers=None):
        """
        🚫: disabled
        🥳: success
        😳: failure
        """
        if not self.token:
            # log.info(f'{self.name} 🚫')
            return
        try:
            response = request(method, url, 2, params, data, json, headers).json()
        except Exception as e:
            raise NotificationError(f'{self.name} 😳\n{e}')
        else:
            retcode = response.get('data', {}).get(
                self.retcode_key,
                -1) if self.name == 'Server Chan Turbo' else response.get(
                self.retcode_key, -1)
            if retcode == self.retcode_value:
                log.info(f'{self.name} 🥳')

            # Telegram Bot
            elif self.name == 'Telegram Bot' and retcode:
                log.info(f'{self.name} 🥳')
            elif self.name == 'Telegram Bot' and response[self.retcode_value] == 400:
                raise NotificationError(f'{self.name} 😳\n请主动给 bot 发送一条消息并检查 TG_USER_ID 是否正确')
            elif self.name == 'Telegram Bot' and response[self.retcode_value] == 401:
                raise NotificationError(f'{self.name} 😳\nTG_BOT_TOKEN 错误')
            else:
                raise NotificationError(f'{self.name} 😳\n{response}')
        #一个推送渠道失败后不会继续进行推送
        finally:
            return

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
        ð«: disabled
        ð¥³: success
        ð³: failure
        """
        if not self.token:
            # log.info(f'{self.name} ð«')
            return
        try:
            response = request(method, url, 2, params, data, json, headers)
        except Exception as e:
            log.error(f'{self.name} ð³\n{e}')
            raise NotificationError()
        else:
            if self.name == 'Server Chan Turbo':
                retcode = response.json().get('data', {}).get(self.retcode_key,-1)
            elif self.name == 'Discord':
                retcode = response.status_code
            else :
                retcode = response.json().get(self.retcode_key, -1)
            if retcode == self.retcode_value:
                log.info(f'{self.name} ð¥³')

            # Telegram Bot
            elif self.name == 'Telegram Bot' and retcode:
                log.info(f'{self.name} ð¥³')
            elif self.name == 'Telegram Bot' and response.json()[self.retcode_value] == 400:
                log.error(f'{self.name} ð³\nè¯·ä¸»å¨ç» bot åéä¸æ¡æ¶æ¯å¹¶æ£æ¥ TG_USER_ID æ¯å¦æ­£ç¡®')
                raise NotificationError()
            elif self.name == 'Telegram Bot' and response.json()[self.retcode_value] == 401:
                log.error(f'{self.name} ð³\nTG_BOT_TOKEN éè¯¯')
                raise NotificationError()
            else:
                log.error(f'{self.name} ð³\n{response}')
                raise NotificationError()
        # ä¸ä¸ªæ¨éæ¸ éå¤±è´¥åä¸ä¼ç»§ç»­è¿è¡æ¨é
        finally:
            return

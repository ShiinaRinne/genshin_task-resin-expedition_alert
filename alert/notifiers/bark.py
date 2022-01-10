from .basenotifier import BaseNotifier as Base
from ..config import config


class Bark(Base):
    def __init__(self):
        self.name = 'Bark'
        self.url = config.BARK_URL
        self.token = config.BARK_KEY
        self.retcode_key = 'code'
        self.retcode_value = 200

    def send(self, text, status, desp):
        url = f'{config.BARK_URL}{config.BARK_KEY}'
        data = {
            'title': f'{text} {status}',
            'body': desp
        }

        # 可选项
        if (config.BARK_GROUP) : data['group'] = f'{config.BARK_GROUP}'
        if (config.BARK_ICON) : data['icon'] = f'{config.BARK_ICON}'
        if (config.BARK_ARCHIVE) : data['isArchive'] = f'{config.BARK_ARCHIVE}'

        return self.push('post', url, data=data)
from .basenotifier import BaseNotifier as Base
from ..config import config


class Bark(Base):
    def __init__(self):
        self.name = 'Bark'
        self.token = config.BARK_KEY
        self.retcode_key = 'errno'
        self.retcode_value = 0

    def send(self, text, status, desp):
        url = f'https://api.day.app/{config.BARK_KEY}'
        data = {
            'title': f'{text} {status}',
            'body': desp
        }

        # 可选项
        if (config.BARK_GROUP) : data['group'] = f'{config.BARK_GROUP}'
        if (config.BARK_ICON) : data['icon'] = f'{config.BARK_ICON}'
        if (config.BARK_ARCHIVE) : data['isArchive'] = f'{config.BARK_ARCHIVE}'

        return self.push('post', url, data=data)
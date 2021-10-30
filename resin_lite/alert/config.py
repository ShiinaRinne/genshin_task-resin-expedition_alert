import json
import os
from .getinfo.model.configdata import ConfigData


class Config():
    def __init__(self):
        project_path = os.path.dirname(__file__)
        config_file = os.path.join(project_path, 'config_data', 'config.json')
        if not(os.path.exists(config_file)):
            config_file = os.path.join(
                project_path, 'config_data', 'config.example.json')

        with open(config_file, 'r', encoding='utf-8') as f:
            self.config_json = json.load(f)

        self.config_data = {}

        # Cookie configs
        # Cookie from https://bbs.mihoyo.com/ys/
        self.config_data['UID'] = self.get_config('UID')
        self.config_data['COOKIE'] = self.get_config('COOKIE')
        self.config_data['SLEEP_TIME'] = self.get_config('SLEEP_TIME')
        self.config_data['QQ'] = self.get_config('QQ')

        self.config = ConfigData.parse_obj(self.config_data)

    def get_config(self, name: str):
        value = os.environ[name] if os.environ.get(name) else self.config_json.get(name)

        return value

config = Config().config

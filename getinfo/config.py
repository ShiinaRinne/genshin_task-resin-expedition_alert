import json
import os
from .model.configdata import ConfigData


class Config():
    def __init__(self):
        project_path = os.path.dirname(__file__)
        config_file = os.path.join(project_path, 'config_data', 'config.json')
        if not(os.path.exists(config_file)):
            config_file = os.path.join(
                project_path, 'config_data', 'config.example.json')

        with open(config_file, 'r', encoding='utf-8') as f:
            self.config_data = ConfigData.parse_obj(json.load(f))


config = Config().config_data

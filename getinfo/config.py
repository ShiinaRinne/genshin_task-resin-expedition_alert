import json
import os


class Config():
    def __init__(self):
        project_path = os.path.dirname(__file__)
        config_file = os.path.join(project_path, 'config_data', 'config.json')
        if not(os.path.exists(config_file)):
            config_file = os.path.join(
                project_path, 'config_data', 'config.example.json')

        with open(config_file, 'r', encoding='utf-8') as f:
            self.config_json = json.load(f)

        self.UID: str = self.get_config('UID')
        self.COOKIE: str = self.get_config('COOKIE')

        self.WECOM_STATUS: str = self.get_config('WECOM_STATUS')
        self.SERVER_CHAN_STATUS: str = self.get_config('SERVER_CHAN_STATUS')

        self.SENDKEY: str = self.get_config('SENDCKEY')

        self.WECOM_CORP_ID: str = self.get_config('WECOM_CORP_ID')
        self.WECOM_SECRET: str = self.get_config('WECOM_SECRET')
        self.WECOM_USER_ID: str = self.get_config('WECOM_USER_ID')
        self.WECOM_AGENT_ID: str = self.get_config('WECOM_AGENT_ID')

        self.RESIN_ALERT_NUM: str = self.get_config('RESIN_ALERT_NUM')
        self.RECEIVE_RESIN_DATA: str = self.get_config('RECEIVE_RESIN_DATA')
        self.RECEIVE_BOSS_COUNT: str = self.get_config('RECEIVE_BOSS_COUNT')
        self.RECEIVE_TASK_NUM: str = self.get_config('RECEIVE_TASK_NUM')
        self.REVEIVE_EXPEDITION_NUM: str = self.get_config(
            'REVEIVE_EXPEDITION_NUM')
        self.INCOMPLETE_ALERT: str = self.get_config('INCOMPLETE_ALERT')
        self.SLEEP_TIME: str = self.get_config('SLEEP_TIME')
        
    def get_config(self, name: str) -> str:
        return os.environ[name] if os.environ.get(name) else self.config_json.get(name, '')


config = Config()

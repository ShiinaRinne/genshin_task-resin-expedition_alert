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
        self.config_data['RESIN_ALERT_NUM'] = self.get_config('RESIN_ALERT_NUM')
        self.config_data['RECEIVE_RESIN_DATA'] = self.get_config('RECEIVE_RESIN_DATA')
        self.config_data['RECEIVE_BOSS_COUNT'] = self.get_config('RECEIVE_BOSS_COUNT')
        self.config_data['RECEIVE_TASK_NUM'] = self.get_config('RECEIVE_TASK_NUM')
        self.config_data['REVEIVE_EXPEDITION_NUM'] = self.get_config('REVEIVE_EXPEDITION_NUM')
        self.config_data['EXPEDITION_COMPLETE_ALERT'] = self.get_config('EXPEDITION_COMPLETE_ALERT')
        self.config_data['INCOMPLETE_ALERT'] = self.get_config('INCOMPLETE_ALERT')
        self.config_data['SLEEP_TIME'] = self.get_config('SLEEP_TIME')
        self.config_data['ALERT_SUCCESS_SLEEP_TIME'] = self.get_config('ALERT_SUCCESS_SLEEP_TIME')
        self.config_data['SLEEP_START_TIME'] = self.get_config('SLEEP_START_TIME')
        self.config_data['SLEEP_END_TIME'] = self.get_config('SLEEP_END_TIME')
        self.config_data['RECEIVE_HOMECOIN_ALERT'] = self.get_config('RECEIVE_HOMECOIN_ALERT')

        # Cookie configs
        # Cookie from https://bbs.mihoyo.com/ys/
        self.config_data['RUN_ENV'] = self.get_config('RUN_ENV')
        self.config_data['NAME'] = self.get_config('NAME')
        self.config_data['UID'] = self.get_config('UID')
        self.config_data['COOKIE'] = self.get_config('COOKIE')

    # Notifier configs
        # WeChat Work App
        self.config_data['WW_ID'] = self.get_config('WW_ID')
        self.config_data['WW_APP_SECRET'] = self.get_config('WW_APP_SECRET')
        self.config_data['WW_APP_USERID'] = self.get_config('WW_APP_USERID')
        self.config_data['WW_APP_AGENTID'] = self.get_config('WW_APP_AGENTID')

        # WeChat Work Bot
        self.config_data['WW_BOT_KEY'] = self.get_config('WW_BOT_KEY')

        # Bark
        self.config_data['BARK_URL'] = self.get_config('BARK_URL')
        self.config_data['BARK_KEY'] = self.get_config('BARK_KEY')
        self.config_data['BARK_GROUP'] = self.get_config('BARK_GROUP')
        self.config_data['BARK_ICON'] = self.get_config('BARK_ICON')
        self.config_data['BARK_ARCHIVE'] = self.get_config('BARK_ARCHIVE')

        # Telegram Bot
        self.config_data['TG_BOT_API'] = self.get_config('TG_BOT_API')
        self.config_data['TG_BOT_TOKEN'] = self.get_config('TG_BOT_TOKEN')
        self.config_data['TG_USER_ID'] = self.get_config('TG_USER_ID')

        # Pushdeer
        self.config_data['PUSHDEER_KEY'] = self.get_config('PUSHDEER_KEY')

        #cqhttp
        self.config_data['CQHTTP_URL'] = self.get_config('CQHTTP_URL')
        self.config_data['CQHTTP_MESSAGE_TYPE'] = self.get_config('CQHTTP_MESSAGE_TYPE')
        self.config_data['CQHTTP_SEND_ID'] = self.get_config('CQHTTP_SEND_ID')
        self.config_data['CQHTTP_TOKEN'] = self.get_config('CQHTTP_TOKEN')

        # DingTalk Bot
        self.config_data['DD_BOT_TOKEN'] = self.get_config('DD_BOT_TOKEN')
        self.config_data['DD_BOT_SECRET'] = self.get_config('DD_BOT_SECRET')

        # Server Chan
        self.config_data['SCTKEY'] = self.get_config('SCTKEY')

        # pushplus
        self.config_data['PUSH_PLUS_TOKEN'] = self.get_config('PUSH_PLUS_TOKEN')
        self.config_data['PUSH_PLUS_USER'] = self.get_config('PUSH_PLUS_USER')

        # Cool Push
        self.config_data['COOL_PUSH_SKEY'] = self.get_config('COOL_PUSH_SKEY')
        self.config_data['COOL_PUSH_MODE'] = self.get_config('COOL_PUSH_MODE')
        self.config_data['COOL_PUSH_SENDID'] = self.get_config('COOL_PUSH_SENDID')

        #QMSG酱
        self.config_data['QMSG_KEY'] = self.get_config('QMSG_KEY')

        # Discord webhook
        self.config_data['DISCORD_WEBHOOK'] = self.get_config('DISCORD_WEBHOOK')

        # iGot
        self.config_data['IGOT_KEY'] = self.get_config('IGOT_KEY')

        # # Custom Notifier Config
        # self.CUSTOM_NOTIFIER = self.get_config('CUSTOM_NOTIFIER')

        self.config = ConfigData.parse_obj(self.config_data)

    def get_config(self, name: str):
        value = os.environ[name] if os.environ.get(name) else self.config_json.get(name)
        if name == 'RESIN_ALERT_NUM' and not value:
            value = 150
        elif name == 'RECEIVE_RESIN_DATA' and not value:
            value = "ON"
        elif name == 'RECEIVE_BOSS_COUNT' and not value:
            value = "ON"
        elif name == 'RECEIVE_TASK_NUM' and not value:
            value = "ON"
        elif name == 'REVEIVE_EXPEDITION_NUM' and not value:
            value = "ON"
        elif name == 'INCOMPLETE_ALERT' and not value:
            value = "215959"
        elif name == 'EXPEDITION_COMPLETE_ALERT' and not value:
            value = "ON"
        elif name == 'SLEEP_TIME' and not value:
            value = 900
        elif name == 'ALERT_SUCCESS_SLEEP_TIME' and not value:
            value = 1800
        elif name == 'RECEIVE_HOMECOIN_ALERT' and not value:
            value = "OFF"
        elif name == 'RUN_ENV' and not value:
            value = "local"

        elif name == 'BARK_URL' and not value:
            value = "https://api.day.app/"
        return value

config = Config().config
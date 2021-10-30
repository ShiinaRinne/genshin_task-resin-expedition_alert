from .getinfo import MysAPI, APIError
from .getinfo.model import BaseData
from .config import config
import time
import requests
import logging
import json

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

log = logger = logging


def insert_data(data: BaseData, status: str = "") -> None:
    data = {
        "current_resin": data.current_resin,
        "max_resin": data.max_resin,
        "resin_discount_num_limit": data.resin_discount_num_limit,
        "resin_recovery_time": data.resin_recovery_time,
        "current_expedition_num": data.current_expedition_num,
        "finished_task_num": data.finished_task_num,
        "is_extra_task_reward_received": data.is_extra_task_reward_received,
        "remarks": "" # 备注
    }
    data["uid"] = config.UID
    data["qq"] = config.QQ
    url = "https://api.youngmoe.com/resinbot"

    requests.post(url=url, data=json.dumps(data))


def main() -> None:
    uid = config.UID
    cookie = config.COOKIE
    try:
        base_data: BaseData = MysAPI(uid, cookie).get_dailyNote()
        insert_data(base_data)
    except APIError:
        log.error("APIError,检查cookie与id是否对应")
        exit()

    log.info(f'本轮运行结束，休眠{config.SLEEP_TIME}秒')
    time.sleep(config.SLEEP_TIME)

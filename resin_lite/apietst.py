
import requests
import json


def insert_data(data) -> None:
    url = "https://api.youngmoe.com/alert/data"
    data = json.dumps(data)
    requests.post(url=url, data=json.dumps(data))



url = "https://api.youngmoe.com/resinbot"
data = {
    "uid": 100088888,
    "qq": 12345678,
    "current_resin": 60,
    "max_resin": 160,
    "resin_discount_num_limit": 10,
    "resin_recovery_time": 10,
    "current_expedition_num": 4,
    "finished_task_num": 0,
    "is_extra_task_reward_received": False,
    "remarks": "no"
}

requests.post(url=url, data=json.dumps(data))

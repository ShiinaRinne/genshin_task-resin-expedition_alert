from ..config import config
from .dataanalystic import *

def receive_data(base_data) -> list[str]:
    """
    
    Configure the data you want to receive
    """
    result: list[str] = []

    if (config.NAME):
        result.append(f'账号：{config.NAME}')

    hidden_uid = str(config.UID).replace(str(config.UID)[3:-3], '***', 1)
    result.append(f'UID: {hidden_uid}\n')

    if config.RECEIVE_RESIN_DATA == "ON":
        result.append(get_resin_data(base_data))

    # resin_discount_num_limit
    if config.RECEIVE_BOSS_COUNT == "ON":
        result.append(get_resin_discount_data(base_data))

    # task_num
    if config.RECEIVE_TASK_NUM == "ON":
        result.append(get_task_num_data(base_data))

    # expedition_num
    if config.REVEIVE_EXPEDITION_NUM == "ON":
        result.append(get_expedition_data(base_data))
        
    return result
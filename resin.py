from getinfo import MysAPI
from getinfo.exceptions import APIError
from getinfo.config import config
from getinfo.model import BaseData
from getinfo.send.exwecom import SendWeixin
from getinfo.send.serverchan import ServerChan
from getinfo.config import config
from data_analystic import *
import time


def sendAll(title: str, info: str) -> None:
    if config.WECOM_STATUS == "ON":
        wx = SendWeixin(title, info)
        wx.send_message()
        # wx.send_message("markdown")

    if config.SERVER_CHAN_STATUS == "ON" and config.SENDKEY != "":
        ServerChan.send(title, status="", desp=info)


def main() -> None:
    uid = config.UID
    cookie = config.COOKIE
    try:
        base_data: BaseData = MysAPI(uid, cookie).get_dailyNote()
    except APIError:
        sendAll(title="error", info="发生错误，请检查cookie与id是否对应")
        exit()

    result: list[str] = []

    # current_resin
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

    
    
    info = "\n".join(result)
    sendAll("亲爱的亲爱的亲爱的旅行者！树脂快溢出啦！", info)
    if(base_data.current_resin >= int(config.RESIN_ALERT_NUM)):
        sendAll("亲爱的亲爱的亲爱的旅行者！树脂快溢出啦！", info)

    if(config.INCOMPLETE_ALERT != "" and base_data.finished_task_num != 4):
        time1 = time.strptime(config.INCOMPLETE_ALERT, '%H%M%S')
        time2 = time.localtime()
        if(time2.tm_hour == time1.tm_hour and time2.tm_min >= time1.tm_min or time2.tm_hour > time1.tm_hour and time2.tm_min < time1.tm_min):
            sendAll("亲爱的亲爱的亲爱的旅行者！你今日的委托还没有完成哦~", info)


if __name__ == "__main__":
    while True:
        main()
        time.sleep(config.SLEEP_TIME)

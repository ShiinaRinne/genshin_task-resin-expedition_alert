from getinfo import MysAPI,APIError
from getinfo.config import config
from getinfo.model import BaseData
from getinfo.send import SendWeixin,ServerChan
from dataanalystic import *
import time

from receivedata import receive_data


def sendAll(title: str, body: str) -> None:
    if config.WECOM_STATUS == "ON":
        wx = SendWeixin()
        wx.send_message(title, body)

    if config.SERVER_CHAN_STATUS == "ON" and config.SENDKEY != "":
        ServerChan.send(title, status="", desp=body)


def main() -> None:
    uid = config.UID
    cookie = config.COOKIE
    try:
        base_data: BaseData = MysAPI(uid, cookie).get_dailyNote()
    except APIError:
        sendAll(title="error", body="发生错误，请检查cookie与id是否对应")
        exit()

    result: str = receive_data(base_data)

    body = "\n".join(result)
    sendAll("亲爱的亲爱的亲爱的旅行者！树脂快溢出啦！", body)
    if(base_data.current_resin >= int(config.RESIN_ALERT_NUM)):
        sendAll("亲爱的亲爱的亲爱的旅行者！树脂快溢出啦！", body)

    if(config.INCOMPLETE_ALERT != "" and base_data.finished_task_num != 4):
        time1 = time.strptime(config.INCOMPLETE_ALERT, '%H%M%S')
        time2 = time.localtime()
        if(time2.tm_hour == time1.tm_hour and time2.tm_min >= time1.tm_min or time2.tm_hour > time1.tm_hour and time2.tm_min < time1.tm_min):
            sendAll("亲爱的亲爱的亲爱的旅行者！你今日的委托还没有完成哦~", body)


if __name__ == "__main__":
    while True:
        main()
        time.sleep(config.SLEEP_TIME)

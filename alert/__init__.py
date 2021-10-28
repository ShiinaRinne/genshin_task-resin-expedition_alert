from .getinfo import MysAPI, APIError
from .config import config
from . import notifiers
from .getinfo.dataanalystic import *
import time

from .notifiers.utils import log
from .getinfo.receivedata import receive_data



def send(text:str,status:str,message:str) -> None:
    # message_box = '\n'.join(message)

    try:
        notifiers.send2all(text=text,status=status, desp=message)
    except Exception as e:
        print(e)


def check(uid, cookie, name):
    try:
        base_data: BaseData = MysAPI(uid, cookie).get_dailyNote()
    except APIError:
        send(status="error", message="发生错误，请检查cookie与id是否对应或是否已开启米游社实时便笺功能。")
        exit()

    result: str = receive_data(base_data)
    message = "\n".join(result)
    alert = alert_task = alert_resin =alert_expedition = False
    status= ""

    # 半夜委托没做完时
    if(config.INCOMPLETE_ALERT != "" and base_data.finished_task_num != 4):
        time1 = time.strptime(config.INCOMPLETE_ALERT, '%H%M%S')
        time2 = time.localtime()
        if(time2.tm_hour == time1.tm_hour and time2.tm_min >= time1.tm_min or time2.tm_hour > time1.tm_hour and time2.tm_min < time1.tm_min):
            status = "你今日的委托还没有完成哦~"
            alert_task = True
            log.info('今日委托未完成，发送提醒。')
        else:
            alert_task = False
            log.info('今日委托未完成，未到提醒时间。')
    else:
        alert_task = False
        log.info('委托检查结束，今日委托已完成。（或未配置委托未完成提醒）')

    # 树脂达到临界时
    if(base_data.current_resin >= int(config.RESIN_ALERT_NUM)):
        if(base_data.current_resin >= 160):
            status= status + "树脂已经溢出啦！"
        else:
            status= status + "树脂快要溢出啦！"
        alert_resin = True
        log.info('树脂已到临界值，发送提醒。')
    else:
        alert_resin = False
        log.info('树脂检查结束，未到提醒临界值。')

    if(config.EXPEDITION_COMPLETE_ALERT == "ON"):
        if("已完成" in message):
            status= status + "探索派遣已经完成啦！"
            alert_expedition = True
            log.info('探索派遣已完成，发送提醒。')
        else:
            alert_expedition = False
            log.info('探索派遣检查结束，不存在完成的探索派遣。')
    else:
        log.info('不提醒探索派遣完成情况，跳过探索派遣检查。')

    alert = alert_resin or alert_task or alert_expedition
    if alert:
        send(text="亲爱的亲爱的亲爱的旅行者！",status=status, message=message)

    return alert

def main() -> None:
    uid = config.UID
    cookie = config.COOKIE
    name = config.NAME

    while True:
        alert= check(uid, cookie, name)

        if alert :
            log.info(f'本轮运行结束，提醒已发送，休眠{config.ALERT_SUCCESS_SLEEP_TIME}秒')
            time.sleep(config.ALERT_SUCCESS_SLEEP_TIME)
        else:
            log.info(f'本轮运行结束，休眠{config.SLEEP_TIME}秒')
            time.sleep(config.SLEEP_TIME)


# for qqbot
def qqmessage()-> list[str]:
    uid = config.UID
    cookie = config.COOKIE
    try:
        base_data: BaseData = MysAPI(uid, cookie).get_dailyNote()
    except APIError:
        send(status="error", message="发生错误，请检查cookie与id是否对应或是否已开启米游社实时便笺功能。")
        exit()

    result: list[str] = receive_data(base_data)

    return result

def qq_query(query_param:str) -> str:
    uid = config.UID
    cookie = config.COOKIE
    try:
        base_data: BaseData = MysAPI(uid, cookie).get_dailyNote()
    except APIError:
        return "发生错误，请检查cookie与id是否对应或是否已开启米游社实时便笺功能。"
    
    if(query_param=="总览"):
        result: list[str] = receive_data(base_data)
        return '\n'.join(result)
    elif(query_param=="树脂"):
        return get_resin_data(base_data)
    elif(query_param=="boss"):
        return get_resin_discount_data(base_data)
    elif(query_param=="委托"):
        return get_task_num_data(base_data)
    elif(query_param=="派遣"):
        return get_expedition_data(base_data)
    else:
        return "查询参数有误"

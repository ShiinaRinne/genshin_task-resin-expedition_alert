from .getinfo import MysAPI, APIError
from .config import config
from . import notifiers
from .getinfo.dataanalystic import *
import time

from .getinfo.receivedata import receive_data



def send(status:str,message:str) -> None:
    # message_box = '\n'.join(message)

    # The ``` is added to use markdown code block
    markdown_message = f'```\n{message}```'
    try:
        notifiers.send2all(status=status, desp=markdown_message)
    except Exception as e:
        print(e)


def main() -> None:
    uid = config.UID
    cookie = config.COOKIE
    try:
        base_data: BaseData = MysAPI(uid, cookie).get_dailyNote()
    except APIError:
        send(status="error", message="发生错误，请检查cookie与id是否对应")
        exit()

    result: str = receive_data(base_data)

    message = "\n".join(result)
    # send(status="亲爱的亲爱的亲爱的旅行者！树脂快溢出啦！", message=message) # 调试用
    # 树脂达到临界时
    if(base_data.current_resin >= int(config.RESIN_ALERT_NUM)):
        send(status="亲爱的亲爱的亲爱的旅行者！树脂快溢出啦！", message=message)
        
        time.sleep(config.ALERT_SUCCESS_SLEEP_TIME)

    # 半夜委托没做完时
    if(config.INCOMPLETE_ALERT != "" and base_data.finished_task_num != 4):
        time1 = time.strptime(config.INCOMPLETE_ALERT, '%H%M%S')
        time2 = time.localtime()
        if(time2.tm_hour == time1.tm_hour and time2.tm_min >= time1.tm_min or time2.tm_hour > time1.tm_hour and time2.tm_min < time1.tm_min):
            send(status="亲爱的亲爱的亲爱的旅行者！你今日的委托还没有完成哦~", message=message)
            
            time.sleep(config.ALERT_SUCCESS_SLEEP_TIME)


if __name__ == "__main__":
    while True:
        main()
        time.sleep(config.SLEEP_TIME)

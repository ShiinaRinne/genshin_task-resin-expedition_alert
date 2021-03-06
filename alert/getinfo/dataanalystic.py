from .model import BaseData
import datetime
import json
import os

def seconds2hours(seconds: int) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)


def get_resin_data(base_data: BaseData) -> str:
    
    current_resin: str = f"{base_data.current_resin}/{base_data.max_resin}"
    resin_data = f"当前树脂：{current_resin}\n"
    if(base_data.current_resin < 160):
        resin_recovery_time = seconds2hours(base_data.resin_recovery_time)
        next_resin_rec_time = seconds2hours(
            8 * 60 - ((base_data.max_resin - base_data.current_resin) * 8 * 60 - base_data.resin_recovery_time))
        resin_data += f"下个/全部树脂恢复倒计时：{next_resin_rec_time}/{resin_recovery_time}\n"
        overflow_time = datetime.datetime.now() + datetime.timedelta(seconds=base_data.resin_recovery_time)
        day = '今天' if datetime.datetime.now().day == overflow_time.day else '明天'
        resin_data += f"全部树脂恢复时间：{day} {overflow_time.strftime('%X')}"
    return resin_data


def get_resin_discount_data(base_data: BaseData) -> str:
    return f"本周boss战树脂减半剩余使用次数：{base_data.remain_resin_discount_num}/{base_data.resin_discount_num_limit}"


def get_task_num_data(base_data: BaseData) -> str:
    task_num: str = f"{base_data.finished_task_num}/{base_data.total_task_num}"
    return f"今日完成委托数量：{task_num} 奖励{'已' if base_data.is_extra_task_reward_received else '未'}领取\n--------------------"

def get_home_coin_data(base_data: BaseData) -> str:
    week_day_dict = {0: '周一',1: '周二',2: '周三',3: '周四',4: '周五',5: '周六',6: '周日',}
    coin_data = f"当前洞天宝钱/洞天宝钱上限：{base_data.current_home_coin}/{base_data.max_home_coin}\n"
    coin_overflow_time = datetime.datetime.now() + datetime.timedelta(seconds=base_data.home_coin_recovery_time)
    coin_data += f"洞天宝钱全部恢复时间：{week_day_dict[coin_overflow_time.weekday()]} {coin_overflow_time.strftime('%X')}\n--------------------"
    return coin_data

def get_expedition_data(base_data: BaseData) -> str:
    project_path = os.path.dirname(__file__)
    config_file = os.path.join(project_path, '', 'avatar_name.json')
    with open(config_file, 'r', encoding='utf-8') as f:
        avatar_json = json.load(f)

    expedition_info: list[str] = []
    finished = 0
    for expedition in base_data.expeditions:
        avatar: str = expedition['avatar_side_icon'][89:-4]
        try:
            avatar_name: str = avatar_json[avatar]
        except KeyError:
            avatar_name: str = avatar

        if(expedition['status'] == 'Finished'):
            expedition_info.append(f"  · {avatar_name} 已完成")
            finished += 1
        else:
            remained_timed: str = seconds2hours(expedition['remained_time'])
            expedition_info.append(
                f"  · {avatar_name} 未完成，剩余时间{remained_timed}")

    expedition_num: str = f"{base_data.current_expedition_num}/{finished}/{base_data.max_expedition_num}"
    expedition_data: str = "\n".join(expedition_info)
    return f"当前探索派遣总数/完成/上限：{expedition_num}\n详细信息:\n{expedition_data}"

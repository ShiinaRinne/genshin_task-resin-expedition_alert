import pydantic
from pydantic import root_validator, validator
class BaseData(pydantic.BaseModel):
    """
    current_resin=35 当前树脂
    max_resin=160 树脂上限
    resin_discount_num_limit=3  本周剩余树脂减半次数
    resin_recovery_time=59900 树脂恢复时间

    current_expedition_num=5 当前派遣数量
    finished_task_num=0 完成的委托数量
    total_task_num=4 全部委托数量
    is_extra_task_reward_received=False  额外委托？突发事件？不知道~
    max_expedition_num=5 最大派遣数量

    """
    current_resin: int
    max_resin: int
    resin_discount_num_limit: int
    resin_recovery_time:int
    current_expedition_num: int
    finished_task_num:int
    total_task_num:int 
    is_extra_task_reward_received:bool
    max_expedition_num:int

    expeditions:list[dict]
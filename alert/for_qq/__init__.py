from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

from .alert import qq_query

resin = on_command("resin", rule=to_me(), priority=5)


@resin.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["param"] = args  # 如果用户发送了参数则直接赋值


@resin.got("param", prompt="你想对我做些什么呢")
async def handle_param(bot: Bot, event: Event, state: T_State):
    Query_Param = state["param"]
    await resin.finish(qq_query(Query_Param))


async def get_info(param: str):
    return alert.qqmessage()
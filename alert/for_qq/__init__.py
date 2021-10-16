from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

from .alert import alert

resin = on_command("resin", rule=to_me(), priority=5)


@resin.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["param"] = args  # 如果用户发送了参数则直接赋值


@resin.got("param", prompt="你想对我做些什么呢")
async def handle_param(bot: Bot, event: Event, state: T_State):
    param = state["param"]
    # if param not in ["总览"]:
    # if param != "总览":
    #     await resin.reject("功能暂不支持，请重新输入！\n目前支持的有:\n1.总览")
    info = await get_info(param)
    await resin.finish(info)


async def get_info(param: str):
    return alert.qqmessage()
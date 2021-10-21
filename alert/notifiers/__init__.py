from . import (
    dingtalkbot,
    discordwebhook,
    igot,
    pushplus,
    serverchan,
    serverchanturbo,
    telegrambot,
    wechatworkapp,
    wechatworkbot,
    coolpush,
    qmsg, )

from .exceptions import NoSuchNotifierError



_all_notifiers = {
    'dingtalkbot': dingtalkbot.DingTalkBot,
    'discordwebhook': discordwebhook.Discord,
    'igot': igot.Igot,
    'pushplus': pushplus.PushPlus,
    'serverchan': serverchan.ServerChan,
    'serverchanturbo': serverchanturbo.ServerChanTurbo,
    'telegrambot': telegrambot.TelegramBot,
    'wechatworkapp': wechatworkapp.WechatWorkApp,
    'wechatworkbot': wechatworkbot.WechatWorkBot,
    'coolpush': coolpush.CoolPush,
    'qmsg': qmsg.Qmsg,
}


def get_notifiers():
    return list(enumerate(_all_notifiers, start=1))


def get_notifier(name=None):
    notifiers = get_notifiers()
    notifier = [x for x in notifiers if name in x]
    if not notifier:
        raise NoSuchNotifierError(f'No {name} Notifier')
    return _all_notifiers[notifier[0][1]]()


def send2all(text='',status:str='',desp:str=''):
    for notifier in _all_notifiers:
        # 不支持 MARKDOWN 语法的推送渠道不做处理
        if (notifier in ['pushpuls','serverchan','serverchanturbo']):
            markdown_message = f'```{desp}'
        else:
            markdown_message = desp
        get_notifier(notifier).send(text, status, markdown_message)

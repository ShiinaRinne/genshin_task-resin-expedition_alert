from . import (
    dingtalkbot,
    discordwebhook,
    igot,
    pushplus,
    serverchan,
    serverchanturbo,
    telegrambot,
    wechatworkapp,
    wechatworkbot, )

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
}


def get_notifiers():
    return list(enumerate(_all_notifiers, start=1))


def get_notifier(name=None):
    notifiers = get_notifiers()
    notifier = [x for x in notifiers if name in x]
    if not notifier:
        raise NoSuchNotifierError(f'No {name} Notifier')
    return _all_notifiers[notifier[0][1]]()


def send2all(text='from ym',status:str='',desp:str=''):
    for notifier in _all_notifiers:
        get_notifier(notifier).send(text, status, desp)

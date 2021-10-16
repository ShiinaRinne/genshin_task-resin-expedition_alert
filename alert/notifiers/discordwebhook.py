# In order to load the package successfully,
# if the discord_webhook package import fails, it will not be imported.
try:
    from discord_webhook import DiscordWebhook, DiscordEmbed
except Exception as e:
    pass

from .basenotifier import BaseNotifier as Base
from ..config import config
from .utils import log


class Discord(object):
    @staticmethod
    def send(text, status, desp):
        if not config.DISCORD_WEBHOOK:
            # log.info(f'Discord 🚫')
            return

        webhook = DiscordWebhook(url=config.DISCORD_WEBHOOK)
        embed = DiscordEmbed(
            title=f'{text} {status}', description=desp, color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
        if response.status_code == 200:
            log.info(f'Discord 🥳')
        else:
            log.error(f'Discord 😳\n{response}')

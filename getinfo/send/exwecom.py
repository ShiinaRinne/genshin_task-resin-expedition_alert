from typing import Literal
import requests
import json
from ..config import config
import urllib3
urllib3.disable_warnings()


class SendWeixin:
    """
    Call the enterprise wechat interface to send wechat messages
    """

    def __init__(self):  # Message subject and content
        self.corp_id = config.WECOM_CORP_ID
        self.secret = config.WECOM_SECRET

    def get_token(self) -> str:  # Get token
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corp_id}&corpsecret={self.secret}"
        r = requests.get(url=url)
        token = r.json()['access_token']
        return token

    # msgtype: text || markdown
    def send_message(self, title: str, body: str, msgtype: Literal['text', 'markdown'] = 'text') -> None:
        """

        :param msgtype: markdown or text

        but there are some errors in markdown, i have not debugged it yet
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={self.get_token()}"
        data = {
            "touser": config.WECOM_USER_ID,
            "msgtype": msgtype,
            "agentid": config.WECOM_AGENT_ID,
            "text": {
                "content": title + '\n' + body
            },
            "safe": "0"
        }
        r = requests.post(url=url, data=json.dumps(data), verify=False)
        print(r.json())

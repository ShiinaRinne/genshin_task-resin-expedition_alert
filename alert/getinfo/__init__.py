from typing import Dict, Optional, List, Literal, Any

import pydantic
import requests

from .exceptions import APIError
from .headers import headers
from .utils import get_server
from .model import BaseData

session = requests.session()


class Response(pydantic.BaseModel):
    retcode: int
    message: str
    data: Optional[dict]


class MysAPI:
    def __init__(self, role_id: int, cookie: str):
        """

        :param role_id: avatar uid
        """
        self.server: str = get_server(role_id)
        self.role_id: int = role_id
        self.body: dict = {
            'server': self.server,
            'role_id': role_id
        }
        self.cookie: str = cookie
        

    @staticmethod
    def _request(url: str, cookie: str, method: Literal['GET', 'POST'] = 'GET', **kwargs: Any) -> dict:
        query: dict = kwargs.get('params', {})
        body = kwargs.get('data', '')
        response = session.request(method, url, headers=headers.new(
            cookie, query, body), **kwargs).json()
        response = Response.parse_obj(response)
        if response.retcode == 0:
            pass
        elif response.retcode == -10001:  # ds error
            raise RuntimeError(response.message)
        else:
            raise APIError(response.retcode, response.message)
        return response.data

    def get_dailyNote(self) -> Dict:
        url = 'https://api-takumi-record.mihoyo.com/game_record/app/genshin/api/dailyNote'
        return BaseData.parse_obj(self._request(url, params=self.body, cookie=self.cookie))

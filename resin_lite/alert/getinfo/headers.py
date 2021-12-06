import hashlib
import random
import time
from typing import List, Tuple


class Headers:
    def __init__(self) -> None:
        pass

    @staticmethod
    def md5(text: str) -> str:
        md5 = hashlib.md5()
        md5.update(text.encode())
        return md5.hexdigest()

    def getCookie(self) -> Tuple[str, int]:
        return self.cookies[self.cookie_idx], self.cookie_idx

    def create_dynamic_secret(self, query: dict, body: str) -> str:
        parameters: List[str] = [
            f'{k}={query[k]}' for k in sorted(query.keys())]
        q = '&'.join(parameters)

        salt: str = 'xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs'
        time_: str = str(int(time.time()))
        random_ = str(random.randint(100000, 199999))

        check: str = self.md5(
            f"salt={salt}&t={time_}&r={random_}&b={body}&q={q}")

        return ','.join((time_, random_, check))

    def new(self, cookie: str, query: dict, body: str = '') -> dict:
        ds = self.create_dynamic_secret(query, body)
        version: str = '2.11.1'
        return {
            'Accept': 'application/json, text/plain, */*',
            'DS': ds,
            'Origin': 'https://webstatic.mihoyo.com',
            'x-rpc-app_version': version,
            'User-Agent': f'Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.70 Mobile Safari/537.36 miHoYoBBS/{version}',
            'x-rpc-client_type': '5',
            'cookie': cookie,
            'Referer': 'https://webstatic.mihoyo.com/app/community-game-records/index.html?v=6',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,en-US;q=0.8',
            'X-Requested-With': 'com.mihoyo.hyperion'
        }


headers = Headers()

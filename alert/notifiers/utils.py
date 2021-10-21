"""Utilities."""

import logging
import time
import requests



logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

log = logger = logging


def request(method: str,
            url: str,
            max_retries: int = 2,
            params=None,
            data=None,
            json=None,
            headers=None,
            **kwargs):
    # The first HTTP(S) request is not a retry, so need to + 1
    total_requests = max_retries + 1
    for i in range(total_requests):
        try:
            response = requests.Session().request(
                method,
                url,
                params=params,
                data=data,
                json=json,
                headers=headers,
                timeout=21,
                **kwargs)
        except Exception as e:
            log.error(('Request failed: {url}\n{e}').format(
                url=url, e=e
            ))
            if i == max_retries:
                raise Exception(('Request failed ({count}/{total_requests}):\n{e}').format(
                    count=(i + 1), total_requests=total_requests, e=e
                ))

            seconds = 5
            log.info(('Trying to reconnect in {seconds} seconds ({count}/{max_retries})...').format(
                seconds=seconds, count=(i + 1), max_retries=max_retries,
            ))
            time.sleep(seconds)
        else:
            return response

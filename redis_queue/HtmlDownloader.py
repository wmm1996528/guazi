import requests
from bs4 import BeautifulSoup
from redis_queue.redis_db import RedisQueue
import time
from setting import *

class HtmlDownloader(object):
    def __init__(self):
        self.__db = RedisQueue('old')
        self.bool = IP_PROXY
        if self.bool == True:
            self.proxy = self._get_ip()
        else:
            self.proxy = None

    def _get_ip(self):
        try:
            # url = 'http://tvp.daxiangdaili.com/ip/?tid=556862908033437&num=1&protocol=https'
            url = 'http://127.0.0.1:8080/ip'
            ip = requests.get(url).text
            proxy = {
                'http': ip,
                'https': ip,
            }



            print(proxy)
            time.sleep(1)
        except Exception as e:
            logger.debug(e)
            proxy = None
        return proxy

    def download(self, url):
        self.url = url
        if url is None:
            return None


        while True:
            try:
                headers = {
                    'Cookie': 'antipas=584O8218393HQ772r8E8456o7wK5D4;',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
                }
                res = requests.get(self.url, headers=headers, proxies=self.proxy, timeout=2)
                if res.status_code == 200:
                    self.__db.put_old(url)
                    print(res.url)
                    return res.text
                else:
                    logger.warning(res.status_code)
                    print(res.url)
            except Exception as e:
                self.proxy = self._get_ip()
                logger.debug(e)


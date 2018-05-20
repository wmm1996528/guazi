from lxml import etree
from redis_queue.DataOutput import data
import re
from redis_queue import redis_db
from setting import *
import requests
import json
from pyquery import PyQuery as pq
BASE_URL = 'https://www.guazi.com'
class HtmlParser(object):
    def __init__(self):
        self.r = redis_db.RedisQueue('new')
    def parser(self, url, htmls):
        '''
        解析网页
        :param page_url: url
        :param html_cont: content
        :return: url 和数据
        '''
        if htmls == None:
            return
        # try:
        #     h = etree.fromstring(htmls)
        # except Exception as e :
        #     h = etree.HTML(htmls)
        if 'bread' in url:
            self._get_new_urls(url, htmls)
        else:

            self._get_datas(url, htmls)


    def _get_new_urls(self, url, html):
        try:
            urls = re.findall('(/bj/.{0,50}no=\d+)', html)
            for i in urls:
                uri = BASE_URL + i
                print(uri)
                self.r.put(uri)
        except Exception as e:
            logger.debug('error urls %s ' % e)

    def _get_datas(self,url, html):
        h = pq(html)
        title = h.find('.titlebox').text()
        price = h.find('.pricestype').text()
        basic = h.find('.basic-eleven').text()
        datas = {
            'title':title,
            'price':price,
            'basic':basic
        }
        try:
            data.output_mongo(datas)
        except Exception as e :
            logger.debug(e, title, url)
if __name__ == '__main__':
    s = HtmlParser()

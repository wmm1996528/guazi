import logging
logger = logging.getLogger('module')
#设置是否为生产端
# True 生产
# None 消费者
SALVER = True
if SALVER:
    REDIS_URL = "redis://localhost:6379"
else:
    REDIS_URL = "redis://192.168.2.171:6379"


BASE_URL = 'https:'


DATABASE_NAME ='guazi'
TABLE_NAME = 'bj'
#设置最大线程数
PROCESS_BOOL = True
PROCESS_NUM = 10

#设置是否启用代理ip
IP_PROXY = False




HEADERS = {
'Cookie':'antipas=584O8218393HQ772r8E8456o7wK5D4;',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
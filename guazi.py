import requests
from lxml import etree
import time
headers = {
    'Cookie':'antipas=584O8218393HQ772r8E8456o7wK5D4;',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

url = 'https://www.guazi.com/bj/buy/o{}/#bread'
for i in range(1,230):
    url = url.format(i)
    res = requests.get(url,headers=headers)
    print(res.text)

    time.sleep(60)
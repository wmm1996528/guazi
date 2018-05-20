from bs4 import BeautifulSoup
import os
from lxml import etree
from pyquery import PyQuery as pq

f = open('1.html', 'rb')
s = f.read()
h = pq(s)
title = h.find('.titlebox').text()
price = h.find('.pricestype').text()
print(price)
print(title)
basic = h.find('.basic-eleven').text()
print(basic)
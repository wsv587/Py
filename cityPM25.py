# _*_coding:utf-8_*_
import requests
from lxml import etree
import io
import json
import os

url = 'https://www.aqistudy.cn/historydata/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:70.0) Gecko/20100101 Firefox/70.0'
}

response = requests.get(url=url, headers=headers)
response_text = response.text

tree = etree.HTML(response_text)
#container = tree.xpath('//div[@class="container"]')[0]
#print(container)
#category_list = container.xpath('.//div[@class="top"]/text()')
#print('city ', category_list)

#citys = container.xpath('.//div[@class="bottom"]//li/a')

print(response.encoding)
categorys = tree.xpath('//div[@class="top"]/text()')
print(categorys)

city_a_lists = tree.xpath('//div[@class="bottom"]//li/a')
#print(city_lists)
filename = 'cityPM25.txt'
for a in city_a_lists:
    city_href = a.xpath('./@href')[0]
    city_name = a.xpath('./text()')[0]
    print(city_href, city_name)
#    encoding='utf-8' 的方式解码存储 将Unicode转化为普通Python字符串："encode" 
    with io.open(filename, 'a', encoding='utf-8') as fp:
        fp.write(city_name + '\n')



# _*_coding:utf-8_*_

import requests
import io
from lxml import etree
import json
import os
import random

next_page = 'http://www.dianping.com/beijing/ch10/p1'
shop_list = []
# 获取url
def get_url():
    domain = 'http://www.dianping.com/'
    city = input('请输入你要爬取的城市拼音后按回车键(例如:"beijing")')
    url  = domain + city + '/ch10'
    return url

# 获取请求头
def get_headers():
    header_list = [
                   {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:70.0) Gecko/20100101 Firefox/70.0'},
                   {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'},
                   {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'},
                   {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}
    ]
    return random.choice(header_list)

def get_proxy():
    proxy_list = [
#                  {'http': '112.115.57.20:3128'},
#                  {'http': '121.41.171.223:3128'},
#                  {'http': '118.118.234.56:80'},
                  {'https': '180.122.224.30:9999'},
                  {'https': '180.123.233.6:61234'},
#                  {'http': '39.137.69.8:8080'},
#                  {'http': '223.111.131.100:8080'}
                  ]
    return random.choice(proxy_list)

# 发起请求
def get_page_html(url):
#    url = get_url()
    headers = get_headers()
    proxy = get_proxy()
    print(proxy)
    response = requests.get(url=url, headers=headers, proxies=proxy)
    response.encoding = 'utf-8'
    response_text = response.text
    return response_text

# 解析html(xpath)
# 获取每页的商户信息
def get_shop_list(url):
    response_text = get_page_html(url)
    tree = etree.HTML(response_text)
    next_page_a = tree.xpath('//div[@class="page"]/a[@class="next"]')
    if len(next_page_a):
        global next_page
        # 不管是获取自己的子标签还是获取自己的属性，都需要./而不是/
        next_page = next_page_a[0].xpath('./@href')[0]
    else:
        global next_page
        next_page = ''
    try:
        shop_detail_url = tree.xpath('//div[@class="tit"]/a/@href')[0]
    except:
        print('url获取出错')
    global shop_list
    shop_list.append(shop_detail_url)
    print(shop_detail_url)
    return tree

tree = get_shop_list(get_url())
while len(next_page) > 0:
#if len(next_page) > 0:
#    next_url = next_page[0].xpath('./@href')[0]
#    next_num = next_page[0].xpath('./@data-ga-page')[0]
#    print('next_page: ', next_url, 'next_num: ', next_num)
    print('begin catch page:', next_page)
    shop_list = get_shop_list(next_page)

# 请求shop的详情
def get_shop_detail(url):
    response = requests.get(url=url, headers=random.choice(header_list), proxies=random.choice(proxy_list))
    response.encoding = 'utf=8'
    response_text = response.text

def get_shop_info(text):
    tree = etree.HTML(text)
    shop_name = tree.xpath('//h1[@class="shop-name"]/text()')[0]
    shop_phone = tree.xpath('')

##################################################################################################################

def get_food_list(url):
    response_text = get_page_html(url)
    #    print(response_text)
    tree = etree.HTML(response_text)
    current_page_all_foods = tree.xpath('//div[@id="shop-all-list"]/ul/li[@class=""]')
    print(current_page_all_foods)
    shop_list = []
    for food in current_page_all_foods:
        title_a = food.xpath('//div[@class="tit"]/a')[0]
        title_text = title_a.xpath('./h4/text()')[0]
        shop_detail_url = title_a.xpath('./@href')
        #        print('title: ', title_text)
        shop_list.append(shop_detail_url)
        print('shop_detail_url: ', shop_detail_url)
    return shop_list

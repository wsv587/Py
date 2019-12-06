# _*_coding:utf-8_*_
#! /usr/bin/python

import io
import requests
#step_1:指定url
url = 'https://www.sogou.com/'
#step_2:发起请求:使用get方法发起get请求，该方法会返回一个响应对象。参数url表示请求对应的url
response = requests.get(url=url)
#step_3:获取响应数据:通过调用响应对象的text属性，返回响应对象中存储的字符串形式的响应数据（页面源码数据）
page_text = response.text
#print("结果：%s", page_text)
#step_4:持久化存储
#f = io.open('./sougou.html', 'w')
#f.write(page_text)
#f.close()

with io.open('./sogou.html','w+',encoding='utf-8') as fp:
    fp.write(page_text)
print('爬取数据完毕！！！')


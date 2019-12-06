# _*_coding:utf-8_*_
#! /user/bin/python

import requests
import io

#指定搜索关键字
word = input('请输入你要爬取的关键字：')

headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

#指定url
url = 'https://www.sogou.com/web'
param = {
    'query': word,
}

#发起请求
reponse = requests.get(url=url,params=param,headers=headers)

#获取响应数据
page_text = reponse.text
#持久化数据
fileName = word+'.html'
with io.open(fileName, 'w', encoding='utf-8') as fp:
    fp.write(page_text)


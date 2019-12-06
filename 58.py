# _*_encoding:utf-8_*_
#解析出一级页面的标题和二级页面的价格和描述
import requests
import io
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:70.0) Gecko/20100101 Firefox/70.0'
}
url = 'https://bj.58.com/changping/ershoufang/?utm_source=sem-baidu-pc&spm=105916147073.26420796294&PGTID=0d30000c-0000-17fc-4658-9bdfb947934d&ClickID=3'
response = requests.get(url=url,headers=headers)
res_text = response.text
print(res_text)
filename = '58.html'
with io.open(filename, 'w') as f:
    f.write(res_text)
print('html爬取完毕！')

# 读取本地的html文件，xpath提取文件中房源的名称
#tree = etree.parse(filename)
tree = etree.HTML(res_text)
title_list = tree.xpath('//div[@class="list-info"]/h2[@class="title"]/a/text()')
print(title_list)

f = io.open('title.txt', 'a+', encoding='utf-8')
for title in title_list:
    f.write(title+'\n')
#    f.write('\n')

f.close()
print('ok')

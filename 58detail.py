# _*_encoding:utf-8_*_
#解析出一级页面的标题和二级页面的价格和描述
import requests
import io
from lxml import etree
import json

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:70.0) Gecko/20100101 Firefox/70.0'
}
url = 'https://bj.58.com/changping/ershoufang/?utm_source=sem-baidu-pc&spm=105916147073.26420796294&PGTID=0d30000c-0000-17fc-4658-9bdfb947934d&ClickID=3'
response = requests.get(url=url,headers=headers)
res_text = response.text
#print(res_text)
filename = '58.html'
with io.open(filename, 'w') as f:
    f.write(res_text)
print('html爬取完毕！')

# 读取本地的html文件，xpath提取文件中房源的名称
#tree = etree.parse(filename)
# 解析response的text文件
tree = etree.HTML(res_text)
title_list = tree.xpath('//div[@class="list-info"]/h2[@class="title"]/a/text()')
#print(title_list)
detail_url_list = tree.xpath('//div[@class="list-info"]/h2[@class="title"]/a/@href')
#print(detail_url_list)
# 拼接http到链接前
url_list = []
for detail_url in detail_url_list:
    if detail_url.startswith('http') or detail_url.startswith('https'):
        url_list.append(detail_url)
        continue
    detail_url = 'http:' + detail_url
#    print('处理后的url：' + detail_url)
    url_list.append(detail_url)

count = 0
house_detail_list = []
for url in url_list:
    if count > 6:
        break
    count += 1
    
    response = requests.get(url=url)
    detail_text = response.text
    tree = etree.HTML(detail_text)
    title_info = tree.xpath('//div[@class="main-wrap"]//h1[@class="c_333 f20"]/text()')
    price_info = tree.xpath('//div[@id="generalExpense"]//div[@class="general-item-wrap"]//text()')
    desc_info = tree.xpath('//div[@id="generalDesc"]//div[@class="general-item-wrap"]//text()')
    if len(title_info) > 0 and len(price_info):
        print('name: ' + title_info[0])
#        貌似strip只能去除首尾换行和h空格
#        print(''.join(price_info).strip(' \n').strip(' \t'))
#        去除所有的换行和空格
        print('price: ' + ''.join(price_info).replace(' ', '').replace('\n', ''))
        house_detail = {
            'title': title_info[0],
            'price': price_info,
            'desc': desc_info
        }
        house_detail_list.append(house_detail)
# 持久化房源信息
fp = io.open('house.txt', 'a', encoding='utf-8')
for detail in house_detail_list:
#    fp.write(detail.decode('gbk'))
#    fp.write(unicode(str(detail), 'utf-8'))

#    fp.write(str(detail).encode('iso-8859-1').decode('utf-8'))
    fp.write(str(detail).encode('utf-9'))
fp.close()

# 持久化房源标题
f = io.open('title.txt', 'a+', encoding='utf-8')
for title in title_list:
    f.write(title+'\n')
#    f.write('\n')

f.close()
print('ok')



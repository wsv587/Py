# _*_encoding:utf-8_*_
import requests
import io
from lxml import etree
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:70.0) Gecko/20100101 Firefox/70.0'
}

url = 'http://jandan.net/ooxx'

response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
response_text = response.text

tree = etree.HTML(response_text)
li_list = tree.xpath('//ol[@class="commentlist"]/li')

img_url_list = []
img_info_list = []

for li in li_list:
    
    path_list = li.xpath('.//div[@class="text"]//img/@src')
    if len(path_list) <= 0:
        continue
    img_path = path_list[0]
    print(img_path)
    if not img_path.startswith('http'):
        img_path = 'http:' + img_path
    img_url_list.append(img_path)
    img_name = img_path.split('/')[-1] + '.jpg'
    print(img_name)
    img_info = {
        'name': img_name,
        'url': img_path
    }
    img_info_list.append(img_info)

dirname = './jiandan'
if not os.path.exists(dirname):
    os.mkdir(dirname)
os.chdir(dirname)
for info in img_info_list:
    img_data = requests.get(url=info['url']).content
    with io.open(info['name'], 'wb') as fp:
        fp.write(img_data)
    print(info['name'], '下载完毕!')


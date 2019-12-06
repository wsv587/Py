# _*_encoding:utf-8_*_
import requests
import io
import os
from lxml import etree

url = 'http://pic.netbian.com/4kmeinv/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:70.0) Gecko/20100101 Firefox/70.0'
}
response_text = requests.get(url=url, headers=headers).text
print(response_text)

tree = etree.HTML(response_text)
# 解析src属性中的图片路径和alt属性中的图片名称
img_path_list = tree.xpath('//div[@class="slist"]/ul//img/@src')
img_name_list = tree.xpath('//div[@class="slist"]/ul//img/@alt')
img_url_list = []
# 拼接图片url
for img_path in img_path_list:
    img_url = 'http://pic.netbian.com' + img_path
    img_url_list.append(img_url)
    print(img_url)

for img_name in img_name_list:
    print(img_name.encode('iso-8859-1').decode('gbk'))

# 创建img文件夹
if not os.path.exists('./img'):
    os.mkdir('./img')
# 切换到img文件夹
os.chdir('./img')
for idx in range(len(img_url_list)):
#    获取二进制使用content
    img_data = requests.get(url=img_url_list[idx]).content
    print(img_data)
#    img的alt文件名称作为本地图片名
#    先编码再解码 去除空格
    filename = img_name_list[idx].encode('iso-8859-1').decode('gbk').replace(' ', '') + '.jpg'
    f = io.open(filename, 'wb')
    f.write(img_data)
    f.close()




#http://pic.netbian.com/uploads/allimg/191121/223811-15743470919c9f.jpg
#                      /uploads/allimg/191121/223811-1574347091a133.jpg

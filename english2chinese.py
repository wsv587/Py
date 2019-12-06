
# _*_encoding:utf-8_*_
#https://fanyi.baidu.com/?aldtype=16047#zh/en/

import requests
import io

word = input("请输入你要翻译的汉字：")
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
url = 'https://fanyi.baidu.com/?aldtype=16047#zh/en/'
#word = input('请求输入要翻译的汉语：')
data = {
    'kw': word
}

reponse = requests.post(url=url, headers=headers, data= data)
filename = '翻译' + word + '.html'
with io.open(filename, 'w') as f:
    f.write(reponse.text)
print("爬取完毕！")


# _*_encoding:utf-8_*_
import requests
import io
import json

city = input('请输入要查询哪个城市的KFC:')
url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:70.0) Gecko/20100101 Firefox/70.0'
}
data = {
    'cname': '',
    'pid': '',
    'keyword': city,
    'pageIndex': 1,
    'pageSize': 20
}

response = requests.post(url=url, headers=headers, data=data)
print(response.text)
filename = 'KFC_' + city + '.json'
f = io.open(filename, 'a', encoding='utf-8')
f.write(response.text)
#json.dump(response.json(),fp = f, ensure_ascii=False)
f.close()

print('爬取完毕！')
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword

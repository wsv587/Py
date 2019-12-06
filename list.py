#_*_encoding:utf-8_*_
import requests
import io
import json
list_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
list_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:70.0) Gecko/20100101 Firefox/70.0'
}

list_data = {
    'on': 'true',
    'page': '1',
    'pageSize': '15',
    'productName': '',
    'conditionType': 1,
    'applyname': '',
    'applysn': ''
}

list_response = requests.post(url=list_url, headers=list_headers, data=list_data)
# print(list_response.json())
listJSON = list_response.json()

ids = []
for obj in listJSON['list']:
    id = obj['ID']
    ids.append(id)

detail_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
detail_headers = list_headers
filename = 'list.json'
f = io.open(filename, 'a+')

for id in ids:
    detail_data = {
        'id':id
    }
    detail_reponse = requests.post(url=detail_url, headers=detail_headers, data=detail_data)
# 打印json中的法人姓名
    jsondata = detail_reponse.json()
    print(jsondata['businessPerson'])
# 写数据
#f.write(detail_reponse.text)
    json.dump(detail_reponse.text, fp=f, ensure_ascii=False)

f.close()
print('爬取完毕！')




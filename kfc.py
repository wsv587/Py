#_*_encoding:utf-8_*_
import requests
#指定ajax-post请求的url（通过抓包进行获取）
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
#定制请求头信息，相关的头信息必须封装在字典结构中
headers = {
    #定制请求头中的User-Agent参数，当然也可以定制请求头中其他的参数
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}
#定制post请求携带的参数(从抓包工具中获取)
data = {
    'cname':'',
    'pid':'',
    'keyword':'北京',
    'pageIndex': '1',
    'pageSize': '10'
}
#发起post请求，获取响应对象
response = requests.post(url=url,headers=headers,data=data)
#获取响应内容
print(response.text)



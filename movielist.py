
# https://raw.githubusercontent.com/facebook/react-native/0.51-stable/docs/MoviesExample.json
# _*_encoding:utf-8_*_
import requests
url = 'https://raw.githubusercontent.com/facebook/react-native/0.51-stable/docs/MoviesExample.json'

headers = {}

response = requests.get(url=url, headers=headers)

print(response.text)


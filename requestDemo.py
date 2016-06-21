import requests

r = requests.get('https://baidu.com')

tb = requests.get('https://taobao.com')

wb = requests.get('http://weibo.cn/pub')

print wb.text

print wb.headers

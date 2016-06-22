import requests

r = requests.get('https://baidu.com')

tb = requests.get('https://taobao.com')



def gettext(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',}
    text = requests.get(url, headers=head).text

    return text

t = gettext('http://www.weibo.cn')

print t

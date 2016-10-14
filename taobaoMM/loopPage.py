#/usr/bin/python
# -*- coding:utf-8 *-

import requests
import urllib
from bs4 import BeautifulSoup
from urllib2 import HTTPError


def gettext(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'#,
        #'Cookie:'
    }
    try:
        req = requests.get(url, headers=head)
        req.encoding = 'gb18030'
        return req.text
    except requests.ConnectionError as e:
        return None

#get hyper link for tag a
def getInfor(htmltext):
    soup = BeautifulSoup(htmltext, 'html.parser')
    p = soup.find_all('p')
    p_contents = []
    for i in p:
        p_contents.append(i.contents[0])
    return p_contents

def main():
    url = 'https://mm.taobao.com/self/info/model_info_show.htm?user_id=631300490'

    #'/mm.taobao.com/self/info/model_info_show.htm?user_id=631300490 '

    html = gettext(url)
    list = getInfor(html)
    for i in list[:5]:
        print i


if __name__ == '__main__':
    main()
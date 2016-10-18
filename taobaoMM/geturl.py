#/usr/bin/python
# -*- coding:utf-8 *-
import re
import time
import requests
import urllib
from bs4 import BeautifulSoup
from urllib2 import HTTPError
from loopPage import *


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

#get name and
def getHref(htmltext):
    soup = BeautifulSoup(htmltext, 'html.parser')
    aTag = soup.find_all('a',{'class':'lady-name'})
    # key:name, valur:url id number
    values = []
    for i in aTag:
        i.encode('utf-8')
        # k = i.string
        id = reId(i.get('href'))
        values.append(id)# filter id
        # infor[k] = v

    return values
    # for k in infor:
        # print "name: %s,  url: %s \n" % (k, infor[k])
        # print k + "\t\t"+ infor[k]

#use regular get id num form url
def reId(url):
    id = re.sub(r'\D','',url)
    return id

def main(page):
    url = 'https://mm.taobao.com/json/request_top_list.htm?page=' + str(page)
    htmltext = gettext(url)
    ID = getHref(htmltext)

    list = []
    (x, y, z) = db_pwd()
    for i in ID:
        url = 'https://mm.taobao.com/self/info/model_info_show.htm?user_id=' + str(i)
        html = gettext(url)
        list = getInfor(html)  # list is information list

        print connect_mysql(x, y, z, list)


    # for k,v in infor:
    #     print "name: %s,  url: %s \n"%(k,v)

if __name__ =='__main__':

    # 16/10/18 get the page 1 to 9 (1,10)
    for page in range(1,10):
        main(page)
        time.sleep(0.5)

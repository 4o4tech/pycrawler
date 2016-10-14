#/usr/bin/python
# -*- coding:utf-8 *-
import requests
import urllib
import time
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
def getHref(htmltext):
    soup = BeautifulSoup(htmltext, 'html.parser')
    aTag = soup.find_all('a',{'class':'lady-name'})

    infor = {}
    for i in aTag:
        i.encode('utf-8')
        k = i.string
        v = i.get('href')
        infor[k] = v

    for k in infor:
        print "name: %s,  url: %s \n" % (k, infor[k])
        # print k + "\t\t"+ infor[k]



def main(page):
    url = 'https://mm.taobao.com/json/request_top_list.htm?page=' + str(page)
    # print url s
    htmltext = gettext(url)
    infor = getHref(htmltext)
    # for k,v in infor:
    #     print "name: %s,  url: %s \n"%(k,v)

if __name__ =='__main__':
    for page in range(1,3):
        main(page)
        time.sleep(0.5)
''' the code still have the encode problem, can't show the chinese at the output'''
 

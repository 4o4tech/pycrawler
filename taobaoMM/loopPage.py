#/usr/bin/python
# -*- coding:utf-8 *-

import MySQLdb
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
    contents = []
    soup = BeautifulSoup(htmltext, 'html.parser')

    span = soup.find_all('span')
    contents.append(span[1]) # add name in list

    p = soup.find_all('p')
    for i in p[:5]:
        contents.append(i.contents[0]) # add height,weight,size,bar,hose in list

    img_url = soup.find('img').get('src') #img url
    contents.append(img_url) # add img_url list
    return contents

'''
height 168CM
weight 45.0KG
size 82-59-86
bar 32B
shose 37码
img_url  //gtd.alicdn.com/imgextra/i1/T1S35PXpXeXXb1upjX.jpg
'''

def connect_mysql(db_host="127.0.0.1:3306", user="root",
                   passwd="Jmz5278",db="practice", charset="utf8"):
    try:
        conn = MySQLdb.connect(host=db_host, user=user, passwd=passwd, db=db, charset=charset)
        conn.autocommit(True)
        sql = 'INSERT INTO `taobaomodle` (`name`,`height`,`weight`,`size`,`bar`, `shose`) VALUES (%s,%s,%s,%s,%s,%s)'

        cur = conn.cursor()
        value = [('崔辰辰','168CM','45.0KG','82-59-86','32B','37码','//gtd.alicdn.com/imgextra/i1/T1S35PXpXeXXb1upjX.jpg')]
        cur.excute(sql,value)

        # values = []
        # for i in range(20):
        #     values.append((i, 'hi rollen' + str(i)))
        #
        # cur.executemany('insert into test values(%s,%s)', values)
    except MySQLdb.Error,e:
        print "error"

def main():
    id = [37448401,631300490]
    for i in id:
        url = 'https://mm.taobao.com/self/info/model_info_show.htm?user_id=' + str(i)
        html = gettext(url)
        list = getInfor(html) # list is information list

    #'/mm.taobao.com/self/info/model_info_show.htm?user_id=631300490 '


if __name__ == '__main__':
    main()
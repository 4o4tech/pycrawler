#/usr/bin/python
# -*- coding:utf-8 *-

import MySQLdb
import requests
import urllib
from bs4 import BeautifulSoup
from urllib2 import HTTPError



sql = 'INSERT INTO `taobaomodle` (`name`,`height`,`weight`,`size`,`bar`, `shose`) VALUES (%s,%s,%s,%s,%s,%s)'
# sql_tmp = 'INSERT INTO `taobaomodle` (`startip`,`endip`,`country`,`local`) VALUES (%s, %s, %s, %s)'
values = [(16890112,16891391,"泰国","曼谷"),(16891392,16891647,"泰国","如果硅农"), (16891648,16892159,"泰国","加拉信府")]



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
    contents = []
    for i in p[:5]:
        contents.append(i.contents[0])
    img_url = soup.find('img').get('src')
    contents.append(img_url)
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
    conn = MySQLdb.connect(host=db_host, user=user, passwd=passwd, db=db, charset=charset)
    conn.autocommit(True)
    return conn.cursor()
db1 = connect_mysql()
# print db1.execute(sql), db1.lastrowid
print db1.executemany(sql, values), db1.lastrowid


def main():
    url = 'https://mm.taobao.com/self/info/model_info_show.htm?user_id=631300490'

    #'/mm.taobao.com/self/info/model_info_show.htm?user_id=631300490 '

    html = gettext(url)
    list = getInfor(html)
    for i in list:
        print i


if __name__ == '__main__':
    main()
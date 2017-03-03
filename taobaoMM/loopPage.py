#/usr/bin/python
# -*- coding:utf-8 *-
import re
import os
import pymysql
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
    contents.append(span[1].string) # add name in list

    p = soup.find_all('p')
    for i in p[:5]:
        # print i
        try:
            str = i.contents[0]
        except:
            pass

        contents.append(str) # add height,weight,size,bar,hose in list

    contents = filterNum(contents)

    img_url = soup.find('img').get('src') #img url
    contents.append(img_url) # add img_url list
    return tuple(contents)


def filterNum(list):
    list[1] = re.sub(r'[a-zA-Z]','',list[1])
    list[2] = re.sub(r'[a-zA-Z]','',list[2])
    return list

'''
height 168CM
weight 45.0KG
size 82-59-86
bar 32B
shose 37码
img_url  //gtd.alicdn.com/imgextra/i1/T1S35PXpXeXXb1upjX.jpg
'''


def db_pwd():
    #path = os.path.abspath('/home/jimze/db.txt')
    path = os.path.abspath('f:/db.txt')
    dbFile = open(path)
    db= dbFile.readlines()

    db_host = db[0].strip()
    user = db[1].strip()
    passwd = db[2].strip()
    return (db_host,user,passwd)



def connect_mysql(id):

    (x, y, z) = db_pwd()

    try:
        conn = pymysql.connect(host=x, user=y, passwd=z, db='mydb', charset='utf8',port=3306)
        sql = "insert ignore into taobaomodle values (%s,%s,%s,%s,%s,%s,%s)"

        cur = conn.cursor()

        values = getList(id)
        #['崔辰辰','168CM','45.0KG','82-59-86','32B','37码','//gtd.alicdn.com/imgextra/i1/T1S35PXpXeXXb1upjX.jpg']
        # cur.execute(sql, value)
        cur.executemany(sql,values)

        conn.commit()
        cur.close()
        conn.close()

        print len(values)

        # values = []
        # for i in range(20):
        #     values.append((i, 'hi rollen' + str(i)))
        #
        # cur.executemany('insert into test values(%s,%s)', values)
    except pymysql.Error, e:
        print  "Mysql Error %d : %s" % (e.args[0],e.args[1])

def getList(id):
    values = []
    for i in id:
        url = 'https://mm.taobao.com/self/info/model_info_show.htm?user_id=' + str(i)
        html = gettext(url)
        list = getInfor(html)
        values.append(list)  # list is information list
    return values

def main():

    # id = [33197951,37448401, 631300490]
    # print getList(id)
    connect_mysql(id)

if __name__ == '__main__':
    main()
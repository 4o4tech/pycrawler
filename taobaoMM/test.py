# -*- coding: UTF-8 -*-
import MySQLdb

import os


'''
  try:
        conn = MySQLdb.connect(host=db_host, user=user, passwd=passwd, db=db, charset=charset)
        cur = conn.cursor()
        print "connect"
    except MySQLdb.Error, e:
        print  e
'''

def db_pwd():
    path = os.path.abspath('/home/jimze/db.txt')
    # path = os.path.abspath('g:/db.txt')
    dbFile = open(path)
    db= dbFile.readlines()

    db_host = db[0].strip()
    user = db[1].strip()
    passwd = db[2].strip()
    return (db_host,user,passwd)



def connect_mysql(db_host, user,passwd):
    db = "practice"
    charset = "utf8"
    try:
        conn = MySQLdb.connect(host=db_host, user=user, passwd=passwd, db=db, charset=charset)
        sql = "insert into taobaomodle values (%s,%s,%s,%s,%s,%s,%s)"

        cur = conn.cursor()

        value = ['崔辰辰', '168.0', '45.0', '82-59-86', '32B', '37码', 'i1/T1S35PXpXeXXb1upjX.jpg']
        #'崔辰辰','168CM','45.0KG','82-59-86','32B','37码','//gtd.alicdn.com/imgextra/i1/T1S35PXpXeXXb1upjX.jpg'
        cur.execute(sql, value)
        # cur.executemany(sql,value)

        conn.commit()
        cur.close()
        conn.close()

        # values = []
        # for i in range(20):
        #     values.append((i, 'hi rollen' + str(i)))
        #
        # cur.executemany('insert into test values(%s,%s)', values)
    except MySQLdb.Error, e:
        print  "Mysql Error %d : %s" % (e.args[0],e.args[1])


def main():

    (x,y,z) = db_pwd()

    connect_mysql(x,y,z)

    print "Down"


if __name__ == '__main__':
    main()

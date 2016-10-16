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
    dbInf= dbFile.readlines()
    return dbInf



def connect_mysql(db_host="45.78.7.228", user="root",passwd="zjz5278"):
    db = "practice"
    charset = "utf8"
    try:
        conn = MySQLdb.connect(host=db_host, user=user, passwd=passwd, db=db, charset=charset)
        sql = "insert into taobaomodle values (%s,%s,%s,%s,%s,%s,%s)"

        cur = conn.cursor()

        value = ['崔辰辰', '168.0', '45.0', '82-59-86', '32B', '37码', 'i1/T1S35PXpXeXXb1upjX.jpg']
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

    db = db_pwd()
    db_host = db[0]
    user = db[1]
    passwd = db[2]

    # connect_mysql(db_host,user,passwd)


    print "finished"


if __name__ == '__main__':
    main()

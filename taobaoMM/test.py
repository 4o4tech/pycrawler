import MySQLdb


def connect_mysql(db_host="127.0.0.1:3306", user="root",
                  passwd="Jmz5278", db="practice", charset="utf8"):


    try:
        conn = MySQLdb.connect(host=db_host, user=user, passwd=passwd, db=db, charset=charset)
        conn.autocommit(True)
        sql = 'INSERT INTO `taobaomodle` (`name`,`height`,`weight`,`size`,`bar`, `shose`) VALUES (%s,%s,%s,%s,%s,%s)'

        cur = conn.cursor()
        value = [
            ('崔辰辰', '168CM', '45.0KG', '82-59-86', '32B', '37码', '//gtd.alicdn.com/imgextra/i1/T1S35PXpXeXXb1upjX.jpg')]
        cur.excute(sql, value)

        # values = []
        # for i in range(20):
        #     values.append((i, 'hi rollen' + str(i)))
        #
        # cur.executemany('insert into test values(%s,%s)', values)
    except MySQLdb.Error, e:
        print "error"

connect_mysql()
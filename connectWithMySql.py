#!/usr/bin/python
#coding:utf-8

import MySQLdb

conn = MySQLdb.connect(user='root',passwd='',host='127.0.0.1')
cur = conn.cursor()
conn.select_db('week')

# insert info into database
sqlim = "insert into userinfo(name, age, gender) values(%s,%s,%s)"
cur.executemany(sqlim,[('first',90,'f'),('second',50,'m'),('third',51,'m')])

# delete element from database
cur.execute('delete frem userinfo where id = 1')

# update info in database
cur.execute("update userinfo set name='again' where id = 2")

# search all info in table of database
cur.execute("select * from userinfo")
cur.fetchone()
cur.fetchone()
cur.fetchone()
cur.fetchone()

## move cursor back to beginning
cur.scroll(0,'absolute')

cur.fetchmany(13)
### or
cur.fetchmany(cur.execute("select * from userinfo"))

# close all
cur.close()
conn.close()
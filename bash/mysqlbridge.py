#!/usr/bin/python

import sys
import pymysql

db_host = 'localhost'
db_user = 'root'
db_pass = 'root'
db_name = 'tealinuxstudios'
querry = ''
# usage: mysqlbridge query

db = pymysql.connect(host=db_host, user=db_user, passwd=db_pass, db=db_name)
cur = db.cursor()

q = sys.argv[1:]
# print(q)
for arg in q:
    querry += str(arg)+' '
querry = querry.strip('\\')
# print(querry)
cur.execute(querry)
db.commit()
temp = cur.fetchall()
# print(temp)
for row in temp:
    p = ''
    for column in row:
        p += str(column)+' '
    print(p)

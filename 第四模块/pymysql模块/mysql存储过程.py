#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving
import pymysql

# 链接
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    db='db6',
    charset='utf8'
)

# 游标
cursor = conn.cursor(pymysql.cursors.DictCursor)

cursor.callproc('p4', (3,))
print(cursor.fetchall())

cursor.execute('select @_p4_0;')
print(cursor.fetchall())
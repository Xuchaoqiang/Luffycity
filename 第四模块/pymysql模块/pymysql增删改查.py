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
    db='db5',
    charset='utf8'
)

# 游标
cursor = conn.cursor()

# 执行sql语句
# sql = 'insert into userinfo(user,pwd) values("root","123456");'
# res = sursor.execute(sql)       # 执行sql语句，返回sql影响成功的行数
# print(res)

sql = 'insert into userinfo(user,pwd) values(%s,%s);'
res = cursor.executemany(sql, [('egon11', '123'), ('egon12', '123'), ('egon13', '123')])
print(cursor.lastrowid)
print(res)

# sql = 'DELETE FROM userinfo WHERE id = %s'
# res = cursor.execute(sql, (10,))

conn.commit()
cursor.close()
conn.close()


# ----查

# 链接
# conn = pymysql.connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     password='',
#     db='db5',
#     charset='utf8'
# )
#
# # 游标
# cursor = conn.cursor(pymysql.cursors.DictCursor)
#
# sql = 'SELECT * FROM userinfo;'
# rows = cursor.execute(sql)  # 执行sql语句，返回影响成功的行数rows，将结果放入一个集合，等待被查询
#
# res1 = cursor.fetchone()
# res2 = cursor.fetchone()
# cursor.scroll(0, mode='absolute')
# res3 = cursor.fetchall()
# print(res1)
# print(res2)
# print(res3)
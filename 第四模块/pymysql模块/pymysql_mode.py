#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

# import pymysql
#
# user = input('user>>:').strip()
# pwd = input('password>>:').strip()
#
# # 建立链接
# conn = pymysql.connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     password='',
#     db='db5',
#     charset='utf8'
# )
#
# # 拿到游标，用来执行sql
# cursor = conn.cursor()
#
# # 执行sql语句
# # sql注入 hello" or 1=1 -- xxxx
# # sql = 'select * from userinfo where user="{}" and pwd="{}"'.format(user, pwd)
#
# sql = 'select * from userinfo where user=%s and pwd=%s'
# print(sql)
# rows = cursor.execute(sql, (user, pwd))
#
# cursor.close()
# conn.close()
#
# # 进行判断
# if rows:
#     print('登陆成功')
# else:
#     print('登陆失败')




import pymysql

user = input('username>>:').strip()
password = input('password>>:').strip()

# 链接
conn = pymysql.connect(host='localhost', user='root', password='', database='db5', charset='utf8')

# 游标
cursor=conn.cursor() #执行完毕返回的结果集默认以元组显示
#cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)


# 执行sql语句
sql = 'SELECT * FROM userinfo WHERE user="%s" and pwd="%s"' % (user, password)#注意%s需要加引号
print(sql)

res = cursor.execute(sql)#执行sql语句，返回sql查询成功的记录数目

print(res)

if res:
    print('登陆成功')
else:
    print('登陆失败')
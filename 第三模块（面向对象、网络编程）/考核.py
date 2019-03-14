#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

# def sayhi(self, name):
#     print('self', name, self, name)
#
# Test = type('Test', (object,) ,{'sayhai': sayhi,'name':'alex'})
#
# t1 = Test()
# t1.sayhai('name')

# import socket
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# server.bind(('localhost', 9090))
# server.listen(5)
#
# while True:
#     conn, addr = server.accept()
#
#     while True:
#         cmd = conn.recv(1024)
#         print(cmd.decode('utf-8'))
#         conn.send(cmd.upper())
#
#     conn.close()
#
# server.close()

# 创建类主要分为三部分
# 1 类名
# 2 类的父类    元组！
# 3 类体         字典！

# class类名
class_name = 'Chinese'

# 类的父体
class_bases = (object, )

# 类体
class_body = '''
country='China'
def __init__(self,name,age):
    self.name=name
    self.age=age
def talk(self):
    print('%s is talking' %self.name)
'''

class_dic = {}
exec(class_body, globals(), class_dic)

Foo = type(class_name, class_bases, class_dic)
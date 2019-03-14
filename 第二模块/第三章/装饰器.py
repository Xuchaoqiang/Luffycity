#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving


# user_status = False #用户登录了就把这个改成True
#
# # 用户验证模块
# def login(func):
#     def inner():
#         _username = "alex"  # 假装这是DB里存的用户信息
#         _password = "abc!23"  # 假装这是DB里存的用户信息
#         global user_status
#
#         if user_status == False:
#             username = input("user:")
#             password = input("pasword:")
#
#             if username == _username and password == _password:
#                 print("welcome login....")
#                 user_status = True
#             else:
#                 print("wrong username or password!")
#         if user_status == True:
#             func()
#     return inner
#
#
# def home():
#     print("---首页----")
#
# def america():
#     print("----欧美专区----")
#
# def japan():
#     print("----日韩专区----")
#
# @login   #等同于 henan = login(henan)   @->相当于把henan当作参数先传给login函数执行了一遍
# def henan():
#     print("----河南专区----")
#
# # 装饰器原则：不修改源代码；不改变源代码的调用方式
# # henan = login(henan)        # 没调用henan就执行
#
# # 用了高阶函数（传入的参数为函数名，返回值包含函数名） 嵌套函数（用来返回内层函数的内存地址给予调用）
# # henan = login(henan)
# henan()


# #带参数(被修饰的函数带参数。)
#
# user_status = False #用户登录了就把这个改成True
#
# # 用户验证模块
# def login(func):
#     def inner(*args, **kwargs):
#         _username = "alex"  # 假装这是DB里存的用户信息
#         _password = "abc!23"  # 假装这是DB里存的用户信息
#         global user_status
#
#         if user_status == False:
#             username = input("user:")
#             password = input("pasword:")
#
#             if username == _username and password == _password:
#                 print("welcome login....")
#                 user_status = True
#             else:
#                 print("wrong username or password!")
#         if user_status == True:
#             func(*args, **kwargs)
#     return inner
#
#
# def home():
#     print("---首页----")
#
# def america():
#     print("----欧美专区----")
#
# @login
# def japan():
#     print("----日韩专区----")
#
# @login
# def henan(style):
#     print("----河南专区----", style)
#
# # 装饰器原则：不修改源代码；不改变源代码的调用方式
# # henan = login(henan)        # 没调用henan就执行
#
# # 用了高阶函数（传入的参数为函数名，返回值包含函数名） 嵌套函数（用来返回内层函数的内存地址给予调用）
#
# japan()
# henan('3p')


#带参数(装饰器带参数。)

user_status = False #用户登录了就把这个改成True

# 用户验证模块
def login(*args):
    def outer(func):
        def inner(*args, **kwargs):
            _username = "alex"  # 假装这是DB里存的用户信息
            _password = "abc!23"  # 假装这是DB里存的用户信息
            global user_status

            if user_status == False:
                username = input("user:")
                password = input("pasword:")

                if username == _username and password == _password:
                    print("welcome login....")
                    user_status = True
                else:
                    print("wrong username or password!")
            if user_status == True:
                func(*args, **kwargs)
        return inner
    return outer

def home():
    print("---首页----")

def america():
    print("----欧美专区----")

@login
def japan():
    print("----日韩专区----")

@login('qq')   # 等同于 先把'qq'参数传给login函数执行一遍，返回outer函数地址，然后再outer(henan), 然后得到inter的函数地址，然后就可以重新赋值 henan = inter(henan)
def henan(style):
    print("----河南专区----", style)

# 装饰器原则：不修改源代码；不改变源代码的调用方式
# henan = login(henan)        # 没调用henan就执行

# 用了高阶函数（传入的参数为函数名，返回值包含函数名） 嵌套函数（用来返回内层函数的内存地址给予调用）

japan()
henan('3p')
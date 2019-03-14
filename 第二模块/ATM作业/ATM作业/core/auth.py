#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

from core import db_handler
from conf import settings
HANDLING_FEE = settings.HANDLING_FEE        # 提现手续费

user_data = []      # 用来存当前登陆用户的数据， 给被装饰的函数用
login_status = False        # 用户登陆状态，用来判断用户进行其他操作是否在登陆状态

def auth_login(func):
    """
    用户认证装饰器
    :param func:
    :return:
    """
    def inner(*args, **kwargs):
        global login_status     # 声明全局变量 login_status
        if not login_status:    # 当login_status状态为False时，用户是未登录状态，进行登陆操作
            username = input('username >>: ').strip()
            data = db_handler.load_db(username)     # 加载用户数据
            user_data.append(data)          # 用来存当前登陆用户的数据（字典格式）， 给被装饰的函数用
            password = input('password >>: ').strip()
            if password == data['password']:
                if user_data[0]['status'] == 0:     # 判断用户是否被冻结， '0'代表正常， '1'代表已冻结
                    login_status = True
                    func(*args, **kwargs)
                else:
                    print('用户已被冻结！')
        elif login_status:
            func(*args, **kwargs)
    return inner

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import os
import json
import time
import hashlib

def load_db(username):
    with open(username+'.json', 'r') as f:
        user_info = json.load(f)
        return user_info

def count_time(t_time):
    user_time = time.mktime(time.strptime(t_time, '%Y-%m-%d'))
    now_time = time.time()
    return now_time < user_time

def save_db(username, user_info):
    with open(username+'.json', 'w') as f:
        json.dump(user_info, f)


count = 0
while count < 3:
    username = input('username:').strip()
    if os.path.isfile(username+'.json'):
        user_info = load_db(username)
        password = input('password:').strip()
        password_hash = hashlib.md5()
        password_hash.update(password.encode('utf-8'))
        if user_info['status'] == 1:
            print('用户处于锁定状态！')
        elif password_hash.hexdigest() == user_info['password']:
            if count_time(user_info['expire_date']):
                print('登陆成功！')
            else:
                print('账户已过期！')
        elif count == 2:
            user_info['status'] = 1
            print('用户已被锁定！')
            save_db(username,user_info)
        else:
            print('密码错误！')
            count += 1
    else:
        print('用户不存在！')

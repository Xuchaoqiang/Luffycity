#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import json
import os
import sys

MENU = """
--------- Luffy Bank ----------
1.  账户信息
2.  转账
3.  提现"""
BASE_dIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_dIR)
INTEREST = 0.05
login_status = False

def login_auth(func):
    def inner(*args, **kwargs):
        if login_status:
            func(*args, **kwargs)
        else:
            username = input('username:').strip()
            if os.path.isfile(BASE_dIR+r'\account\%s.json' % username):
                user_data = load_db(username)
                password = input('password:').strip()
                if password == user_data[username]['password']:
                    func(*args, **kwargs)
                    global login_status
                    login_status = True
                else:
                    print('密码错误！')
            else:
                print('用户不存在！')
    return inner

def init_db():
    luffy_acount = {'luffy': {'account': 1000000, 'credit_value': 50000, 'password': 'abc123'}}
    tesla_acount = {'tesla': {'account': 0}}
    with open(BASE_dIR+r'\account\luffy.json', 'w', encoding='utf-8') as f:
        json.dump(luffy_acount, f)

    with open(BASE_dIR+r'\account\tesla.json', 'w', encoding='utf-8') as f2:
        json.dump(tesla_acount, f2)

def load_db(name):
    with open(BASE_dIR+r'\account\%s.json' % name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data

def save_db(name, data):
    with open(BASE_dIR+r'\account\%s.json' % name, 'w', encoding='utf-8') as f:
        json.dump(data, f)

@login_auth
def transfer(source, target, cost):
    source_data = load_db(source)
    target_data = load_db(target)
    cost = int(cost)
    all_cost = cost * INTEREST + cost
    source_data[source]['account'] = int(source_data[source]['account']) - all_cost
    target_data[target]['account'] = int(target_data[target]['account']) + all_cost
    save_db(source, source_data)
    save_db(target, target_data)
    print('转账成功！')

@login_auth
def with_draw(name):
    user_info = load_db(name)
    credit_value = int(user_info[name]['credit_value'])
    print('您的信用额度为：%s' %credit_value)
    money = input('How many you want to withdraw: ').strip()
    money = int(money)
    if money <= credit_value:
        all_cost = money + money* INTEREST
        user_info[name]['account'] = int(user_info[name]['account']) - all_cost
        print('提现成功!')
        save_db(name, user_info)
    else:
        print('抱歉，你提现的额度大于你的信用额度。')


# init_db()
while True:
    print(MENU)
    choice = input('>>: ').strip()
    if choice == '1':
        pass
        # print(luffy_data)
    elif choice == '2':
        transfer('luffy', 'tesla', 700000)
    elif choice == '3':
        with_draw('luffy')

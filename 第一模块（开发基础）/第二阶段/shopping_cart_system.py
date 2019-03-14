#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

#! _*_coding:utf-8 _*_
#__author__:"Irving"
import json
import os


goods = [
    {'name': '电脑', 'price': 1999},
    {'name': '鼠标', 'price': 10},
    {'name': '游艇', 'price': 20},
    {'name': '美女', 'price': 998}
]

#状态码，用于判断随时退出程序
status_code = True
#存放用户信息的字典
user_info = {'alex': {'password': '123456'}}
#购物车列表
shopping_cart = []
#用户消费记录
shopping_log = {}

while status_code:      #第一层loop, 让用户输入信息
    username = input('请输入用户名:').strip()
    if not username:
        continue
    elif username in user_info:
        password = input('请输入密码:').strip()
        if not password:
            print('\033[32;1m 密码不许为空，请重新登录！\033[0m')
        elif password == user_info[username]['password']:
            if os.path.exists('user_log'):
                with open('user_log', 'r') as f:       #反序列化user_log
                    user_info = json.loads(f.read())
                #print(user_info)
                if username in user_info:
                    account = user_info[username]['account']
                    print('欢迎再次来到某宝购物商场，你的工资余额为\033[33;1m %s \033[0m!' % account)
            else:
                account = input('请输入你的工资：').strip()
                print('欢迎来到某宝购物商城,你的工资余额为\033[33;1m %s \033[0m！' % account)

            while status_code:      #第二层loop， 购物车操作
                count = 1
                for i in goods:
                    print('%s %s : %s元' % (count, i['name'], i['price']))
                    count += 1
                print('5 查看购买消费记录')
                print('6 退出程序')
                choice = input('请输入你想要购买的商品编号:').strip()
                if not choice:
                    continue
                elif int(choice):
                    if int(choice) == 6:
                        print('\033[32;1m 您本次的购物车列表为：%s, 您的工资余额为：%s！\033[0m' % (shopping_cart, account))
                        status_code = False
                    elif int(choice) == 5:      #查询消费记录
                        with open('user_log', 'r') as f:
                            user_info = json.loads(f.read())
                            shopping_log = user_info[username]['shopping_log']
                            print('\033[32;1m 您的购买记录为%s。\033[0m' % shopping_log)
                    elif int(choice) >= 1 and int(choice) <= 6:
                        if goods[int(choice)-1]['price'] > int(account):
                            print('\033[32;1m 您的工资余额不足！\033[0m')
                        else:
                            choice_name = goods[int(choice) - 1]['name']
                            shopping_cart.append(choice_name)
                            account = int(account)
                            account -= goods[int(choice) - 1]['price']

                            # 此层判断是为了 shopping_log 字典不会每次运行程序的时候被覆盖，导致购买记录不准确。
                            if os.path.exists('user_log'):
                                with open('user_log', 'r') as f:
                                    user_info = json.loads(f.read())
                                    shopping_log = user_info[username]['shopping_log']
                                    if choice_name not in shopping_log:
                                        shopping_log[choice_name] = {}
                                        shopping_log[choice_name]['count'] = 1
                                        shopping_log[choice_name]['cost'] = goods[int(choice) - 1]['price']
                                    else:
                                        shopping_log[choice_name]['cost'] += goods[int(choice) - 1]['price']
                                        shopping_log[choice_name]['count'] += 1
                            else:
                                if choice_name not in shopping_log:
                                    shopping_log[choice_name] = {}
                                    shopping_log[choice_name]['count'] = 1
                                    shopping_log[choice_name]['cost'] = goods[int(choice) - 1]['price']
                                else:
                                    shopping_log[choice_name]['cost'] += goods[int(choice) - 1]['price']
                                    shopping_log[choice_name]['count'] += 1

                            print('\033[032;1m %s加入购物车成功，您的工资余额为%s \033[0m' % (choice_name, account))
                            user_info[username]['account'] = account
                            user_info[username]['shopping_log'] = shopping_log
                            with open('user_log', 'w') as f:    #序列化user_log
                                json.dump(user_info, f)
                    else:
                        print('\033[31;1m商品编号不存在，请重新输入！\033[0m')
        else:
            print('\033[31;1m 密码错误，请重新登录！ \033[0m')
    else:
        print('\033[31;1m 用户不存在，请重新输入！\033[0m')
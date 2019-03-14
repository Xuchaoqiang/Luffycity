#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
from core import main

# 货物列表
goods = [
    {'name': '电脑', 'price': 1999},
    {'name': '鼠标', 'price': 10},
    {'name': '游艇', 'price': 20},
    {'name': '美女', 'price': 998}
]
# 用户购物车
shopping_car = []

if __name__ == '__main__':
    print('\033[33;1m 欢迎来到某宝购物商场！\033[0m')
    while True:
        all_cost = 0    # 购物车货物总价格
        count = 1       # 用来打印货物编号
        # 打印货物列表
        for i in goods:
            print('{0} {1} : {2}元'.format(count, i['name'], i['price']))
            count += 1
        choice = input('请输入需要购买的商品编号(q --> 结算（ATM）) :').strip()
        if choice.isdigit():
            choice = int(choice)
            shopping_car.append(goods[choice-1])
            print('\033[33;1m %s 加入购物车成功！\033[0m' % goods[choice-1]['name'])
        # 当用户输入‘q’时，打印购物车列表，并且调用ATM接口结算
        elif choice == 'q':
            print('\033[33;1m your shopping_car : \033[0m')
            for i in shopping_car:
                all_cost += i['price']
                print(i)
            print('\033[33;1m all_cost: %s元\033[0m' % all_cost)
            main.shopping_cost(all_cost)        # 调用ATM结算接口
        else:
            print('\033[31;1m Invail value! \033[0m')


# -*- coding: utf-8 -*-
"""
Copyright (c) 2018,掌阅科技
All rights reserved.

摘    要: main2.py
创 建 者: Chentaizhang
创建日期: 2019/1/9 19:31
"""

import sys
import os
# 程序入口，调整python环境变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
from core import manager_handler, auth
from core import main
from core import logger
from core import shopping_cart

ADMIN_MENU  = """
1.  添加账户
2.  修改额度
3.  冻结账户
4.  退出登录
"""

MAIN_MENU = """
1.  提现
2.  转账
3.  还款
4.  查看流水
5.  购物
6.  退出登录
"""

@auth.auth_login
def login_start():
    print(auth.user_data)
    if auth.user_data[0]['id'] == 'admin':
            logger.ad_logger.info('manager login.')
            while True:
                print(ADMIN_MENU)
                choice = input('请输入您要进行的操作：').strip()
                if choice == '1':
                    manager_handler.add_user()
                elif choice == '2':
                    manager_handler.credit_modify()
                elif choice == '3':
                    manager_handler.block_user()
                elif choice == '4':
                    break
                else:
                    print('\033[31;1m Invail value! \033[0m')
    else:
        while True:
            print(MAIN_MENU)
            choice = input('请选择 >>:').strip()
            if choice == '1':
                main.with_draw()
            elif choice == '2':
                main.transfer()
            elif choice == '3':
                main.repayment()
            elif choice == '4':
                main.view_record()
            elif  choice == '5':
                shopping_cart.shooping()
            elif choice == '6':
                break
            else:
                print('\033[31;1m Invaild values! \033[0m')


if __name__ == '__main__':
    login_start()



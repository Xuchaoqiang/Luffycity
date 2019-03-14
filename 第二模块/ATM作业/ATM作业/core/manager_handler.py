#!-*- coding:utf-8 -*-
#__author__:"irving"

import os
import json
from conf import settings
from core import db_handler
from core import logger

BASE_DIR = settings.BASE_DIR
DEFAULT_INFO = settings.DEFAULT_INFO        # 添加新用户时的默认信息
MENU = """
1.  添加账户
2.  修改额度
3.  冻结账户"""

def add_user():
    """
    manager添加账户
    :param username:
    :param password:
    :return:
    """
    username = input('username >>:').strip()
    password = input('password >>:').strip()
    db_file = settings.BASE_DIR + r'\account\%s.json' % username
    if not os.path.exists(db_file):     # 判断文件是否存在，存在则代表要创建的用户已存在
        new_data = DEFAULT_INFO
        new_data['id'] = username
        new_data['password'] = password
        with open(db_file, 'w', encoding='utf-8') as f:
            json.dump(new_data, f)      # new_data 新创建用户的数据文件
        # 记录数据库
        logger.ad_logger.info('%s is created.' % username)
        print('\033[33;1m 用户 %s 创建成功！\033[0m' % username)
    else:
        print('\033[31;1m 用户已存在！\033[0m')

def credit_modify():
    """
    manager修改用户额度
    :return:
    """
    username = input('username >>:').strip()
    user_data = db_handler.load_db(username)
    old_credit = user_data['credit']
    new_credit = input('目前用户额度为 %s , 新额度：' % old_credit)
    if new_credit.isdigit():
        new_credit = int(new_credit)
        user_data['credit'] = new_credit
        db_handler.save_db(user_data['id'], user_data)  # 写入用户json文件
        # 记录数据库
        logger.ad_logger.info('%s credit modify : %s.' % (username, new_credit))
        print('修改成功，目前用户{0}额度为{1}'.format(user_data['id'], user_data['credit']))
    else:
        print('Invalid value!')

def block_user():
    """
    manager冻结账户
    :return:
    """
    username = input('username >>:').strip()
    user_data = db_handler.load_db(username)
    if user_data['status'] == 0:        # 判断block之前用户是否已经被block
        user_data['status'] = 1
        db_handler.save_db(user_data['id'], user_data)        # 写入用户json文件
        # 记录数据库
        logger.ad_logger.info('account %s is blockd!' % username)
        print('账户%s 冻结成功！' % username)

def run():
    """
    manager程序入口启动函数
    :return:
    """
    while True:
        username = input('username >>:').strip()
        # 加载管理员账户信息
        mananger_data = db_handler.load_db('admin')
        password = input('password >>:').strip()
        if username == mananger_data['id'] and password == mananger_data['password']:
            # 记录日志
            logger.ad_logger.info('manager login.')
            while True:
                print(MENU)
                choice = input('请输入您要进行的操作：').strip()
                if choice == '1':
                    add_user()
                elif choice == '2':
                    credit_modify()
                elif choice == '3':
                    block_user()
                else:
                    print('\033[31;1m Invail value! \033[0m')
        else:
            print('\033[31;1m 账号密码错误！\033[0m')
            # 记录manager登陆错误日志
            logger.ad_logger.warning('manager 登陆账号密码错误。')
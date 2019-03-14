#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import os
import json
from conf import settings

def _initdb():
    """
    初始化用户数据文件函数(alex, egon, manager)
    :return:
    """
    alex_db = {'id': 'alex', 'password': 'abc123', 'credit': 15000, 'cost_record': [], 'status': 0}
    egon_db = {'id': 'egon', 'password': 'abc1234', 'credit': 15000, 'cost_record': [], 'status': 0}
    manager_db = {'id': 'admin', 'password': 'admin'}
    db_file = settings.BASE_DIR + r'\account\%s.json' % alex_db['id']
    db_file2 = settings.BASE_DIR + r'\account\%s.json' % egon_db['id']
    db_file3 = settings.BASE_DIR + r'\account\%s.json' % manager_db['id']
    with open(db_file, 'w', encoding='utf-8') as f:
        json.dump(alex_db, f)
    with open(db_file2, 'w', encoding='utf-8') as f2:
        json.dump(egon_db, f2)
    with open(db_file3, 'w', encoding='utf-8') as f3:
        json.dump(manager_db, f3)

def load_db(name):
    """
    加载用户数据，并返回给调用的函数
    :param name: 用户名
    :return:
    """
    db_file = settings.BASE_DIR + r'\account\%s.json' %name
    if os.path.isfile(db_file):
        with open(db_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    else:
        print('用户不存在！')

def save_db(name, data):
    """
    保存用户数据，会覆盖原数据文件
    :param name: 用户名
    :param data: 新的用户数据
    :return:
    """
    db_file = settings.BASE_DIR + r'\account\%s.json' % name
    with open(db_file, 'w', encoding='utf-8') as f:
        json.dump(data, f)





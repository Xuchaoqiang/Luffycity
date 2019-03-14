#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

# configparser 解析配置文件

import configparser

# config = configparser.ConfigParser()  # 实例化一个对象
# # print(config.sections())
# config.read('conf_test.ini')        # 读取配置文件
# print(config.sections())        #调用sections方法， 默认不会读取default

# if 'bytebong.com' in config:
#     print(111)

# print(config['bitbucket.org']['User'])  # 通过字典的形式取值

# print(config['DEFAULT']['Compression'])

# for i in config['bitbucket.org']:
# #     print(i)
#
# config['bitbucket.org']['MaxUsers'] = '22'
#
# for i in config['bitbucket.org']:
#     print(i)

# topsecret = config['topsecret.server.com']
# topsecret['test'] = 'text'
# topsecret['test22'] = 'text22'


config = configparser.ConfigParser()
config.read('i.cfg')

## 读
# secs = config.sections()
# print(secs)
#
# options = config.options('group2')  # 获取指定section的keys
# print(options)
#
# item_list = config.items('group2')
# print(item_list)
#
# val = config.get('group1', 'k2')        # 获取指定key 的value
# print(val)

## 改写
# sec = config.remove_section('group1')    #删除指定的section
# sec = config.add_section('wupeiqi')
# 增
# config['wupeiqi']['age'] = '53'
#
# config.write(open('i.cfg', 'w'))

# config.set('wupeiqi', 'k3', 'aaaa')
# config.write(open('i.cfg', 'w'))

config.remove_option('wupeiqi', 'k3')
config.write(open('i.cfg', 'w'))
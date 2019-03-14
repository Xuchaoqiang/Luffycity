#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving


"""
1. logging模块有5个级别：DEBUG，INFO，WARNING,ERROR,critical

3. json,pickle,shelve都是python序列化的模块
json支持多种语言，但是数据类型限制：dict, list, tuple, str, int (set不行)
pickle只可以在python中使用，支持python所有数据类型。
shelve是pickle的高级封装，以key-value的形式序列化，可以多次序列化数据在一个文件。

4. json的作用是把数据序列化，反序列化。可以在不同语言间传送数据。

5. subprocess执行命令的方法有： subprocess.run(), subprocess.call(), subprocess.Popen()

6. 设计好程序目录结构： 提高程序的可读性和可维护性

7. 打印出命令行的第一个参数。
    import sys
    print(sys.argv[1])

8.
    i: 打印的内容是：/usr/local/nginx
    ii: os.path.dirname -- 返回上一级目录  os.path.abspath -- 返回当前文件的绝对路径

"""

# 2.
# import logging
#
#
# logger = logging.getLogger('access')
# logger.setLevel(logging.INFO)
#
# # 设置handler
# ch = logging.StreamHandler()
# ch.setLevel(logging.INFO)
#
# fh = logging.FileHandler('test.log')
# fh.setLevel(logging.INFO)
#
# # 设置formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# # 绑定handler
# ch.setFormatter(formatter)
# fh.setFormatter(formatter)
#
#
#
# # add handler to logger instance
# logger.addHandler(ch)
# logger.addHandler(fh)
#
# logger.error("account [1234] too many login attempts")


# 9.
# import configparser
# conf = configparser.ConfigParser()      # 实例化一个configparser对象
# conf.read('my.cnf')     # 读配置文件
# mysqld = conf['mysqld']
# # mysqld['default-time-zone'] = '+00:00'
# # conf.write(open('my.cnf', 'w'))
#
# # conf.remove_option('mysqld', 'explicit_defaults_for_timestamp')
# # conf.write(open('my.cnf', 'w'))
#
# conf['DEFAULT']['character-set-server'] = 'utf8'
# conf.write(open('my.cnf', 'w'))


# 10.
# import random
# import string
#
# s_dig = random.choice(string.digits)
# s_up = random.choice(string.ascii_uppercase)
# s_li = random.choice(string.ascii_lowercase)
# s_three = random.sample(string.digits + string.ascii_letters, 3)
#
# s_three.append(s_dig)
# s_three.append(s_up)
# s_three.append(s_li)
# #print(s_three)
# random.shuffle(s_three)
# print(s_three)


# 11.
# import re
# with open('re.txt', encoding='utf-8') as f:
#         res = re.findall('[a-z]{9}\.(?:com|cn|edu)', f.read())
#         print(res)





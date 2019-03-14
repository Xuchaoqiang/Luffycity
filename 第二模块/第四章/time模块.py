#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import time

print(time.localtime())     #返回本地时间（系统时间）  结构化时间
print(time.gmtime())        #返回UTC时间    结构化时间

# mktime    把结构化时间转成时间戳
print(time.mktime(time.localtime()))

# asctime   结构化时间转成外国标准时间
print(time.asctime())

# ctime     时间戳转成外国标准时间
print(time.ctime(time.time()))

# strftime      结构化时间转化为格式化时间
# a 缩写星期几      U 这年第几周
time_a = time.localtime()
time_b = time.strftime('%Y-%m-%d %H:%M:%S %U', time_a)
print(time_b)

# strptime      格式化时间转成结构化时间
time_c = time.strptime(time_b, '%Y-%m-%d %H:%M:%S %U')
print(time_c)


# 时间戳转格式化字符串
# a = time.local(时间戳)  --> time.strftime('%Y-%m-%d %H:%M:%S', a)

# 格式化字符串转时间戳
# a = time.strptime(格式化字符串, '%Y-%m-%d %H:%M:%S' )  time.mktime(a)
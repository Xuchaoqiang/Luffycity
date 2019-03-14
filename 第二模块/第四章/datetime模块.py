#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving


import datetime,time
# datetime模块主要用来时间运算

# datetime.datetime.now()       返回当前的datetime日期类型
d = datetime.datetime.now()
print(d)



# datetime.date.fromtimestamp   把一个时间戳转为datetime日期类型
# d1 = datetime.date.fromtimestamp(time.time())

# 时间运算
# d1 = d + datetime.timedelta(hours=3)
# print(d1)

# 时间替换
d2 = d.replace(year=2008, month=8)
print(d2)
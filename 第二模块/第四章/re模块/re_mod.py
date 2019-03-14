#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import re

# ret = re.findall('a', 'eva egon yuan')      # 返回所有满足匹配条件的结果，放在列表里
# print(ret)

# ret = re.search('eva', 'eva egon yuan').group()
# print(ret)
# # 函数会在字符串内查找模式匹配， 直到找到第一个匹配然后返回一个包含匹配信息的对象，
# # 该对象可以通过group()方法得到匹配的字符串，如果字符串没有匹配，则返回None

# ret = re.match('a', 'abc').group()      #同search， 不过只在字符串开头处进行匹配

# ret = re.split('[d]', 'abcd')
# print(ret)

# ret = re.sub('\d', 'H', 'eva3egon4yuan4', 1)
# print(ret)

# ret = re.subn('\d', 'H', 'eva3egon4yuan4')
# print(ret)

# obj = re.compile('\d{3}')
# ret = re.search(obj, 'abc1234wwwww')
# print(ret)


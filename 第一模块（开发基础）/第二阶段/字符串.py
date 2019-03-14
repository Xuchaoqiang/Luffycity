#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving


#
#s = s.capitalize()     首字母大写，其他全部小写

#s = s.casefold()        全部变小写

#print(len(s))
#s = s.center(13, '-')  以字符串为中心规定长度，不足补'-'

#s = s.count('l', 0, 5)     从字符串0-5位置统计‘l’出现的次数

#s = s.endswith('d')        判断字符串是否以'd'结尾
#s = s.expandtabs(16)

#s = s.find('l',7,11)       规定范围内查找某字符的位置（索引）

# s = 'my name is {name}, age is {age}'
# s = s.format(name='alex',  age=22)

# s = '\nHe22Jo'

#print('-'.join(s))         在字符串每个元素中插入'-'

# print(s.ljust(20, '-'))     从左边开始数20位，不足补'-'

# print(s.rjust(20, '-'))       从右边开始数20位，不足补'-'
# print(s)
# print(s.lstrip())         去除字符串左边的换行符

# a = 'abcdef'
# b = '123456'
#
# table = str.maketrans(a, b)
# print(table)
# name = 'abcalex'
# print(name.translate(table))      maketrans    , translate

# print(s)
# print(s.replace('\n', ''))

# s = 'Hello World'
# # print(s.find('o'))
# # print(s.rfind('o'))
#
# print(s.rsplit('o'))
# print(s.split('o'))

s = 'Hello world'
# print(s.swapcase())       大写变小写

print(s.zfill(50))
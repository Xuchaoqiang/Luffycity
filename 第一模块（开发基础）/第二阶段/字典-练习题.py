#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

#dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

# for i in dic:
#     print(i)

# for i in dic:
#     print(dic[i])

# for i in dic.values():
#     print(i)

# for i in dic:
#     print(i, dic[i])

# dic['k4'] = 'v4'
# print(dic)
#
# dic.pop('k1')
# print(dic)

# dic.pop('k5', None)

# print(dic.get('k2'))

# dic.get('k6', None)

# dic2 = {'k1': 'v111', 'a': 'b'}
# dic2.update(dic)
# print(dic2)

#10
#lis = [['k', ['qwe', 20, {'k1': ['tt', 3, '1']}, 89], 'ab']]
#print(lis[0][1][2]['k1'][0].upper())
#print(lis[-1][-2][-2]['k1'][-3].upper())

#lis[0][1][2]['k1'][1] = '100'
# lis[-1][-2][-2]['k1'][-2] = '100'
# print(lis)

#11
li = [1, 2, 3, 'a', 'b', 4, 'c']
dic = {}

dic.setdefault('k1', [])

if type(dic['k1']) is list:
    for i in li:
        if li.index(i) % 2 == 1:
            dic['k1'].append(i)

print(dic)


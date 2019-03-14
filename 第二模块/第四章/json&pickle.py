#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

'''
把内存数据 转成字符串，叫序列化
把字符串转成内存数据类型  叫反序列化

json.dumps    json.loads
只是把数据类型转成字符串存到内存里的意义？
1.把你内存数据 通过网络 共享给远程其他人
2.定义了不同语言之间的交互规则
    1.纯文本，坏处，不能共享复杂的副局类型
    2.xml， 坏处， 占空间大
    3.json， 简单， 可读性好

json 仅支持 int/str/list/tuple/dict
pickle  支持python所有数据类型

'''


import pickle
#
data = {'k1': 123, 'k2': 'hello'}
#
# # pickle.dumps 将数据通过特殊的形式转换为只有python认识的字符串 bytes格式
# aa = pickle.dumps(data)
# bb = pickle.loads(aa)
# print(bb)
#
# # pickle.dump   将数据通过特殊的形式转换为只有python语言认识的字符串，并写入文件
# with open('data.pk', 'wb') as f:
#     pickle.dump(data, f)
#
# pickle.load       反序列化
# with open('data.pk', 'rb') as f:
#     a = pickle.load(f)
#     print('pl',a)


import json

# json.dumps 将数据通过特殊的形式转换为所有程序都认识的字符串
# j_str = json.dumps(data)
# print(j_str)
# j2_str = json.loads(j_str)
# print(j2_str)

# json.dump    将数据通过特殊的形式转换为所有程序都认识的字符串，并写入文件
# with open('data.json', 'w', encoding='utf-8') as f2:
#     json.dump(data, f2)

# json.load     反序列化
with open('data.json', 'r', encoding='utf-8') as f:
    aa = json.load(f)
    print(aa)


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

# f = open('兼职.txt', 'wb')
# f.write('原子二号'.encode('gbk'))
# f.close()
#
#
# # print('原子二号'.encode('gbk'))

# import os
# f_name = '兼职.txt'
# f_new_name = '兼职2.txt'
#
# old_file = open(f_name, 'r', encoding='utf-8')
# new_file = open(f_new_name, 'w', encoding='utf-8')
# old_data = '深圳'
# new_data = '佛山'
#
# for line in old_file:
#     if old_data in line:
#         replace_data = line.replace(old_data, new_data)
#         new_file.write(replace_data)
#     else:
#         new_file.write(line)
#
# old_file.close()
# new_file.close()
#
# os.remove(f_name)
# os.rename(f_new_name, f_name)

with open('兼职.txt', 'r+', encoding='utf-8') as f:
    data = f.read()
    new_data = data.replace('上海', '')
    f.seek(0)
    f.write(new_data)
    f.truncate()
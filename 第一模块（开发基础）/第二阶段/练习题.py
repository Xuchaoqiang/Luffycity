#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

#1
# li = ['alec', 'aric', 'Alex', 'Tony', 'rain']
# print(type('-'.join(li)))

#2
# li = ['alec', 'aric', 'Alex', 'Tony', 'rain']
#
# for i, j in enumerate(li):
#     li[i] = j.strip()
#     if li[i].startswith('a') or li[i].startswith('A'):
#         if li[i].endswith('c'):
#             print(li[i])
# print(li)


#3
#li = ['alex', 'eric', 'rain', 'seven']

# print(len(li))
#
# li.append('seven')
# print(li)
#
# li.insert(0, 'Tony')
# print(li)
#
# li[1] = 'Kelly'
# print(li)

# li.remove('eric')
# print(li)
#
# print(li.pop(1))
# print(li)
#
# li.pop(2)
# print(li)

#print(li)
# del li[1:]
#
#
# li.reverse()
# print(li)

# for i in range(len(li)):
#     print(i)

# count = 100
# for i, j in enumerate(li):
#     print(j, count)
#     count += 1
#
# for i in li:
#     print(i)

#li = ['hello', 'seven', ['mon', ['h', 'kelly'], 'all'], 123, 446]
# print(li[2][1][1])
# li[-3][-1] = 'ALL'
# print(li)

#tu = ('alex', 'eric', 'rain')
# print(len(tu))
# print(tu[1])
# print(tu[0:2])
# for i in tu:
#     print(i)

# for i in range((len(tu))):
#     print(i)

# count = 10
# for i, j in enumerate(tu):
#     print(j,count)
#     count += 1

# tu = ('alex', [11, 22, {'k1': 'v1', 'k2': ['age', 'name'], 'k3': (11, 22, 33)}, 44])
# '''1.元组的特性：不可修改，只有两种方法  count,type
# 2.不可以
# 3.'k2'对应的值是列表， 可以修改
# 4.'k3'对应的值是元祖，不可修改
# '''
# tu[1][2]['k2'].append('Seven')
# print(tu)
#
# dic = {'k1': 'v1', 'k2': 'v2', 'k3': [11, 22, 33]}
# for i in dic.keys():
#     print(i)

# for i in dic.values():
#     print(i)

# for i in dic:
#     print(i, dic[i])

# dic['k4'] = 'v4'
# dic['k1'] = 'alex'
# dic['k3'].append(44)
# dic['k3'].insert(0, 18)
# print(dic)


# s = 'alex'
# print(list(s))
# print(tuple(s))
# li = ['alex', 'seven']
# print(tuple(li))
# tu = ('Alex', 'Seven')
# print(list(tu))


# dict = {'name': 'Zara', 'age': 7, 'class': 'First'}
# print(type(str(dict)), str(dict))

# dict = {}
# li = ['alex', 'seven']
# count = 10
# for i in li:
#     dict[count] = i
#     count += 1
# print(dict)


# set = {11 ,22, 33, 44, 55, 66, 77, 88 ,99, 90}
# dict = {'k1': [], 'k2': []}
#
# for i in set:
#     if i > 66:
#         dict['k1'].append(i)
#     else:
#         dict['k2'].append(i)
# print(dict)


#10

# li = ['手机', '电脑', '鼠标垫', '游艇']
# while True:
#     print(li)
#     choice = input('Please input your choice:').strip()
#     if not choice:
#         continue
#     elif int(choice) >= 1 and int(choice) <= 4:
#         print(li[int(choice) - 1])
#     else:
#         print('\033[33;1m you must enter 1 - 4. \033[0m')


#11
# map = {'广东省': {'广州市':
#                    {'英德': ['aa'], '连州': ['bb']},
#                '深圳市':
#                    {'宝安区': ['cc'], '银湖区': ['dd']}
#                },
#        '安徽省': {'淮北市':
#                    {'相山区': ['aa'], '杜集区': ['bb']},
#                '毫州市':
#                    {'蒙城县': ['cc'], '利辛县': ['dd']}}
#        }
#
# while True:
#     for i in map:
#         print(i)
#     choice = input('please input your choice:(q:exit!):').strip()
#     if not choice:
#         continue
#     elif choice == 'q':
#         break
#     elif choice in map:
#         for a in map[choice]:
#             print(a)
#
#
#         while True:
#             choice1 = input('please input your choice1:(q:exit!):').strip()
#             if not choice1:
#                 continue
#             elif choice1 == 'q':
#                 break
#             elif choice1 in map[choice]:
#                 for b in map[choice][choice1]:
#                     print(b)
#
#             while True:
#                 choice2 = input('please input your choice2:(q:exit!):').strip()
#                 if not choice2:
#                     continue
#                 elif choice2 == 'q':
#                     break
#                 elif choice2 in map[choice][choice1]:
#                     print(map[choice][choice1][choice2])
#                     break


#11
# print(bool(0))
# print(bool())
# print(bool([]))


#13
# l1 = [11, 22, 33]
# l2 = [22, 33, 44]
#
# l1 = set(l1)
# l2 = set(l2)
# print(l1.intersection(l2))
# print(l1.difference(l2))
# print(l2.difference(l1))
# print(l1.symmetric_difference(l2))

#14
# count = 100
# for i in range(100):
#     print(count)
#     count -= 1

# for i in range(100):
#     print(i+1)

for i in range(1, 10):
    for j in range(1, 10):
        if i < j:
            break
        print('%sx%s=%2'
              's   ' % (j, i, i * j), end='')
    print('')
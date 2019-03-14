#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

# names = ['old_driver', 2, 'rain', 'jack', 2, 'shanshan', 2,  'peiqi', 'black_girl']
#
# num1 = names.index(2)
# names2 = names[num1+1:]
# num2 = names2.index(2)
# print(num1+num2+1)

# names.insert(-1, 'alex')
#
# names[3] = '珊珊'
#
# names2 = ['oldboy', 'oldgorl']
# names.insert(2,names2)
#
# names3 = [1, 2, 3, 4, 5, 6, 2]
# names.extend(names3)
#
# print(names[4:8])
# print(names[2:11:2])
# print(names[-3:])
# print(names.index('peiqi'))
# print(names)

# for i in names:
#     print(names.index(i),i)

# for i in names:
#     if names.index(i) % 2 == 0:
#         names[names.index(i)] = -1
#
# print(names)

shopping_list = []
products = [['iphone', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 31], ['Book', 80], ['nike shoes', 799]]
print('---------商品列表---------')
for index, i in enumerate(products):
    print(index, i[0], i[1])
print('q 退出')

while True:
    choice = input('please input the products id :').strip()
    if choice == 'q':
        for i in shopping_list:
            print(i)
        break

    else:
        shopping_list.append(products[int(choice)][0])
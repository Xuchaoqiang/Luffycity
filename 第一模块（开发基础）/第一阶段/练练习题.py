#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

#! _*_coding:utf-8 _*_
#__author__:"Irving"

"""
1.
编译型与解释型语言的区别：编译型语言的运行速度快，但是需要修改代码就得重新编译，跨平台性比较差；
而解释型语言的运行速度相对比较慢，但是跨平台性强，开发效率较高
编译型语言：C，JAVA
解释型语言：Python，PHP

2.
执行python脚本的两种方式：
（1）.在stdin交互环境下执行（一般用于调试）。
（2）.在一些文本编辑器，或者pycharm里面先用文本保存好代码，再执行。

3.
Python的单行注释用   #
多行注释用   ''' '''   或者 """ """

4.
布尔值有 True和False  或者  0和1

5.
声明变量的注意事项：
（1）变量名只能由数字，字母，下划线组成
（2）不能以数字开头
（3）不用以python的一些内置方法，模块，或者语法命名，例如：def，print，while，class，if，import...
（4）变量名不能词不达意
（5）变量名不能太过长
（6）尽量不要用拼音，中文
（7）变量名规范，下划线连接或者驼峰式

6.
如何查看变量在内存中的地址

9.
n1 = 123456  ,    n2 = n1
'n2 = n1'相当于是把n2的内存指针指向了n1的值，n1 = 123456相当于是n1这个变量名的内存指针指向了内存中'123456'这段数据，
所以n1和n2没有关联关系，n1修改了值， n2还是123456
"""

#7a
# username = 'seven'
# password = '123'
# name = input('name:')
# passwd = input('passwd:')
#
# if username == name and password == passwd:
#     print('login success.')
# else:
#     print('user or password wrong,please try again.')

#7b
# username = 'seven'
# password = '123'
#
# count = 1
# while count <= 3:
#     name = input('name:').strip()
#     passwd = input('password:').strip()
#     if name == username and passwd == password:
#         print('login success.')
#         break
#     else:
#         print('name or passwd wrong, you have %d choice.' %(3-int(count)))
#     count += 1

#7c
# username1 = 'seven'
# username2 = 'alex'
# password = '123'
#
# count = 1
# while count <= 3:
#     name = input('name:').strip()
#     if name == username1 or name == username2:
#         passwd = input('password:').strip()
#         if passwd == password:
#             print('login success.')
#             break
#         else:
#             print('passwd wrong, you have %d choice.' %(3-int(count)))
#     else:
#         print('user is not exist! you have %d choice.' %(3-int(count)))
#     count += 1

#8a
# num = 0
# num1 = 0
# count = 2
# while count <= 100:
#     if count % 2 == 0:
#         num += count
#     else:
#         num1 += count
#     count += 1
# print('result :',num - num1)

#8b:
# count = 1
# while count < 13:
#     if count == 6 or count == 10:
#         pass
#     else:
#         print(count)
#     count += 1

#8c
# count = 101
# num = 50
# while True:
#     if count >= 51:
#         count -= 1
#         print(count)
#     else:
#         result = count - num
#         print(result)
#         num -= 1
#         if result == 50:
#             break

#8d
# count = 0
# while count < 100:
#     count += 1
#     if count % 2 == 1:
#         print(count)
#     else:
#         pass

#8e
# count = 0
# while count < 100:#8d
# count = 0
# while count < 100:
#     count += 1
#     if count % 2 == 1:
#         print(count)
#     else:
#         pass
#     count += 1
#     if count % 2 == 0:
#         print(count)
#     else:
#         pass


#10
# name = input('input your name:').strip()
# area = input('input your area:').strip()
# hobby = input('input your hobby:').strip()
# print('敬可爱的%s,最喜欢在%s地方干%s...' %(name,area,hobby))

#11
# years = input('>>:').strip()
# if int(years) % 4 == 0 and int(years) % 100 != 0:
#     print('%s 是闰年' % years)
# elif int(years) % 400 == 0:
#     print('%s 是闰年' % years)
# else:
#     print('您输入的不是闰年！')

#12
# count_years = 1
# money = 10000
# interest = 0.0325
#
# print(money * interest)
# while True:
#     money += money*interest
#     print(count_years, money)
#     if money > 20000:
#         break
#     count_years +=1

#13

# count = 1
# weight = 1
# weight1 = 4
# while count < 10:
#     if weight < 6:
#         print('* ' * weight)
#     count += 1
#     weight += 1
#     if weight > 5:
#         print('* ' * weight1)
#         weight1 -= 1

#14

# wage = 3000
# while True:
#     income = int(input('input you performance:'))
#     if income > 0:
#         if income >= 350000:
#             person_income = income * 0.15
#             print('your total wage:', wage+person_income)
#         elif income >= 250000:
#             person_income = income * 0.1
#             print('your total wage:', wage+person_income)
#         elif income >= 150000:
#             person_income = income * 0.08
#             print('your total wage:', wage+person_income)
#         elif income >= 100000:
#             person_income = income * 0.05
#             print('your total wage:', wage+person_income)
#         elif income >= 50000:
#             person_income = income * 0.03
#             print('your total wage:', wage+person_income)
#         else:
#             print('无提成！')
#     else:
#         print('your input must bigger 0')

#15


# while True:
#     distance = int(input('input your distance:').strip())       #用户输入距离
#     if distance > 0:
#         day = 0
#         all_cost = 0
#         discount = 1
#         while day < 20:
#             if distance <= 6:
#                 cost = 3
#                 print('day_cost:', cost)
#                 all_cost = all_cost + cost * discount
#             elif distance <= 12:
#                 cost = 4
#                 print('day_cost:', cost)
#                 all_cost = all_cost + cost * discount
#             elif distance <= 22:
#                 cost = 5
#                 print('day_cost:', cost)
#                 all_cost = all_cost + cost * discount
#             elif distance <= 32:
#                 cost = 6
#                 print('day_cost:', cost)
#                 all_cost = all_cost + cost * discount
#             else:       #超过32km的计费情况
#                 more_distance = distance - 32   #具体超多32多少km，多出来的每20km加1元
#                 cost_count = more_distance / 20     #超出的km 除以20  ，算多出来的钱，有两种情况，如果商是整数那就好算
#                 #print(cost_count)                   #多出来的钱，如果不是整数的话，我用了以下取整数商（\\）的对比方法
#                 cost_count_int = more_distance // 20
#                 #print(cost_count_int)
#                 if cost_count == cost_count_int:
#                     cost = cost_count_int + 6
#                     #print('day_cost:', 6 + cost_count_int)
#                     all_cost = all_cost + cost * discount
#                 else:
#                     cost = cost_count_int + 6 + 1
#                     #print('day_cost:', cost)
#                     all_cost = all_cost + cost * discount
#                     #print(all_cost)
#                 if all_cost > 150:
#                     discount = 0.5
#                 elif all_cost > 100:
#                     discount = 0.8
#                 else:
#                     pass
#                 print(all_cost)
#             day += 1
#         else:
#             pass


#16
count = 1
meters = 100
Rebound_meters = 0
totol_meters = 0
while count < 11:
    meters /= 2
    Rebound_meters = meters
    totol_meters = meters + Rebound_meters
    print(meters)
    print(Rebound_meters)
    count += 1


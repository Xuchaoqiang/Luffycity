#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving
# 其实这仅仅是一种变形操作
# 类中所有双下划线开头的名称如__x 都会自动变成： _类名__x的形式

# class A:
#     __N = 0     # 类的数据属性就应该是共享的，但是语法上是可以设置成私有的属性 __N会变形成_A__N
#     def __init__(self):
#         self.__X = 10       # 变形成 self._A__X
#     def __foo(self):        # 变形成 _A__foo
#         print('from A')
#     def bar(self):
#         self.__foo()        # 变形成_A__foo

# A._A__N是可以访问到的， 即这种操作并不是严格意义上的限制外部访问，仅仅是一种语法意义上的变形

class A:
    def __fa(self):     #  _A__fa
        print('from A')
    def test(self):
        self.__fa()     # _A__fa

class B(A):
    def __fa(self):     # _B__fa
        print('from B')

b = B()
b.test()

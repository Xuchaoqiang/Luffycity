#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

# 经典类 class 类名： 这样叫经典类 class 类名(object)： 继承了object的类叫新式类，在python2中
# 新式类 全部类都为新式类

# 经典类查找属性顺序： 对象本身， 父类 -- 深度优先
# 新式类查找属性顺序： 对象本身， 父类 -- 广度优先

class A(object):
    def test(self):
        print('from A')

class B(A):
    def test(self):
        print('from B')

class G(A):
    def test(self):
        print('from G')

class C(G):
    def test(self):
        print('from C')

class D(B):
    def test(self):
        print('from D')

class E(C):
    def test(self):
        print('from E')

class F(D, E):
    pass

print(F.__mro__)
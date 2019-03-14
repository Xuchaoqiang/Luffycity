#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

# with open('print_test.txt', 'w') as f:
#     print('testtest', 'test2test2', file=f, sep='---', end=' and ')
#     print('second!!!', file=f)

# import time
# for i in range(100):
#     time.sleep(0.1)
#     print('{}'.format(i), end='')


# code = '''
# import os
# print(os.path.abspath('.'))
# '''
# code = '''
# print(123)
# a = 20
# print(a)
# '''
# a = 10
# exec(code,{'print':print},)
# print(a)


# res = divmod(10, 3)
# print(res)

# print(round(1.61284567, 3))

# ret = bytearray('alex',encoding='utf-8')
# print(id(ret))
# print(ret[0])
# ret[0] = 65
# print(ret)
# print(id(ret))


# l = (1,2,23,213,5612,342,43)
# print(l)
# print(list(reversed(l)))


# l = (1,2,23,213,5612,342,43)
# sli = slice(1,5,2)
# print(l[sli])

# l=[3,2,100,999,213,1111,31121,333]
# print(max(l))
#
# dic = {'k1': 10, 'k2': 100, 'k3': 30}
# print(max(dic))
# print(dic[max(dic, key=lambda k:dic[k])])


# def num_sqrt(n):
#     num_res = n ** 0.5
#
#     return num_res is int
#
# print(list(filter(num_sqrt, range(1, 101))))

# import math
# def is_sqr(x):
#     return x**0.5 % 1 == 0
# print(list(filter(is_sqr, range(1, 101))))


# list1 = [x for x in range(1, 100)]
# print(list1)

# L = [1, 2, 3, 4, 5, 6, 7, 8]
# def pow2(x):
#     return x*x
#
# print(list(map(pow2, L)))
# t1 = (('a'),('b'))
# t2 = (('c'),('d'))
#
# res = lambda t1,t2 : [{i,j}for i, j in zip(t1, t2)]
# print(res(t1, t2))


# def calc(n):
#     print(n)
#     if int(n/2) > 0:
#         calc(int(n/2))
#     else:
#         print('---')
#     print(n)
#
# calc(10)


# with open('account.txt', 'r', encoding='utf-8') as f:
#     data = f.read()
#     print(data)


# l = ['aaaaaaaaa', 'b', 'c', 'd']
# print(len(l))
#
# for index, i in enumerate(l, 2):
#     print(index, i)




# for i in test:
#     connt = 0
#     for j in i:
#         if connt == 6:
#             print('%s' % j, end='')
#         else:
#             print('%s,' % j, end='')
#         connt += 1
#     print('')

# with open('test2', 'w', encoding='utf-8') as f:
#     f.write(','.join(l))


# a = range(100)
# print(a)


# def yn(fun):#fun=sc_inner
#     print('111yy')
#     def yn_inner(*args,**kwargs):
#         print("yun..........before")
#         ret=fun(*args,**kwargs)#sc_inner()
#         print("yn...........after")
#         return ret
#     return yn_inner
#
# def sx(fun):#fun=china
#     print('222 ss')
#     def sx_inner(*args,**kwargs):
#         print("sx..........before")
#         ret=fun(*args,**kwargs)#china()
#         print("sx...........after")
#         return ret
#     return sx_inner
#
# @yn #china=yn(china)-----china=yn(sx(china))----china=yn(sx_inner)---->china=yn_ineer
# @sx  #china=sx(china)----china=
# def china():
#     print("china is good ")

#china()#yn_inner()



# a = ['1', 'Alex Li', '58', '13651054608', 'IT', '2013-04-01']
# print(','.join(a))


# def is_odd(x):
#     return x % 2 == 1
#
#
#
# l2 = filter(is_odd, range(1, 101))
# l3 = list(l2)
# print(l3)


# def is_not_empty(s):
#     return s and len(s.strip()) > 0
#
# a = 'a b c'
#
# t1 = filter(is_not_empty, ''.join(a))
# print(list(t1))


# def is_sqr(x):
#     return x ** 0.5 % 1 == 0
#
# t2 = filter(is_sqr, range(1, 101))
# print(list(t2))

# t = [1, 2, 3, 4, 5]
# #
# # def pow2(x):
# #     return x * x
# #
# # t3 = map(pow2, t)
# # print(list(t3))


# l1 = [1, 3, 5, -2, -4, -6]
# l2 = sorted(l1, key=abs)
# print(l1)
# print(l2)

# l = [[1,2],[3,4,5,6],(7,),'123']
# print(sorted(l, key=len))


# dic = {2:'a', -1:'w', 9:'i'}
# print(sorted(dic))

# def _add(x, y):
#     return x+y
#
# from functools import reduce
# s2 = reduce(_add, range(1, 101))
# print(s2)

# a = 10 if 3 > 4 else 5
# print(a)

# _lambda = lambda arg : arg +1
# print(_lambda(123))


# cal2 = lambda n : n * n
# print(cal2(10))

# _lambda = lambda x, y : x + y
# print(_lambda(2, 3))


# dic={'k1':10,'k2':100,'k3':30}
# print(max(dic))
#
# print(dic [ max(dic, key=lambda x : dic[x])])


# res = map(lambda x : x * x, [1, 2, 3, 4, 5, 6, 7])
# print(list(res))

# res = filter(lambda a : a > 3, [1, 2, 3, 4, 5, 6])
# print(list(res))

# a = (('a'), ('b'))
# b = (('c'), ('d'))
#
# res = lambda t1, t2: [{i, j}for i, j in zip(t1 , t2)]
# print(res(a, b))

# def func():
#     name = 'eva'
#     def inner():
#         print(name)
#     print(inner.__closure__)
#     return inner
#
# f = func()
# f()

# import time
# time_1 = time.mktime(time.strptime('2021-01-01', '%Y-%m-%d'))
# print(time_1)

# import hashlib
#
# m = hashlib.md5()
# m.update(b'abc')
#
# with open('hash1.json', 'w', encoding='utf-8') as f:
#     f.write(m.hexdigest())


# a = {'a': {'a': 1, 'b': 2}}
# print(a.values())
# import datetime
#
# print(datetime.datetime.now())
# list = {'name': '电脑', 'price': 1999}
# print('{0} {1}'.format(datetime.datetime.now(), list))


# def work(n):
#     count = 0
#     while count < n:
#         count += 1
#         sign = yield count
#         if sign:
#             break
#     yield "over"
#
# new_range = work(5)
# res = next(new_range)
# res1 = new_range.__next__()
# res2 = new_range.send(True)
# print(res, res1, res2, sep=' ')
# next(new_range)

# def work(n):
#     v = n // 2
#     print(v)
#     if v == 0:
#         return "over"
#     work(v)
#     print(v)
# work(6)


# def w1(fun):
#     print('...装饰器开始装饰...')
#     def inner():
#         print('...验证权限...')
#         res = fun()
#         print("this is inner")
#         return res
#     return inner
# @w1
# def test():
#     print('test')
#     return 123
#
# print(test())


# class chinese:
#     """"""
#     country = 'China'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def talk(self):
#         print('%s is talking' % self.name)
#
#
#
# print(chinese.__dict__)


# a = 'aa'
# a.isalpha()


# class Mymeta(type):
#     n=444
#
#     def __call__(self, *args, **kwargs): #self=<class '__main__.OldboyTeacher'>
#         obj=self.__new__(self)
#         print(self.__new__ is object.__new__) #True
#
#
# class Bar(object):
#     n=333
#
#     def __new__(cls, *args, **kwargs):
#         print('Bar.__new__')
#
# class Foo(Bar):
#     n=222
#
#     def __new__(cls, *args, **kwargs):
#         print('Foo.__new__')
#
# class OldboyTeacher(Foo,metaclass=Mymeta):
#     n=111
#
#     school='oldboy'
#
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def say(self):
#         print('%s says welcome to the oldboy to learn Python' %self.name)
#
#
#     # def __new__(cls, *args, **kwargs):
#     #     print('OldboyTeacher.__new__')
#
#
# OldboyTeacher('egon',18) #触发OldboyTeacher的类中的__call__方法的执行，进而执行self.__new__开始查找


# class P1:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class People(P1):
#     def __init__(self, name, age, sex, high):
#         self.sex = sex
#         self.high = high
#         super(People, self).__init__(name, age)
#
# p1 = People('alex', '18', 'male', 180)
# print(p1.__dict__)

# class Mymeta(type):
    # def __call__(self, *args, **kwargs):
    #     # 1.获取空对象
    #     obj = object.__new__(self)
    #     # 2.实例化空对象
    #     self.__init__(obj, *args, **kwargs )
    #     # 3.返回对象
    #     return obj


# class People:
#     country = 'China'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def talking(self):
#         print('talking...')
#
#     def walking(self):
#         print('walking...')
#
# p1 = People('alex', 12)
# print(hasattr(p1, 'talking'))


# a = {'a': 'b', 'c': 'd'}
# if 'a' in a:
#     print(111)


# def create_file(path, size):
#     with open(path, 'w') as f:
#         f.seek(1024 * 1024 * size)
#         f.write('\x00')
#
# create_file('test.txt', 2)

# import hashlib
#
# m = hashlib.md5()
# with open('test.txt', 'rb') as f:
#     for line in f:
#         m.update(line)
#
# print(m.hexdigest())

# LOG_FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# LOG_TYPES = {
#     'teacher': 'teacher.log',
#     'student': 'student.log',
#     'admin': 'admin.log',
# }
# __log_type__ = 'teacher'


# import socket
# import optparse
#
# class FtpClient(object):
#     """ftp客户端"""
#     def __init__(self):
#
#         parser = optparse.OptionParser()
#         parser.add_option("-s", "--server", dest="server", help="ftp server ip_addr")
#         parser.add_option("-P", "--port", type="int", dest="port", help="ftp server port")
#         parser.add_option("-u", "--username", dest="username", help="username info")
#         parser.add_option("-p", "--password", dest="password", help="password info")
#         self.options, self.args = parser.parse_args()
#
#         print(self.options, self.args)
#
# client = FtpClient()

# import time
# from multiprocessing import Process
#
# def foo():
#     print(123)
#     time.sleep(1)
#     print("end123")
#
# def bar():
#     print(456)
#     time.sleep(3)
#     print("end456")
#
# if __name__ == '__main__':
#     p1=Process(target=foo)
#     p2=Process(target=bar)
#
#     p1.daemon=True
#     p1.start()
#     p2.start()
#     time.sleep(0.2)
#     print("main-------")#打印该行则主进程代码结束,则守护进程p1应该被终止.#可能会有p1任务执行的打印信息123,因为主进程打印main----时,p1也执行了,但是随即被终止.


import os
import time
import random
from multiprocessing import Process

def work(n):
    print('%s: %s is running' %(n,os.getpid()))
    time.sleep(random.random())
    print('%s:%s is done' %(n,os.getpid()))

if __name__ == '__main__':
    for i in range(3):
        p=Process(target=work,args=(i,))
        p.start()
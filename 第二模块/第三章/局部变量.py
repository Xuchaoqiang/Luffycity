 #!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving


# 局部变量
# 不加global修改names其实是在内存里重新创建了一个names变量，指向另外一块内存地址，id不一样， 加了global就是直接引用了names
# names = ['alex', 'irving', 'eric']
# def change_name():
#     global names
#     names = ['alex', 'irving']
#     print(names)
#
# change_name()
# print(names)


# 在函数里面可以直接引用列表修改里面的元素， 但是不能对列表进行修改（重新赋值）
# names = ['alex', 'irving', 'eric']
# def change_name():
#     del names[1]
#     names.append('张三丰')
#     print(names)
# change_name()
# print(names)

# 嵌套函数
# 函数内部可以再次定义函数， 执行需要被调用
# def func1():
#     print('alex')
#
#     def func2():
#         print('eric')
#
#     func2()
# func1()

#
# age = 19
# def func1():
#     age = 73
#     def func2():
#         print(age)
#     func2()
# func1()

#
# age = 19
#
# def func1():
#     def func2():
#         print(age)
#     age = 73
#     func2()
# func1()

#
# func1函数里面其实没有重新创建一个值age， 而是对全局变量age操作修改了
# age = 19
# def func1():
#     global age
#     def func2():
#         print(age)
#     age = 73
#     func2()
# func1()
# print(age)

#
# age = 18
#
# def func1():
#     age = 73
#     def func2():
#         print(age)
#     return 666
#
# va1 = func1()
# print(va1)


# 代码定义完成之后，作用域已经生产，作用域链向上查找

#
# age = 18
#
# def func1():
#     age = 73
#     def func2():
#         print(age)
#
#     return func2
#
# va1 = func1()
# va1()
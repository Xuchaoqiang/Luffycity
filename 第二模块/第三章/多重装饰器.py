#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

# def first(func):
#     print('%s() was post to first()' % func.__name__)
#     def _first(*args, **kwargs):
#         print('Call the function %s() in _first().' % func.__name__)
#         return func(*args, **kwargs)
#     return _first
#
# @first      # first(test)  test = first(test) --> _first
# def test():
#     return 'hello world!'
#
# test()
#
# test() was post to first()
# Call the function test() in _first().



def first(func):
    print('%s() was post to first()' % func.__name__)
    def _first(*args, **kwargs):
        print('Call the function %s() in _first().' % func.__name__)
        return func(*args, **kwargs)
    return _first

def second(func):
    print('%s() was post to second()' % func.__name__)
    def _second(*args, **kwargs):
        print('Call the function %s() in _second().' % func.__name__)
        return func(*args, **kwargs)
    return _second


@first      # first(test)  test = first(test) --> _first
@second     # second(test) test = second(test) --> _second
def test():
    return 'hello world!'

test()
#
# 代码逻辑：
# @second -->  second(test) --> test = second(test)
# @first -->  first(test) 相当于 first(second(test))  --> test = first(test)
#
# 执行流程：
# test()   =   first(test)()   -->   test() 相当于 second(test)()  =  test()
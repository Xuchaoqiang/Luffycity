#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving
# import time
#
# def timmer(func):
#     def inner():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(end_time - start_time)
#     return inner
#
# @timmer
# def test():
#     print(111)

l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]

def test(k, l):
    all_len = len(l)
    tmp = len(l) / 2
    if k > l[tmp]:
        l[tmp+1:]
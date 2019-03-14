#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

def fib(max):
    n, a, b = 0, 1, 1
    while n < max:
        yield b
        print('aaaaaaaaaaaaaa')
        a, b = b, a+b
        n += 1
    return 'done'

f = fib(15)
for i in f:
    print(i)


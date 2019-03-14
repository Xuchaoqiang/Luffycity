#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

def gen1():
    for c in 'AB':
        yield c
    for i in range(3):
        yield i

print(list(gen1()))

def gen2():
    yield from 'AB'
    yield from range(3)

print(list(gen2()))


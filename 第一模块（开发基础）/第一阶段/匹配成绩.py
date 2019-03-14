#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

core = int(input('input your core:'))

if core <= 100 and core >= 90:
    print('A')
elif core <= 89 and core >= 80:
    print('B')
elif core <= 79 and core >= 60:
    print('C')
elif core <= 59 and core >= 40:
    print('D')
elif core <= 39 and core >= 0:
    print('E')
else:
    print('please input your core again.')
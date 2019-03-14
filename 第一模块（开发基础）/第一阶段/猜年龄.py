#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

age = 22

count = 0

while True:
    count +=1
    guest_age = int(input('>>:'))
    if count == 3:
        choice = input('game over,if you want to conntinue , you can input y:')
        if choice == 'y':
            count = 0
    elif guest_age == age:
        print('your are right!')
        break
    elif guest_age < age:
        print('think more bigger!', count)
    elif guest_age > age:
        print('think more smaller!')



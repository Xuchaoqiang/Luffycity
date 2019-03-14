#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving
import random

r1 = random.randrange(1, 10)        #不包括10
print(r1)

r2 = random.randint(1, 10)          #包括10
print(r2)

r3 = random.random()            #浮点数
print(r3)

r4 = random.choice('sdahkjsj&&^2as')        #返回一个
print(r4)

r5 = random.sample('dasdk*&*&^12mja', 3)        #可返回多个
print(r5)

## 随机生成字符串

import string
s = string.ascii_letters + string.digits
r6 = random.sample(s, 5)
print(''.join(r6))


# 洗牌, 直接修改原处
t = list(range(100))
print(t)
random.shuffle(t)
print(t)

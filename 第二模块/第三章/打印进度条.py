#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving


import time
for i in range(0, 101, 2):
    time.sleep(0.1)
    char_num = i//2     # 打印多少个'*'
    per_str = '\r{}% : {}\n'.format(i, '*' * char_num) if i == 100 else '\r{}% : {}'.format(i, '*' * char_num)
    print(per_str, end='', flush=True)
    # \r可以把光标移动行首但不换行
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

data_set = list(range(101))
# print(data_set)

def b_search(n, low, high, d):

    mid = int((low + high)/2)
    if low == high:
        print('no find!')
        return
    if n < d[mid]:     # n小于列表中间值，去列表左边找
        print('go left {} ,{} , {}'.format(low, high, d[mid]))
        b_search(n, low, mid, d)
    elif n > d[mid]:    # n大于列表中间值，去列表右边找
        print('go right {}, {}, {}'.format(low, high, d[mid]))
        b_search(n, mid+1, high, d)     # mid+1是为了避免重复比较
    else:
        print('find it!')

b_search(44, 0, len(data_set), data_set)
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

from multiprocessing import Process, Lock
import time
import json

def search(name):
    with open('db', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print('<%s> 查看到剩余票数为%s' % (name, data))

def get(name):
    time.sleep(1)
    with open('db', 'r', encoding='utf-8') as f:
        data = json.load(f)
        if data['counts'] > 0:
            data['counts'] -= 1
            time.sleep(3)
            with open('db', 'w', encoding='utf-8') as f2:
                json.dump(data, f2)
                print('<%s> 购票成功！' % name)
        else:
            print('购票失败')

def task(name, mutex):
    search(name)
    mutex.acquire()
    get(name)
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    for i in range(10):
        p = Process(target=task, args=('路人%s' % i, mutex))
        p.start()
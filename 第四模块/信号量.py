#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

from threading import  Thread, Semaphore, currentThread
import random, time

sm = Semaphore(3)

def task():
    sm.acquire()
    print('%s in ' % currentThread().getName())
    time.sleep(random.randint(1, 3))
    sm.release()

if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=task)
        t.start()
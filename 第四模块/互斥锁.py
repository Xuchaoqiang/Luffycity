#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

from multiprocessing import Process,Lock
import time

# def task(name):
#     print('%s 1' % name)
#     time.sleep(1)
#     print('%s 2' % name)
#     time.sleep(1)
#     print('%s 3' % name)
#
# if __name__ == '__main__':
#     for i in range(3):
#         p = Process(target=task, args=('进程%s' % i,))
#         p.start()



def task(name, mutex):
    mutex.acquire()
    print('%s 1' % name)
    time.sleep(1)
    print('%s 2' % name)
    time.sleep(1)
    print('%s 3' % name)
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    for i in range(3):
        p = Process(target=task, args=('进程%s' % i, mutex, ))
        p.start()
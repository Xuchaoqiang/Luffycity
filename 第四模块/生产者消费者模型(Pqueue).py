#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

from multiprocessing import Process, Queue
import time

def Produce(q):
    for i in range(5):
        time.sleep(0.5)
        print('生产者生产了包子%s！' % i)
        q.put('包子%s' % i)

def Consumer(q):
    while True:
        time.sleep(1)
        baozi = q.get()
        if not baozi:
            break
        print('消费者吃了%s' % baozi)


if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=Produce, args=(q, ))
    p2 = Process(target=Produce, args=(q, ))

    c1 = Process(target=Consumer, args=(q, ))
    c2 = Process(target=Consumer, args=(q, ))

    p1.start()
    p2.start()
    c1.start()
    c2.start()
    p1.join()
    p2.join()
    q.put(None)
    q.put(None)

    print('main process end')


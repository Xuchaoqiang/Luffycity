#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

from multiprocessing import Process, JoinableQueue
import time

def Produce(q):
    for i in range(5):
        time.sleep(0.5)
        print('生产者生产了包子%s！' % i)
        q.put('包子%s' % i)
    q.join()

def Consumer(q):
    while True:
        time.sleep(1)
        baozi = q.get()
        if not baozi:
            break
        print('消费者吃了%s' % baozi)
        q.task_done()


if __name__ == '__main__':
    q = JoinableQueue()

    p1 = Process(target=Produce, args=(q, ))
    p2 = Process(target=Produce, args=(q, ))

    c1 = Process(target=Consumer, args=(q, ))
    c2 = Process(target=Consumer, args=(q, ))

    c1.daemon = True
    c2.daemon = True

    p1.start()
    p2.start()
    c1.start()
    c2.start()
    p1.join()
    p2.join()

    print('main process end')

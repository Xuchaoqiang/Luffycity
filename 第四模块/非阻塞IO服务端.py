#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8081))
server.listen(5)
server.setblocking(False)

print('starting..')

rlist = []
wlist = []
while True:

    try:
        conn, addr = server.accept()
        rlist.append(conn)
        print(rlist)
    except BlockingIOError:

        # 收消息
        del_rlist = []
        for conn in rlist:
            try:
                data = conn.recv(1024)
                if not data:
                    del_rlist.append(conn)
                    continue
                wlist.append((conn, data.upper()))
            except BlockingIOError:
                continue
            except Exception:
                conn.close()
                del_rlist.append(conn)

        # 发消息
        del_wlist = []
        for item in wlist:
            try:
                conn = item[0]
                data = item[1]
                print(item)
                print(conn)
                conn.send(data)
                del_wlist.append(item)
            except BlockingIOError:
                continue

        # 删除无用链接
        for item in del_wlist:
            wlist.remove(item)

        for item in del_rlist:
            rlist.remove(item)

server.close()


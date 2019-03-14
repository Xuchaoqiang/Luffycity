#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import socket
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8081))
server.listen(5)
server.setblocking(False)
print('starting')

rlist = [server, ]
wlist = []
wdata = {}

while True:
    rl, wl, xl = select.select(rlist, wlist, [], 0.5)
    print('rl', rl)
    print('wl', wl)

    for sock in rl:
        if sock == server:
            conn, addr = sock.accept()
            rlist.append(conn)
        else:
            try:
                data = sock.recv(1024)
                if not data:
                    sock.close()
                    rlist.remove(sock)
                    continue
                wlist.append(sock)
                wdata[sock] = data.upper()
            except Exception:
                sock.close()
                rlist.remove(sock)

    for sock in wl:
        data = wdata[sock]
        sock.send(data)
        wlist.remove(sock)
        wdata.pop(sock)

server.close()

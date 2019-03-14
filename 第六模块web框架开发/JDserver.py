#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("127.0.0.1", 8800))

sock.listen(5)

while True:
    print("server waiting...")
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print('data', data)
    conn.send(b"HTTP/1.1 200 OK\r\n\r\nhello luffycity!")
    conn.close()
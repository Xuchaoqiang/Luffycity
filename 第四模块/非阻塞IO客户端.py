#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 8081))

while True:
    msg = input('>>:').strip()
    if not msg:
        continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))

client.close()
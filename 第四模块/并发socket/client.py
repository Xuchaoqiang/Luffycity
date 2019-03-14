#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8081))

while True:
    inp = input('>>:').strip()
    client.send(inp.encode('utf-8'))
    data = client.recv(1024).decode('utf-8')
    print(data)

client.close()
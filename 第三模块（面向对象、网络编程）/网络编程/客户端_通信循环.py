#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import socket

# 1、买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2、拨号
phone.connect(('127.0.0.1', 8080))

# 3、开始发收信息
while True:
    msg = input('>>:').strip()
    if not msg: continue
    phone.send(msg.encode('utf-8'))

    data = phone.recv(1024)
    print(data)

phone.close()
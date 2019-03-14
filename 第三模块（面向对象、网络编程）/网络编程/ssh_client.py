#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('localhost', 8779))

while True:
    # 1、发送命令
    cmd = input('>>:').strip()
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))
    # 2、接收命令结果并打印
    data = phone.recv(1024)
    print(data.decode('gbk'))

phone.close()
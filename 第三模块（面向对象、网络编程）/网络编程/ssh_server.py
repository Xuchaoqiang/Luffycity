#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import socket
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.bind(('localhost', 8779))

phone.listen(5)

while True:
    conn, addr = phone.accept()
    print(addr)

    while True:
        try:
            # 1、接受命令
            cmd = conn.recv(1024)
            if not cmd:
                break    # linux解决客户端突然断开的方法

            # 2、执行命令， 拿到结果
            ret = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            stdout = ret.stdout.read()
            stderr = ret.stderr.read()

            # 3、返回结果
            conn.send(stdout + stderr)
        except ConnectionResetError:    # windows解决客户端突然断开的方法
            break
    conn.close()

phone.close()
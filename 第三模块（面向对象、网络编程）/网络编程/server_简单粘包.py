#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import socket
import struct
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 7888))

server.listen(5)

print('starting...')

while True:     # 链接循环
    conn, client_addr = server.accept()
    print(client_addr)

    while True:     # 通信循环
        try:
            #1、 收命令
            cmd = conn.recv(1024)
            if not cmd: break

            #2、 执行命令，拿到结果
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            #3、 把命令结果返回给客户端
            # 第一步：制作固定长度的报头（执行结果的长度）
            total_size = len(stderr) + len(stdout)
            header = struct.pack('i', total_size)

            # 第二步：把包头发给客户端
            conn.send(header)

            # 第三步：再发送真实的数据
            conn.send(stdout)
            conn.send(stderr)

        except ConnectionResetError:
            break
    conn.close()

server.close()

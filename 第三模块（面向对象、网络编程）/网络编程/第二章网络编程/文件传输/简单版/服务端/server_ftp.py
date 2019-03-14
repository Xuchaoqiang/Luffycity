#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import os
import socket
import subprocess
import struct
import json

SERVER_DIR = r'C:\Users\Xuuuuuu\PycharmProjects\Luffycity\第三模块（面向对象、网络编程）\网络编程\第二章网络编程\文件传输\简单版\服务端'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 9991))

server.listen(5)

while True:
    conn, client_addr = server.accept()
    print(client_addr)
    while True:
        try:
            cmd = conn.recv(1024)
            # 命令分析  get a.txt
            print(cmd.decode('utf-8').split(' '))
            handler = cmd.decode('utf-8').split(' ')[0]
            filename = cmd.decode('utf-8').split(' ')[1]

            if not cmd: break

            # 2、制作报头， 回复报头长度， 并回复报头内容
            header_dic = {'filename': filename,
                          'md5': 'xxxxxxxxxx',
                          'total_size': os.path.getsize('{}\\{}'.format(SERVER_DIR, filename))}

            header_bytes = json.dumps(header_dic).encode('utf-8')
            # 先发送报头固定长度
            conn.send(struct.pack('i', len(header_bytes)))
            # 再发送报头内容
            conn.send(header_bytes)

            # 3、发送真实数据
            with open(os.path.join(SERVER_DIR, filename), 'rb') as f:
                for line in f:
                    conn.send(line)
        except ConnectionResetError:
            break

    conn.close()

server.close()
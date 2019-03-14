#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import socket
import subprocess
import struct
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 9999))

server.listen(5)

while True:
    conn, client_addr = server.accept()
    print(client_addr)
    while True:
        try:
            cmd = conn.recv(1024)
            if not cmd: break
            # 1、执行命令
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                            stderr=subprocess.PIPE,
                                            stdout=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            # 2、制作报头， 回复报头长度， 并回复报头内容
            header_dic = {'filename': 'a.txt',
                          'md5': 'xxxxxxxxxx',
                          'total_size': len(stderr) + len(stdout)}

            header_bytes = json.dumps(header_dic).encode('utf-8')
            # 先发送报头固定长度
            conn.send(struct.pack('i', len(header_bytes)))
            # 再发送报头内容
            conn.send(header_bytes)

            # 3、发送真实数据
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:
            break

    conn.close()

server.close()


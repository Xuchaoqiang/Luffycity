#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import socket
import json
import struct

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 9999))

while True:
    cmd = input('>>:').strip()
    if not cmd: continue
    client.send(cmd.encode('utf-8'))
    # 1、先接收报头长度
    header_len = struct.unpack('i',client.recv(4))

    # 2、再根据报头的长度来接收报头内容
    header_bytes = client.recv(header_len[0])

    # 3、获取报头内容
    header_dic = json.loads(header_bytes.decode('utf-8'))
    print(header_dic)
    total_size = header_dic['total_size']

    # 4、接收内容
    recv_size = 0
    recv_data = b''
    while recv_size < total_size:
        ret = client.recv(1024)
        recv_size += len(ret)
        recv_data += ret
    print(recv_data.decode('gbk'))

client.close()
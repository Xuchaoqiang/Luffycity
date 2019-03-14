#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import socket
import struct

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7888))

while True:
    cmd = input('>>:').strip()
    if not cmd: continue
    client.send(cmd.encode('utf-8'))

    data = client.recv(4)
    header = struct.unpack('i', data)

    total_size = header[0]

    recv_size = 0
    recv_data = b''

    while recv_size < total_size:
        r_data = client.recv(1024)
        recv_size += len(r_data)
        recv_data += r_data

    print(recv_data.decode('gbk'))

client.close()

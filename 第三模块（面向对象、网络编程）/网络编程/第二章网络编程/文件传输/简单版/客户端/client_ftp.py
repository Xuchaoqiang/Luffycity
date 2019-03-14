#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import os
import socket
import json
import struct

DOWNLOAD_DIR = r'C:\Users\Xuuuuuu\PycharmProjects\Luffycity\第三模块（面向对象、网络编程）\网络编程\第二章网络编程\文件传输\简单版\客户端'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 9991))

while True:
    cmd = input('>>:').strip()      # get a.txt
    if not cmd: continue
    client.send(cmd.encode('utf-8'))
    # 1、先接收报头长度
    header_len = struct.unpack('i', client.recv(4))

    # 2、再根据报头的长度来接收报头内容
    header_bytes = client.recv(header_len[0])

    # 3、获取报头内容
    header_dic = json.loads(header_bytes.decode('utf-8'))
    '''
                header_dic = {'filename': os.path.join(SERVER_DIR, filename),
                          'md5': 'xxxxxxxxxx',
                          'total_size': os.path.getsize('{}\\{}'.format(SERVER_DIR, filename))}
    '''
    filename = header_dic['filename']
    print(header_dic)
    total_size = header_dic['total_size']

    # 4、接收内容

    with open(os.path.join(DOWNLOAD_DIR, filename), 'wb') as f:
        recv_size = 0
        while recv_size < total_size:
            ret = client.recv(1024)
            recv_size += len(ret)
            f.write(ret)
            print(total_size, recv_size)


client.close()
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

"""
ftp_clinet
发送命令
自己也需要对命令进行分析切割
接收 报头的长度bytes
根据报头的长度规定下一次接收的长度（这样就保证了报头的内容不会粘包）
根据文件大小进行不粘包操作
"""
import os
import socket
import struct
import json

DOWNLAOD = r'C:\Users\Xuuuuuu\PycharmProjects\Luffycity\第三模块（面向对象、网络编程）\网络编程\第二章网络编程\download'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9897))

def get():
    # 接收固定长度的struct  -- 报头长度
    header_len = struct.unpack('i', client.recv(4))
    print(header_len)

    # 接收报头内容
    header_str = client.recv(header_len[0]).decode('utf-8')
    header_dic = json.loads(header_str)
    print(header_dic)

    filename = header_dic['filename']
    total_size = header_dic['total_size']

    with open(os.path.join(DOWNLAOD, filename), 'wb') as f:
        ret_size = 0
        while ret_size < total_size:
            ret_data = client.recv(1024)
            ret_size += len(ret_data)
            f.write(ret_data)
            print(total_size, ret_size)


def put(client, filename):
    header_dic = {'filename': filename,
                  'md5': 'xxxxxxx',
                  'total_size': os.path.getsize('{}\\{}'.format(DOWNLAOD, filename))}
    header_bytes = json.dumps(header_dic).encode('utf-8')

    # 发送报头的总长度的struct
    header_len = struct.pack('i', len(header_bytes))
    client.send(header_len)

    # 发送报头
    client.send(header_bytes)

    # 真正开始处理数据
    real_filename = os.path.join(DOWNLAOD, filename)
    with open(real_filename, 'rb') as f:
        for line in f:
            client.send(line)  # 粘包


def run():
    while True:
        inp = input('>>: ').strip()
        if not inp: continue
        client.send(inp.encode('utf-8'))
        cmds = inp.split()
        handler = cmds[0]
        filename = cmds[1]

        if handler == 'get':
            get()

        if handler == 'put':
            put(client, filename)


if __name__ == '__main__':
    run()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving
"""
ftp server      多链接、多信息交互
接收客户端发送过来的命令
将命令进行切割
对命令进行分析，提取命令部分和文件部分
如果是get，用rb操作打开服务端的文件
返回内容
关闭链接

解决粘包：
发送目标文件的大小给客户端
让客户端根据文件总大小来while循环来接收（每次接收限定大小）
"""
import os
import socket
import json
import struct

SHARE_DIR = r'C:\Users\Xuuuuuu\PycharmProjects\Luffycity\第三模块（面向对象、网络编程）\网络编程\第二章网络编程\share'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9897))
server.listen(5)

def put(conn):
    # 接收固定长度的struct  -- 报头长度
    header_len = struct.unpack('i', conn.recv(4))
    print(header_len)

    # 接收报头内容
    header_str = conn.recv(header_len[0]).decode('utf-8')
    header_dic = json.loads(header_str)
    print(header_dic)

    filename = header_dic['filename']
    total_size = header_dic['total_size']

    with open(os.path.join(SHARE_DIR, filename), 'wb') as f:
        ret_size = 0
        while ret_size < total_size:
            ret_data = conn.recv(1024)
            ret_size += len(ret_data)
            f.write(ret_data)
            print(total_size, ret_size)


def get(conn, cmds):
    filename = cmds[1]
    header_dic = {'filename': filename,
                  'md5': 'xxxxxxx',
                  'total_size': os.path.getsize('{}\\{}'.format(SHARE_DIR, filename))}
    header_bytes = json.dumps(header_dic).encode('utf-8')

    # 发送报头的总长度的struct
    header_len = struct.pack('i', len(header_bytes))
    conn.send(header_len)

    # 发送报头
    conn.send(header_bytes)

    # 真正开始处理数据
    real_filename = os.path.join(SHARE_DIR, filename)
    with open(real_filename, 'rb') as f:
        for line in f:
            conn.send(line)  # 粘包


def run():
    print('starting..')
    while True:     # 多链接
        try:
            conn, client_addr = server.accept()
            print(client_addr)
            while True:     # 多交互
                cmds = conn.recv(1024).decode('utf-8').split()
                if not cmds: break
                handler = cmds[0]
                if handler == 'get':
                    get(conn, cmds)
                elif handler == 'put':
                    put(conn)

            conn.close()
        except ConnectionResetError:
            break

    server.close()


if __name__ == '__main__':
    run()




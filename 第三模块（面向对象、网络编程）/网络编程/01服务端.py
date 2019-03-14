#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import socket

# 1、买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2、绑定手机卡
phone.bind(('localhost', 8080))

# 3、开机      可以挂起多少个电话
phone.listen(5)

# 4、等电话连接
print('starting ..')
conn, addr = phone.accept()
print(conn)
print(addr)

# 5、开始收发信息
data = conn.recv(1024)      # 1.单位bytes     2. 1024代表最大接收1024个bytes
print('客户端的数据', data)

conn.send(data.upper())

# 6、挂电话
conn.close()

# 7、关机
phone.close()


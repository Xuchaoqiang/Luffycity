#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import socket

# 1、买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 解决端口冲突（因为操作系统回收端口太慢）
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

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
while True:
    try:
        data = conn.recv(1024)      # 1.单位bytes     2. 1024代表最大接收1024个bytes

        # 解决客户端断开后的问题
        # linux 会死循环
        if not data: break

        # windows会抛出 connectionreseterror 异常

        print('客户端的数据', data)

        conn.send(data.upper())
    except ConnectionResetError:
        break

# 6、挂电话
conn.close()

# 7、关机
phone.close()

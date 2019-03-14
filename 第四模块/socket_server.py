#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

'''
socketserver使用模式：

1 功能类
    class MyServer(socketserver.BaseRequestHandler):
        def handle(self):
            pass

2 server = socketserver.ThreadingTCPServer(('localhost', 8080), MyServer)

3 server.serve_forever()

'''

import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        """
        并发的业务逻辑
        conn: self.request
        :return:
        """
        while True:
            client_data = self.request.recv(1024)
            print(client_data.decode('utf-8'))
            if client_data.decode('utf-8') == "exit":
                print("客户端断开连接， 等待新的用户连接...")
                break
            print("接收数据 >> ", client_data.decode('utf-8'))
            response = input("响应数据 >>>")
            self.request.sendall(response.encode('utf-8'))

        self.request.close()

server = socketserver.ThreadingTCPServer(('localhost', 8080), MyServer)
server.serve_forever()

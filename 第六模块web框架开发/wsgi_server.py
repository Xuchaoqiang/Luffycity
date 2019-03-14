#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

from wsgiref.simple_server import make_server

def application(environ, start_response):
    # 按着http请求协议来解析数据
    # 按着http响应协议来封装数据

    path = environ.get('PATH_INFO')

    start_response('200 OK', [])
    data = ''
    if path == '/login':
        with open('login.html', 'r') as f:
            data = f.read()
    elif path == '/index':
        with open('index.html', 'r') as f:
            data = f.read()
    return [data.encode()]


# 封装socket
httped = make_server("localhost", 8090, application)

# 等待用户连接： conn,addr = sock.accept()
httped.serve_forever()
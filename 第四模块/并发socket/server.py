#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Irving

import socket
from multiprocessing import Process



def interactive(conn):
    while True:
        cmd = conn.recv(1024)
        conn.send(cmd.upper())
    conn.close()

def accept(ip_addr):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ip_addr)
    server.listen(5)
    while True:
        conn, addr = server.accept()
        print(addr)
        p = Process(target=interactive, args=(conn, ))
        p.start()
    server.close()



if __name__ == '__main__':
    accept(('localhost', 8081))
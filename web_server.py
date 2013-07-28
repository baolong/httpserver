#!/usr/bin/env python
# -*- coding: utf8

from socket import *
import threading
import sys
sys.path.append('/home/long/web/src')
import response_builder
from http_request_parser import HttpRequestParser
import connection
import time

def newconnection(socket, ip):
    connect = connection.connection(socket, ip)
    connect.newconnection()
    socket.close()

def main():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', 8888))
    sock.listen(100)
    while True:
        cli,addr = sock.accept()
        t = threading.Thread(target = newconnection, args = (cli, addr))
        thread = []
        thread.append(t)
        thread[0].start()
    sock.close()

if __name__ == '__main__':
    main()

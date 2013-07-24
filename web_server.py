#!/usr/bin/env python
# -*- coding: utf8

from socket import *
import os
import response_builder
from http_request_parser import HttpRequestParser

def main():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', 8888))
    sock.listen(2)

    print 'waiting for connection.....'
    cli,addr = sock.accept()
    print '...connnect from:', addr
    data = cli.recv(1024)
    request = HttpRequestParser()
    request.parse(data)
    cli.send(data)
    cli.close()
    sock.close()

if __name__ == '__main__':
    main()

#!/usr/bin /env python
# _*_ coding: utf8

BUFSIZE = 1024

import threading

class connection(object):
    def __init__(self, connection, ip):
        self.connection = connection   #套接字
        self.client_ip = ip     #客户端IP地址

    def GetConnection():
        return self.connection

    def GetIp():
        return self.ip

    def newconnection():
        request = self.connection.recv(BUFSIZE)  #获取请求
        request_parse = HttpRequestParser()   #请求解析对象
        request_parse.parse(request)       #解析请求
        response = ResponseBuilder()      #响应对象
        response.setHttpStatus(200)
        response.setHttpReason('OK')
        response.setHttpVersion(request_parse.GetVersion)
        headers = request_parse.GetHeas()
        for key in headers:
            response.addHeaer(key, headers[key])


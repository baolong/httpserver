#!/usr/bin /env python
# _*_ coding: utf8

BUFSIZE = 1024
import sys
sys.path.append('/home/long/httpserver/src')
import threading
from http_request_parser import HttpRequestParser
from response_builder import ResponseBuilder

class connection(object):
    def __init__(self, connection, ip):
        self.connection = connection   #套接字
        self.client_ip = ip     #客户端IP地址

    def GetConnection():     #获取套接字
        return self.connection

    def GetIp():         #获取客户端IP
        return self.ip

    def newconnection(self):
        request = self.connection.recv(BUFSIZE)  #获取请求
        request_parse = HttpRequestParser()   #请求解析对象
        request_parse.parse(request)       #解析请求
        response = ResponseBuilder()      #响应对象
        response.setHttpStatus(200)
        response.setHttpReason('OK')
        response.setHttpVersion(request_parse.GetVersion)
        headers = request_parse.GetHeaders()
        for key in headers:
            response.addHeader(key, headers[key])
        response.writeContent()
        result = response.getResult()
        self.connection.send(result)
        print result

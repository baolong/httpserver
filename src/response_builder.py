#!/usr/bin/env python
# -*- coding: utf8
import sys
import os
from time import ctime
sys.path.append('~/web/src')
from mime_types import filename_to_type
from template import render

class ResponseBuilder(object):
    def __init__(self):
        self.status = None
        self.ip = None
        self.reason = None
        self.version = None
        self.headers = {}
    def setHttpStatus(self, status):   #设置响应状态
        self.status = status

    def setIp(self, ip):
        self.ip = ip
    
    def setHttpReason(self, reason):   #设置状态代码的文本描述
        self.reason = reason

    def setHttpVersion(self, version):    #设置http协议版本
        self.version = version

    def addHeader(self, key, value):    #添加报头
        self.headers[key] = value

    def writeContent(self, filename):     #写入正文
        if (filename == '/'):
            filename = 'index.htm'
            print 'connection from ' + str(self.ip) + '  at:  ' + ctime()
        else:
            filename = filename.lstrip('/')
        self.context_type = filename_to_type(filename)
        self.length = os.path.getsize(filename)
#        if (filename != 'index.htm'):
        fp = open(filename)
        self.content = fp.read() 
        fp.close()
#        else:
#            dict = {
#                'time':ctime()
#            }
#            self.content = render(filename,dict)

    def getResult(self):     #获取响应内容
        result = ''
        result += self.version + ' '
        result += self.status + ' '
        result += self.reason + '\r\n'
        result += 'Content-Length: ' + str(self.length) + '\r\n'
        result += 'Content-Type: ' + self.context_type + '\r\n'
        for key in self.headers:
            result += key + ': ' + self.headers[key] + '\r\n'
        result += '\r\n'
        result += self.content
        return result

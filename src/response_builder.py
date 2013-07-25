#!/usr/bin/env python
# -*- coding: utf8

import os

class ResponseBuilder(object):
    def __init__(self):
        self.status = ''
        self.reason = ''
        self.version = ''
        self.headers = {}
    def setHttpStatus(self, status):   #设置响应状态
        self.status = status
    
    def setHttpReason(self, reason):   #设置状态代码的文本描述
        self.reason = reason

    def setHttpVersion(self, version):    #设置http协议版本
        self.version = version

    def addHeader(self, key, value):    #添加报头
        self.headers[key] = value

    def writeContent(self, filename = 'index.htm'):     #写入正文
        fp = open(filename)
        self.length = os.path.getsize(filename)
        self.content = fp.read() 

    def getResult(self):     #获取响应内容
        result = ''
#        result += self.version + ' '
        print 'version:'
        print type(self.version)
        print '\n'
        result += self.status + ' '
        result += self.reason + '\n'
        for key in self.headers:
            result += key + ': ' + self.headers[key]
        return result

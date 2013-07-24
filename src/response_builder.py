#!/usr/bin/env python
# -*- coding: utf8

class 

class ResponseBuilder(object):
    def setHttpStatus(self, status):   #设置响应状态
        self.status = status
    
    def setHttpReason(self, reason):   #设置状态代码的文本描述
        self.reason = reason

    def setHttpVersion(self, version):    #设置http协议版本
        self.version = version

    def addHeader(self, key, value):    #添加报头
        self.headers[key] = value

    def writeContent(self, filename):     #写入正文
        fp = open(filename)
        self.length = os.path.gtsize(filename)
        self.content = fp.read() 

    def getResult(self):     #获取响应内容
        result = ''
        result += self.version + ' '
        result += self.status + ' '
        result += self.reason + '\n'
        for key in self.headers:
            result += key + ': ' + self.headers[key]

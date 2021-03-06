#!/usr/bin/env python
# -*- coding: utf8

class HttpRequestParser(object):
    def __init__(self):
        'http request parser'
        self.method = ''    #http请求方法
        self.path = '' #请求的路径
        self.version = ''   #http版本
        self.headers = {}      #请求headers 

    def parse(self, request_data):
        #解析http请求
        list = request_data.split('\n')
        self.method, self.path, self.version = list[0].split(' ')
        for str in list[1:]:
            key = ''
            value = ''
            if (len(str) <=  1):
                break
            key, value = str.split(': ')
            self.headers[key] = value

    def GetMethod(self):
        return self.method

    def GetPath(self):
        return self.path

    def GetVersion(self):
        return self.version

    def GetHeaders(self):
        return self.headers

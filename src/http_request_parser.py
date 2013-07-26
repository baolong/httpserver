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
        num = 0
        list = request_data.splitlines(0)
        while (list[0][num] != ' '):
            self.method += list[0][num]
            num += 1
        num += 1
        while (list[0][num] != ' '):
            self.path += list[0][num]
            num += 1
        num += 1
        for ch in list[0][num:]:
            self.version += ch 
        
        
        list = request_data.split('\n')
        for str in list[1:]:
            key = ''
            value = ''
            if (len(str) <=  1):
                break
            key, value = str.split(': ')
            self.headers[key] = value
        print '请求:\n' + request_data

    def GetMethod(self):
        return self.method

    def GetPath(self):
        return self.path

    def GetVersion(self):
        return self.version

    def GetHeaders(self):
        return self.headers

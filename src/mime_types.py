#!/usr/bin/env python
# -*- coding: utf8

#根据文件名解析content-type
def filename_to_type(filename):
    postfix = ''
    name, postfix = filename.split('.')
    return postfix

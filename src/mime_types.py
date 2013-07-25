#!/usr/bin/env python
# -*- coding: utf8

#根据文件名解析content-type
def filename_to_type(filename):
    postfix = ''
    type = {                   \
        'gif' : 'image/gif',   \
        'htm' : 'text/html',   \
        'html': 'text/html',   \
        'jpg' : 'image/jpeg',  \
        'png' : 'image/png'    \
    } 
    name, postfix = filename.split('.')
    return type[postfix]

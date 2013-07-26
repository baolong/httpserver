#!/usr/bin/env python
# -*- coding: utf8

def render(templatename, dict):
    fp = open(templatename)
    template = fp.read()
    fp.close()
    str = template.format(**dict)
    return str

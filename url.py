#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""

import importlib,sys  #utf-8，兼容汉字
importlib.reload(sys)
from handlers.index import IndexHandler    #假设已经有了
url = [
    (r'/', IndexHandler),
]
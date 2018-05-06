# coding=utf-8
# author: jenifly

import importlib,sys  #utf-8，兼容汉字
importlib.reload(sys)

from handlers.base import BaseHandler, testHandler
from handlers.chat import chatBasicHandler, homeHandler, newChatStatus 

url = [
    (r'/', BaseHandler),
    (r"/test/([0-9]+)", testHandler),
    (r'/chat', chatBasicHandler),
    (r'/chat/home/', homeHandler),
    (r'/chat/newChatStatus/', newChatStatus),
]
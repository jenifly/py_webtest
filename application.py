# coding=utf-8
# author: jenifly

from url import url

import tornado.web
import os
from methods.chatHome import ChatHome

class Application(tornado.web.Application):
    def __init__(self):
        self.chathome = ChatHome()

        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "statics")
            )
            
        tornado.web.Application.__init__(self, handlers = url, **settings)
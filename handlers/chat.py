# coding=utf-8
# author: jenifly

import json
import tornado.web
import tornado.websocket
from uuid import uuid4

class chatBasicHandler(tornado.web.RequestHandler):
    '''
        主页， 选择进入聊天室
    '''
    def get(self):
        session = uuid4()   #生成随机标识码，代替用户登录
        self.render('chat/basic.html', session = session)

class homeHandler(tornado.web.RequestHandler):
    '''
        聊天室， 获取主页选择聊天室跳转的get信息渲染页面
    '''
    def get(self):
        n = self.get_argument('n')      #聊天室
        u = self.get_argument('u')      #用户
        self.render('chat/home.html', n=n, u=u)


class newChatStatus(tornado.websocket.WebSocketHandler):
    '''
        websocket， 记录客户端连接，删除客户端连接，接收最新消息
    '''
    def open(self):
        n = str(self.get_argument('n'))
        self.write_message(json.dumps({'from':'sys', 'message':'欢迎来到 聊天室（%s）' % n}))      #向新加入用户发送首次消息
        self.application.chathome.register(self)    #记录客户端连接

    def on_close(self):
        self.application.chathome.unregister(self)  #删除客户端连接

    def on_message(self, message):
        self.application.chathome.callbackNews(self, message)   #处理客户端提交的最新消息
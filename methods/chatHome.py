# coding=utf-8
# author: jenifly

import json


class ChatHome(object):
    '''
        处理websocket 服务器与客户端交互
    '''
    chatRegister = {}

    def register(self, newer):
        '''
            保存新加入的客户端连接、监听实例，并向聊天室其他成员发送消息！
        '''
        home = str(newer.get_argument('n'))     #获取所在聊天室
        if home in self.chatRegister:
            self.chatRegister[home].append(newer)
        else:
            self.chatRegister[home] = [newer]

        message = {
            'from': 'sys',
            'message': '%s 加入聊天室（%s）' % (str(newer.get_argument('u')), home)
        }
        self.callbackTrigger(home, message)

    def unregister(self, lefter):
        '''
            客户端关闭连接，删除聊天室内对应的客户端连接实例
        '''
        home = str(lefter.get_argument('n'))
        self.chatRegister[home].remove(lefter)
        if self.chatRegister[home]:
            message = {
                'from': 'sys',
                'message': '%s 离开聊天室（%s）' % (str(lefter.get_argument('u')), home)
            }
            self.callbackTrigger(home, message)

    def callbackNews(self, sender, message):
        '''
            处理客户端提交的消息，发送给对应聊天室内所有的客户端
        '''
        home = str(sender.get_argument('n'))
        user = str(sender.get_argument('u'))
        message = {
            'from': user,
            'message': message
        }
        self.callbackTrigger(home, message)

    def callbackTrigger(self, home, message):
        '''
            消息触发器，将最新消息返回给对应聊天室的所有成员
        '''
        for callbacker in self.chatRegister[home]:
            callbacker.write_message(json.dumps(message))
#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.readdb as mrd

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.write("welcome you: " + username)
            else:
                self.write("your password was not right.sss")
        else:
            self.write("There is no thi user.")

class testHandler(tornado.web.RequestHandler): 
   def get(self, story_id): 
       self.write("xiaorui.cc niubi'id is" + story_id) 
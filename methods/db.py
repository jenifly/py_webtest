# coding=utf-8
__author__ = 'jenifly'

import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="qiwsirtest", port=3306, charset="utf8")    #连接对象

cur = conn.cursor()    #游标对象
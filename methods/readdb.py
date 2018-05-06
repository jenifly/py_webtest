#!/usr/bin/env Python
# coding=utf-8

import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="qiwsirtest", port=3306, charset="utf8")
cur = conn.cursor()

def show_table(table):
    sql = "select * from " + table
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

def select_table(table, column, condition, value ):
    sql = "select " + column + " from " + table + " where " + condition + "='" + value + "'"
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

def select_columns(table, column ):
    sql = "select " + column + " from " + table
    cur.execute(sql)
    lines = cur.fetchall()
    return lines
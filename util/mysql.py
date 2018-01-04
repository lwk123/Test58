#!/usr/bin/python
#coding:utf-8
#获取mysql连接，统一都用这个，引用时通过import util.mysql，使用时也是util.mysql.conn或util.mysql.cur

import ConfigParser
import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

config = ConfigParser.ConfigParser()
config.readfp(open("../config.properties", "rb"))
session_name = 'mysql'

conn = MySQLdb.connect(
        host=config.get(session_name,'host'),
        port = 3306,
        user=config.get(session_name, 'username'),
        passwd=config.get(session_name, 'password'),
        db=config.get(session_name, 'dbname'),
        charset='utf8')

conn.ping(True)

cur = conn.cursor()

def connect():
    conn = MySQLdb.connect(
        host=config.get(session_name, 'host'),
        port=3306,
        user=config.get(session_name, 'username'),
        passwd=config.get(session_name, 'password'),
        db=config.get(session_name, 'dbname'),
        charset='utf8')
    conn.ping(True)
    cur = conn.cursor()

"""
user = cur.execute("select * from user")

info = cur.fetchmany(user)
for ii in info:
    print ii

cur.close()
conn.commit()
conn.close()
"""
#!/usr/bin/python
#coding:utf-8

import ConfigParser
import pymongo
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def connect():
    client = pymongo.MongoClient('localhost',27017)
    proxy = client['proxy']
    proxy_list = proxy['proxy_list']
    return proxy_list
connect()
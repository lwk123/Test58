#coding:utf-8
#获取日期

import sys
import time
from datetime import timedelta, datetime

reload(sys)
sys.setdefaultencoding('utf8')

#获取当前日期
def get_current_date():
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))

#获取当前时间
def get_current_datetime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

#获取前一天
def get_previous_date():
    yesterday = datetime.today() + timedelta(-1)
    return yesterday.strftime('%Y-%m-%d')

#获取前两天
def get_pre_pre_date():
    yesterday = datetime.today() + timedelta(-2)
    return yesterday.strftime('%Y%m%d')

#获取前一天
def get_pre_date():
    yesterday = datetime.today() + timedelta(-1)
    return yesterday.strftime('%Y%m%d')

#获取后一天
def get_next_date():
    yesterday = datetime.today() + timedelta(1)
    return yesterday.strftime('%Y%m%d')

#获取当前的毫秒
def get_milliseconds():
    return int(round(time.time() * 1000))

#获取指定时间的字符串
def get_appoint_date(interval,dateformat):
    return (datetime.today()+timedelta(interval)).strftime(dateformat)

#时间戳转换成时间
def timestamp_totime(timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

#时间戳转换成日期
def timestamp_todate(timestamp):
    return time.strftime('%Y-%m-%d', time.localtime(timestamp))
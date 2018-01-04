#coding:utf-8
#每次随机获取一个代理
import mysql
import sys
import random

reload(sys)
sys.setdefaultencoding('utf-8')


#获取代理，返回{protocol:'http/https',ip:'1.2.3.4:20'}
def getproxy():
    sql = "select * from ods_proxy where protocol='http' order by responsetime limit 20"
    conn = mysql.conn
    cur = mysql.cur
    cur.execute(sql)
    results = cur.fetchall()
    data = results[random.randint(0,len(results)-1)]
    proxy = {
        'protocol':data[2],
        'ip':data[1]
    }
    conn.commit()

    return proxy

def getcommonproxy():

    sql = "select * from ods_proxy"
    conn = mysql.conn
    cur = mysql.cur
    cur.execute(sql)
    results = cur.fetchall()
    data = results[random.randint(0, len(results) - 1)]
    proxy = {
        'protocol': data[2],
        'ip': data[1]
    }
    conn.commit()

    return proxy


#获取https代理，返回{protocol:'http/https',ip:'1.2.3.4:20'}
def gethttpsproxy():
    sql = "select * from ods_proxy where protocol='https' order by responsetime limit 20"
    conn = mysql.conn
    cur = mysql.cur
    cur.execute(sql)
    results = cur.fetchall()
    data = results[random.randint(0,len(results)-1)]
    proxy = {
        'protocol':data[2],
        'ip':data[1]
    }
    conn.commit()

    return proxy

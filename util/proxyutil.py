#coding:utf-8
#每次随机获取一个代理
import sys
import random
import util.mongodb

reload(sys)
sys.setdefaultencoding('utf-8')


#获取代理，返回{protocol:'http/https',ip:'1.2.3.4:20'}
def getproxy():
    # util.mongodb.proxy_list.find().limit(20)
    results = util.mongodb.proxy_list.find().limit(20)
    data = results[random.randint(0,len(results)-1)]
    proxy = {
        'protocol':data[2],
        'ip':data[1]
    }
    # conn.commit()

    return proxy

def getcommonproxy():

    # sql = "select * from ods_proxy"
    # conn = mysql.conn
    # cur = mysql.cur
    # cur.execute(sql)
    results = util.mongodb.proxy_list.find()
    data = results[random.randint(0, len(results) - 1)]
    proxy = {
        'protocol': data[2],
        'ip': data[1]
    }
    # conn.commit()

    return proxy


#获取https代理，返回{protocol:'http/https',ip:'1.2.3.4:20'}
def gethttpsproxy():
    # sql = "select * from ods_proxy where protocol='https' order by responsetime limit 20"
    # conn = mysql.conn
    # cur = mysql.cur
    # cur.execute(sql)
    results = util.mongodb.proxy_list.find({'protocol':'https'}).limit(20)
    data = results[random.randint(0,len(results)-1)]
    proxy = {
        'protocol':data[2],
        'ip':data[1]
    }
    # conn.commit()

    return proxy

#coding:utf-8
#定时获取代理，并且写入到数据库中

import sys
import time
import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
sys.path.append('..')
# import util.mysql
import util.mongodb
import util.driverutil
import util.headerutil
import random


reload(sys)
sys.setdefaultencoding('utf8')


def init():
    # conn = util.mysql.conn
    # cur = util.mysql.cur
    proxy_list = util.mongodb.proxy_list
    url = 'http://www.ip181.com/'
    driver = util.driverutil.get_driver(url)
    time.sleep(5)

    count = 0
    while(driver is None or driver.page_source == '<html><head></head><body></body></html>'):
        driver = util.driverutil.get_driver(url)
        ran_time = random.randint(5,10)
        print 'error,change proxy and retry,sleep %d seconds' % ran_time
        time.sleep(ran_time)
        if(count > 10):
            break
        count += 1
    proxy_list.drop()
    #delete_sql = 'delete from ods_proxy'
    #cur.execute(delete_sql)

    if(driver is None or driver.page_source == '<html><head></head><body></body></html>'):
        print 'get proxy url failure,break'
        #util.mailutil.send_email('362702750@qq.com', '获取代理error', '获取代理error')

    print '......'
    print driver.page_source

    if(len(driver.find_elements_by_xpath("//table[@class='table table-hover panel-default panel ctable']/tbody/tr")) == 1):
        print 'get proxy url failure,break'
        #util.mailutil.send_email('362702750@qq.com','获取代理error','获取代理error')

    for tr in driver.find_elements_by_xpath("//table[@class='table table-hover panel-default panel ctable']/tbody/tr")[1:]:
        tds = tr.find_elements_by_xpath("./td")
        ip = tds[0].text.strip()
        port = tds[1].text.strip()
        protocol = tds[3].text.strip()
        responsetime = tds[4].text.strip()
        print 'ip:%s,port:%s,protocol:%s' % (ip, port, protocol)
        #代理可用
        #if(isusable(responsetime)=='success' and testavailable(ip+':'+port,protocol.lower())=='success'):
        if(protocol.find(",")>0):
            protocol = 'http'
            addProxy(ip+':'+port, protocol.lower(), responsetime, proxy_list)
            protocol = 'https'
            addProxy(ip + ':' + port, protocol.lower(), responsetime, proxy_list)
        else:
            protocol = 'http'
            addProxy(ip + ':' + port, protocol.lower(), responsetime, proxy_list)

    #time.sleep(3)

#从http://www.66ip.cn/index.html获取代理
def get_ip_from_66ip(url):
    driver = util.driverutil.get_driver_without_proxy(url)
    time.sleep(5)
    cur = util.mongodb.proxy_list

    count = 0
    while (driver is None or driver.page_source == '<html><head></head><body></body></html>'):
        driver = util.driverutil.get_driver_without_proxy(url)
        ran_time = random.randint(5, 10)
        print 'error,change proxy and retry,sleep %d seconds' % ran_time
        time.sleep(ran_time)
        if (count > 10):
            break
        count += 1

    if (driver is None or driver.page_source == '<html><head></head><body></body></html>'):
        print 'get proxy url failure,break'
        return

    for tr in driver.find_elements_by_xpath("//div[@class='containerbox boxindex']/div/table/tbody/tr")[1:]:
        tds = tr.find_elements_by_xpath("./td")
        ip = tds[0].text.strip()
        port = tds[1].text.strip()
        protocol = 'http,https'
        responsetime = 0
        print 'ip:%s,port:%s,protocol:%s' % (ip, port, protocol)
        # 代理可用
        if (protocol.find(",") > 0):
            protocol = 'http'
            addProxy(ip + ':' + port, protocol.lower(), responsetime, cur)
            protocol = 'https'
            addProxy(ip + ':' + port, protocol.lower(), responsetime, cur)
        else:
            protocol = 'http'
            addProxy(ip + ':' + port, protocol.lower(), responsetime, cur)



def init_next():
    # conn = util.mysql.conn
    cur = util.mongodb.proxy_list
    print "开始代理ip获取"
    url = 'http://www.xicidaili.com/nn/'
    driver = util.driverutil.get_driver_without_proxy(url)
    time.sleep(5)
    print len(driver.find_elements_by_xpath("//table[@id='ip_list']/tbody/tr"))
    for tr in driver.find_elements_by_xpath("//table[@id='ip_list']/tbody/tr")[1:]:
        ip = tr.find_element_by_xpath("./td[2]").text.strip()
        port = tr.find_element_by_xpath("./td[3]").text.strip()
        protocol = tr.find_element_by_xpath("./td[6]").text.strip()
        responsetime = tr.find_element_by_xpath("./td[7]/div").get_attribute("title").strip()
        print 'ip:%s,port:%s,protocol:%s' % (ip, port, protocol)
        #代理可用
        #if(isusable(responsetime)=='success' and testavailable(ip+':'+port,protocol.lower())=='success'):
        if(protocol.find(",")>0):
            protocol = 'http'
            addProxy(ip+':'+port, protocol.lower(), responsetime, cur)
            protocol = 'https'
            addProxy(ip + ':' + port, protocol.lower(), responsetime, cur)
        else:
            protocol = 'http'
            addProxy(ip + ':' + port, protocol.lower(), responsetime, cur)

    driver.get('http://www.xicidaili.com/nn/2')
    time.sleep(5)
    print len(driver.find_elements_by_xpath("//table[@id='ip_list']/tbody/tr"))
    for tr in driver.find_elements_by_xpath("//table[@id='ip_list']/tbody/tr")[1:]:
        ip = tr.find_element_by_xpath("./td[2]").text.strip()
        port = tr.find_element_by_xpath("./td[3]").text.strip()
        protocol = tr.find_element_by_xpath("./td[6]").text.strip()
        responsetime = tr.find_element_by_xpath("./td[7]/div").get_attribute("title").strip()
        print 'ip:%s,port:%s,protocol:%s' % (ip, port, protocol)
        # 代理可用
        # if(isusable(responsetime)=='success' and testavailable(ip+':'+port,protocol.lower())=='success'):
        if (protocol.find(",") > 0):
            protocol = 'http'
            addProxy(ip + ':' + port, protocol.lower(), responsetime, cur)
            protocol = 'https'
            addProxy(ip + ':' + port, protocol.lower(), responsetime, cur)
        else:
            protocol = 'http'
            addProxy(ip + ':' + port, protocol.lower(), responsetime, cur)
    driver.close()


#判断响应时间是否合理
def isusable(responsetime):
    responsetime = responsetime.replace(' ','').replace('秒','')
    if(float(responsetime)<5):
        return 'success'
    return 'failure'

def addProxy(ip,protocol,responsetime,cur):
    try:
        if protocol == 'http':
            requests.get('http://httpbin.org/ip', proxies={"http": "http://"+ip}, timeout=5)
        elif protocol == 'https':
            requests.get('https://www.ipip.net/', proxies={"https": "https://"+ip}, timeout=5)
    except:
        print '%s://%s connect failed' % (protocol, ip)
    else:
        print '%s://%s connect success' % (protocol, ip)
        if(whether_exist(ip,protocol) == False):
            cur.insert({'ip': ip, 'protocol': protocol, 'responsetime': responsetime})
            # sql = "insert into ods_proxy(ip,protocol,createTime,responsetime) values('%s','%s',now(),'%s')" % (ip, protocol, responsetime)
            # cur.execute(sql)
            # util.mysql.conn.commit()

def whether_exist(ip,protocol):
    # util.mongodb.proxy_list.find({'ip':ip},{'protocol':protocol})
    # sql = "select id from ods_proxy where ip='%s' and protocol='%s'" % (ip,protocol)
    # util.mysql.cur.execute(sql)
    results =  util.mongodb.proxy_list.find({'ip':ip},{'protocol':protocol})
    if(len(results)>0):
        return True
    return False

def deal_existing_proxy():
    results = util.mongodb.proxy_list.find()
    # ids = '('
    for row in results:
        ip = row[0]
        protocol = row[1]
        id = row[2]
        try:
            if protocol == 'http':
                requests.get('http://httpbin.org/ip', proxies={"http": "http://" + ip}, timeout=5)
            elif protocol == 'https':
                requests.get('https://www.ipip.net/', proxies={"https": "https://" + ip}, timeout=5)
        except:
            print '%s://%s connect failed' % (protocol, ip)
            util.mongodb.proxy_list.delete_many({'ip':ip},{'protocol':protocol})
    # ids+='-1)'
    # print ids
    # util.mongodb.proxy_list.delete_many()
    # del_sql = "delete from ods_proxy where id in %s" % ids
    # util.mysql.cur.execute(del_sql)
    # util.mysql.conn.commit()

def main():
    # deal_existing_proxy()
    # del_sql = "delete from ods_proxy"
    # util.mysql.cur.execute(del_sql)
    # util.mysql.conn.commit()
    util.mongodb.proxy_list.drop()
    init_next()
    for p in range(1, 3):
        get_ip_from_66ip("http://www.66ip.cn/%d.html" % p)
        print 'page %d finish' % p
        time.sleep(random.randint(30, 60))


main()
#init()

#selenium_use_poxy()

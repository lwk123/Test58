#coding:utf-8
#提供selenium的driver
from selenium import webdriver
from bs4 import BeautifulSoup
import util.headerutil
import util.proxyutil
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#自定义header
def init_phantomjs_driver(*args, **kwargs):

    for key, value in util.headerutil.get_header().iteritems():
        webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value
    #不加载图片
    webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.loadImages'] = False

    driver =  webdriver.PhantomJS(*args, **kwargs)
    driver.set_window_size(1400,1000)
    #超时时间
    driver.set_page_load_timeout(10)

    return driver



#加代理获取driver
def get_driver(url):
    proxy = util.proxyutil.getcommonproxy()
    print proxy
    driver = init_phantomjs_driver(service_args=[
        '--proxy=' + proxy['ip'],
        '--proxy-type=' + proxy['protocol']])
    try:
        driver.get(url)
        return  driver
    except Exception as r:
        print "error"
        return None

#加代理获取driver
def get_driver_without_proxy(url):
    driver = init_phantomjs_driver(service_args=[])
    try:
        driver.get(url)
        return driver
    except Exception as r:
        print "error"
        return None

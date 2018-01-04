from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list2']
item_info = ceshi['item_info']

#spider 1
def get_links_from(channel,pages,who_sells=0):
    list_view = '{}pn{}/'.format(channel,str(pages))
    wb_data = requests.get(list_view)
    requests.get()
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find('td','t'):
        count = 0
        for link in soup.select('div[id="infolist"] a[class="t"]'):
            item_link = link.get('href').split('?')[0]
            if 'jump' not in item_link:
                url_list.insert({'url':item_link})
                count = count + 1
                print (item_link+'-----'+link.text)
            else:
                pass
        print (list_view + ':::::' + str(count))
    else:
        pass

def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find('span','soldout_btn'):
        pass
    else:
        title = soup.find('h1','info_titile').text
        price = soup.select('span[class="price_now"] > i')[0].text
        area = list(soup.select('div[class="palce_li"] > span > i')[0].text.split('-'))
        item_info.insert({'title':title,'price':price,'area':area})
        print ({'title':title,'price':price,'area':area})
# get_item_info('http://zhuanzhuan.58.com/detail/940815222691807241z.shtml')
# get_links_from('http://bj.58.com/bijiben/',1)
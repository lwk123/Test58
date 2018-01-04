#coding:utf-8
#从36ke 抓取新闻
import sys
#为了引用别的文件
sys.path.append('..')
import util.mysql

def main():
    sql = "select investors_text from ods_org_finance"
    util.mysql.cur.execute(sql)
    results = util.mysql.cur.fetchall()
    count = 0
    print len(results)
    for row in results:
        investor = row[0]
        print 'investor = %s count = %d' % (investor,count)
        if(investor is None or investor.find("未透露")>-1):
            continue
        investors = investor.split(",")
        for inve in investors:
            sql2 = "insert into ods_investors(investor) values('%s')" % inve
            util.mysql.cur.execute(sql2)
        print 'count = %d' % count
        count += 1
        if(count % 100 == 0):
            util.mysql.conn.commit()

def deal_similar_org():
    sql = "select DISTINCT brand from ods_org_finance as fin where brand is not null"
    util.mysql.cur.execute(sql)
    results = util.mysql.cur.fetchall()
    for row in results:
        brand = row[0]
        sql2 = "select brand from ods_org_finance as fin where brand like concat('%%','%s','%%') and brand != '%s'" % (brand,brand)
        util.mysql.cur.execute(sql2)
        results2 = util.mysql.cur.fetchall()
        for row2 in results2:
            brand2 = row2[0]
            sql3 = "insert into ods_name_relation(realname,similarname,createtime,creator,type) values('%s','%s',now(),'卫占魁','自动添加')" % (brand,brand2)
            util.mysql.cur.execute(sql3)
        print '处理%s,相似的有%d个' % (brand,len(results2))
        util.mysql.conn.commit()

#main()
deal_similar_org()


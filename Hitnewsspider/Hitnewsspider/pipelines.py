# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


mysqlHost="localhost"
mysqlUser="root"
mysqlPasswd="gg19970110"
mysqldatabase="newstest"
#
# '''
# ---------------------------------------------------------
# '''
#
#
#



conn=pymysql.connect(host=mysqlHost,user=mysqlUser,password=mysqlPasswd,db=mysqldatabase,charset="utf8",port=3306)
cursor = conn.cursor()

class HaveatryPipeline(object):
    def process_item(self, item, spider):

        print('--------------------------')
        content=item['content']
        title=item['title']
        link=item['link']
        print(title)
        with open('file.txt','a') as f:
            f.write(str(content))



        sql = 'INSERT INTO newspaper(link,title,content)    VALUES (%s,%s,%s)'
        cursor.execute(sql, (link, title, content))
        #try:
            # 执行sql语句
        cursor.execute(sql, (link, title, content))
            # 提交到数据库执行
        conn.commit()
        print('-----------------insert success-------------------')
        #except:
             # 如果发生错误则回滚
             #conn.rollback()


        return item

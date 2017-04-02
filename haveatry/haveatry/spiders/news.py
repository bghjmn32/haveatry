# -*- coding: utf-8 -*-
import sys
import importlib
importlib.reload(sys)
from bs4 import BeautifulSoup

import scrapy
from haveatry.items import HaveatryItem
from scrapy.spiders import Spider
from scrapy.selector import Selector

class newsworm(scrapy.Spider):
    name = 'news'
    allowed_domains = ["news.hitwh.edu.cn"]
    start_urls=['http://news.hitwh.edu.cn/news_list.asp?id=1&page=1']#从第一页开始爬取
    #从起始新闻页开始爬取,根据ID规律进行叠加爬取新闻


    def parse(self, response):

        soup = BeautifulSoup(response.body, 'lxml', from_encoding='utf8')
    #使用"美丽的汤"进行response调用,编码方式为uhf-8
        content = soup.find('table')
        tpage=content.find('strong').contents[1].strip('/')
        tpage=int(tpage)
        for i in range(1,3):
            next_url='http://news.hitwh.edu.cn/news_list.asp?id=1&page='+str(i)
            yield scrapy.Request(next_url, callback=self.parse1)
    #使用字符串进行递推找到地址进行下一步的爬取




    def parse1(self,response):
        for sel in response.xpath('//*[@id="news_list"]/ul/li'):
        #循环具体组合
            if not sel.xpath('a'):
                continue
            link='http://news.hitwh.edu.cn/'+sel.xpath('a/@href')[0].root

            yield scrapy.Request(link,callback=self.parse2)


    def parse2(self,response):
        newitem=HaveatryItem()


        title=response.xpath('//*[@id="show_left_news"]/div[1]/text()').extract()[0]
        #获取新闻标题
        link=response.url
        #获取这个新闻的链接

        soup0 = BeautifulSoup(response.body, 'lxml', from_encoding='utf8')
        #获取新闻内容
        content = soup0.find(attrs={'id': 'newsContnet'})
        line = content.text
        #在LINE里存储新闻内容
        newitem['content']=line
        #这三行把内容,标题和链接存到item里面去
        newitem['title']=title
        newitem['link']=link
        yield newitem
        #返回这个item,返回的item调用pipelines.py函数处理


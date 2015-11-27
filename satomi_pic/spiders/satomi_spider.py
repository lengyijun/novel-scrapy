# -*- coding:utf-8 -*-
__author__ = 'church-father'

from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from satomi_pic.items import SatomiPicItem


class SatomiSpider(CrawlSpider):
    name="satomi_pic_spider"

    #download_delay=1

    # from the last page to crawl to the first page
    start_urls=[
        "http://www.kanshu.la/book/zetianji/8372193.html"
    ]

    rules=(
        # Rule(LinkExtractor(allow=(r'\d{7}.html'),restrict_xpaths=('//a[starts-with(@id=a_03)]')),callback='parse_item',follow=True),
        Rule(LinkExtractor(allow=(r'\d{7}.html')),callback='parse_item',follow=True),
        # Rule(LinkExtractor(allow=(r'\d{7}.html'),restrict_xpaths=('//a[@id=a_03]')),callback='parse_item',follow=True),
    )

    def parse_item(self, response):
        sel=Selector(response)
        item=SatomiPicItem()

        if response.url>="http://www.kanshu.la/book/zetianji/8357143.shtml":

            title=sel.xpath('//title/text()').extract()
            item['title']=[t.encode('utf-8') for t in title]
            path='/home/church-father/Documents/zetianji2/title'
            output2=open(path,'a')
            ss=''
            n=0
            while n<len(item['title']):
                ss+=str(item['title'][n])
                n+=1
            output2.write(ss)
            output2.write('\n')

            content=sel.xpath('//div[@id="contentTxt"]/text()').extract()
            item['content']=[t.encode('utf-8') for t in content]
            path='/home/church-father/Documents/zetianji2/'+ss
            output1=open(path,'a')
            ss1=''
            n=0
            while n<len(item['content']):
                ss1+=str(item['content'][n])
                n+=1
            output1.write(ss)
            output1.write(ss1)
            output1.close()

            yield item
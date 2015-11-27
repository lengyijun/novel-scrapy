# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request

class SatomiPicPipeline(object):
    def process_item(self, item, spider):
        # t=item['content'].decode('utf-8')
        t=item['content'].decode('utf-8')
        path='/home/church-father/Documents/novel/new3.txt'
        output=open(path,'a')
        output.write(t)
        output.close()
        return item


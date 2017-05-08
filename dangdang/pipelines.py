# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class DangdangPipeline(object):
    def process_item(self, item, spider):
    	for j in range(len(item["title"])):
    		print(j)
    		title = item["title"][j]
    		num = item["num"][j]
    		print("商品名："+title)
    		print("商品评论数："+num)
    		print("-----------------------------")
    	return item

# -*- coding: utf-8 -*-
import scrapy
import re
from dangdang.items import DangdangItem
from scrapy.http import Request

class DangspdSpider(scrapy.Spider):
    name = "dangspd"
    allowed_domains = ["dangdang.com"]
    start_urls = (
    	'http://category.dangdang.com/pg1-cid4002644.html'
    )
    
    def parse(self, response):
        item = DangdangItem()
        item["title"] = response.xpath("//a[@class='pic']/@title").extract()
        item["num"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        yield item
        for i in range(2,101):
            url = "http://category.dangdang.com/pg"+str(i)+"-cid4002644.html"
            yield Request(url,callback=self.parse)


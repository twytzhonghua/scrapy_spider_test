# -*- coding: utf-8 -*-
import scrapy


class TbaiduSpider(scrapy.Spider):
    name = "tbaidu"
    allowed_domains = ["www.baidu.com"]
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
		#title = response.xpat
        print(response)

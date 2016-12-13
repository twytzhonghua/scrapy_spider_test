# -*- coding: utf-8 -*-
import scrapy


class TbaiduSpider(scrapy.Spider):
	name = "tbaidu"
	allowed_domains = ["www.baidu.com"]
	start_urls = ['http://www.baidu.com/']

	def parse(self, response):
		sel = scrapy.selector.Selector(response)
		title = sel.xpath("//title/text()").extract()
		#title = response.xpat
		print(title)

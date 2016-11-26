#-*- coding: utf-8 -*-
import scrapy
from lxml import etree
import urllib
import re
import sys
from tutorial.items import DmozeItem
import codecs
import json
import sqlite3
import os

#reload(sys)
#sys.setdefaultencoding("utf-8")

class StockSpider(scrapy.Spider):
	name = "stock_yidian"
	allowed_domains = ['yidiancangwei.com']
	start_urls = [
		#'http://stockpage.10jqka.com.cn/000935/holder/'
		'http://www.yidiancangwei.com/gudong/sdlt_300111_2015_06_30.html'
	]
	
	
	#流通股东数据
	def checkLTGD(self, response):
		sel = scrapy.selector.Selector(response)
		self.stock_name = sel.xpath('//div[@class="Title shareTit"]/span[@class="blue"]/text()').extract()
		
		print(self.stock_name)
		
		LTGD_body = sel.xpath('//div[@class="TabBox"]')
		one_jidu_info_divs = LTGD_body.xpath('.//tr')
		
		for one_gudong_info in one_jidu_info_divs:
			LTGD_name = one_gudong_info.xpath('.//a/text()').extract()
			other_info = one_gudong_info.xpath('.//td/text()').extract()
			print(LTGD_name)
			print(other_info)
		
	
	def parse(self, response):
		
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		match = pattern.search(str(response)) 
		if match:
			self.stock_num = match.group()
			print("stock_num %s" % str(self.stock_num))
			self.checkLTGD(response)

		
		#return self.items
	

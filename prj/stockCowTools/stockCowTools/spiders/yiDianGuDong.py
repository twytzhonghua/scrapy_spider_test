# -*- coding: utf-8 -*-
import scrapy
import re
import sys
#import dataHtmlParse
from stockSMT.stockSql import *
from stockSMT.dataHtmlParse import *


class YidiangudongSpider(scrapy.Spider):
	name = "yiDianGuDong"
	allowed_domains = ["yidiancangwei.com"]
	start_urls = [
	#'http://www.yidiancangwei.com/gudong/sdlt_300111_2015_06_30.html'
	]

	with open('C:/scrapy/crawls_urls.txt', 'r') as f:
		for line in f.readlines():
			start_urls.append(line.strip())
					

	def parse(self, response):
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		match = pattern.search(str(response)) 
		if match:
			self.stock_num = match.group()
			#print("stock_num %s" % str(self.stock_num))
			# yiDianCheckLTGD(response)
		
	

		



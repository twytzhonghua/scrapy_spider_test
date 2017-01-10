# -*- coding: utf-8 -*-
import scrapy
import re
import sys

from stockCowTools.spiders.stockSql import *
from stockCowTools.spiders.dataHtmlParse import *

class ThsgudongSpider(scrapy.Spider):
	name = "ths2"
	allowed_domains = ['10jqka.com.cn']
	start_urls = [
	#	'http://stockpage.10jqka.com.cn/000935/holder/'
	]

	with open('C:/scrapy/ths_urls.txt', 'r') as f:
		for line in f.readlines():
			start_urls.append(line.strip())
		
	#print(start_urls)

	#流通股东数据
	def checkLTGD(self, response):
		sel = scrapy.selector.Selector(response)
		LTGD_body = sel.xpath('//div[@id="flowholder"]')
		date_time = LTGD_body.xpath('.//li/a[@class="fdates"]/text()').extract()
		print(date_time)
		all_info = []
		date_length = len(date_time)
		
		cur_seq = 0
		one_jidu_info_divs = LTGD_body.xpath('.//table[@class="m_table m_hl ggintro"]')
		print("gudong info parts %d" % len(one_jidu_info_divs))
		for one_jidu_info in one_jidu_info_divs:
			one_gudong_info_divs = one_jidu_info.xpath('.//tr')
			#print("gudong info member %d" % len(one_gudong_info_divs))
			for one_gudong_info in one_gudong_info_divs:
				name = one_gudong_info.xpath('.//th[@class="tl holder_th"]/a/text()').extract()
				info = one_gudong_info.xpath('.//td/text()').extract()
				#print('---------------------------------------------------------')
				#print(info)
				#print("list len %d" % len(info))
				if (name and info):
					gdname = name[0]
					hold_num = info[0]
					percent = info[2]
					stock_type = info[-1].strip()
					date = date_time[cur_seq]
					stock_number = self.stock_num
					stock_name = self.cName
					#print('stock_number = ', stock_number)
					#print('stock_name =', stock_name)	
					#print('gdname =', gdname)				
					#print('percent =', percent)
					#print('hold_num =', hold_num)
					#print('stock_type =', stock_type)
					#print('date =',date)
			#stock_number varchar(20), stock_name varchar(20), gudong_name varchar(100),  hold_num varchar(20), percent varchar(20), date varchar(20), stock_type varchar(20)
			gdinfo = (stock_number, stock_name,  gdname,  hold_num,  percent, date,  stock_type)
			all_info.append(gdinfo)
			cur_seq += 1
		
		store_lt_gudong_db(all_info)
	
	def checkCName(self,response):
		sel = scrapy.selector.Selector(response)
		self.cName = sel.xpath('//strong/text()').extract()
		print('cName = ', self.cName)
	
	def parse(self, response):
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		match = pattern.search(str(response)) 
		if match:
			self.stock_num = match.group()
			print("stock_num =", str(self.stock_num))
			self.checkCName(response)
			self.checkLTGD(response)
			
	

		



# -*- coding: utf-8 -*-
import scrapy
import re
import sys
import urllib.request
from stockCowTools.spiders.stockSql import *
from stockCowTools.spiders.dataHtmlParse import *
from stockCowTools.spiders.update_stock import * 

class DzhgudongSpider(scrapy.Spider):
	name = "dzh"
	allowed_domains = ['webf10.gw.com.cn']
	start_urls = [
		# 'http://webf10.gw.com.cn/SH/B10/SH600767_B10.html#'
	]

	with open('C:/scrapy/dzh_urls.txt', 'r') as f:
		for line in f.readlines():
			start_urls.append(line.strip())
	
	self_dict = generate_stock_dic()
	#print(start_urls)

	#流通股东数据
	def checkLTGD(self, response):
		sel = scrapy.selector.Selector(response)
		# <section class="sdgdBox dzh_index" id="十大流通股东">
		LTGD_body = sel.xpath('//section[@id="十大流通股东"]')
		body = sel.xpath('//nav[@class="sdgd_nav clearfix"]')
		dateList = body.xpath('.//a/text()').extract()
		# print('dateList = ', dateList)
		h2 = LTGD_body.xpath('.//h2/text()').extract()
		# print('h2 = ', h2)

		all_info = []
		#date_length = len(date_time)
		
		cur_seq = 0
		
		one_jidu_info_divs = LTGD_body.xpath('.//div[@class="sdgdCon  sdltgdTb"]')
		jd_parts = len(one_jidu_info_divs)
		# print("gudong info parts %d" % len(one_jidu_info_divs))
		for one_jidu_info in one_jidu_info_divs:
			#<table class="f10tabel sdgd_table">
			one_gudong_info_divs = one_jidu_info.xpath('.//table[@class="f10tabel sdgd_table"]')
			#print("gudong info member %d" % len(one_gudong_info_divs))
			#for one_gudong_info in one_gudong_info_divs:
			name = one_gudong_info_divs.xpath('.//td/a/text()').extract()
			info = one_gudong_info_divs.xpath('.//td/text()').extract()
			# print('---------------------------------------------------------')
			name_len = len(name) + 1

			if (name and info):
				for i in range(1,name_len):
					# print('cur = ', i)
					"""
					'1.', '5350.83', '未变', '15.70', '流通A股',
					"""
					gdname = name[i-1]
					hold_num = info[5*(i-1) + 1]
					change = info[5*(i-1) + 2]
					percent = info[5*(i-1) + 3]
					stock_type = info[5*(i-1) + 4]
					date = dateList[-jd_parts + cur_seq]
					stock_number = self.stock_num
					Cname = self.self_dict[stock_number]
					#gdinfo = (stock_number, stock_name,  gdname,  hold_num,  percent, date,  stock_type)
					gdinfo = (stock_number, Cname,  gdname,  hold_num,  percent, change, date, stock_type)
					#print('gdinfo = ', gdinfo)
					all_info.append(gdinfo)
			cur_seq += 1
		
		# print('all_info = ', all_info)
		store_lt_gudong_db(all_info)
	
	
	def parse(self, response):
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		match = pattern.search(str(response)) 
		if match:
			self.stock_num = match.group()
			print("stock_num =", str(self.stock_num))
			self.checkLTGD(response)
			
			
	

		



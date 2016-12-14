# -*- coding: utf-8 -*-
import scrapy
import re
import sys


class YidiangudongSpider(scrapy.Spider):
	name = "yiDianGuDong"
	allowed_domains = ["yidiancangwei.com"]
	start_urls = [
	#'http://www.yidiancangwei.com/gudong/sdlt_300111_2015_06_30.html'
	]

	with open('C:/scrapy/yidian_urls.txt', 'r') as f:
		for line in f.readlines():
			start_urls.append(line.strip())
					

	def parse(self, response):
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		match = pattern.search(str(response)) 
		if match:
			self.stock_num = match.group()
			#print("stock_num %s" % str(self.stock_num))
			self.checkLTGD(response)
		
	
	def checkLTGD(self, response):
		title_name = response.xpath('//div[@class="Title shareTit"]/span[@class="blue"]/text()').extract() 
				
		#print(stock_name)
		a = title_name[0].replace(')', ' ').split('(')
			
		stock_chinese_name = a[0]
		stock_number_name = a[1]
			
		print(stock_chinese_name)
		print(stock_number_name)
			
		LTGD_body = response.xpath('//div[@class="TabBox"]')
		one_jidu_info_divs = LTGD_body.xpath('.//tr')
		all_info = []
		for one_gudong_info in one_jidu_info_divs:
			LTGD_name = one_gudong_info.xpath('.//a/text()').extract() 
			other_info = one_gudong_info.xpath('.//td/text()').extract() 
		
			if not other_info or not LTGD_name:
				pass
			else:              
				gdname = LTGD_name[0].strip()
				date = other_info[-1].strip()
				stock_name = stock_chinese_name
				percent = other_info[2].strip()  
				hold_num = other_info[3].strip()  
				increase = other_info[4].strip()  
				stock_type = other_info[5].strip()
				#print(gdname)				
				#print(percent)
				#print(hold_num)
				#print(increase)
				#print(stock_type)
				#print(date)
				#print(other_info)
				#print('-------------------------------')
				gdinfo = (gdname, date, stock_name, percent, hold_num, increase, stock_type)
				all_info.append(gdinfo)
		



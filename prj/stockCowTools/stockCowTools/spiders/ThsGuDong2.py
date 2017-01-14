# -*- coding: utf-8 -*-
import scrapy
import re
import sys
import os

import stockSMT.stockSql as stockSql
# from stockSMT.dataHtmlParse import *

class ThsgudongSpider(scrapy.Spider):
	name = "ths"
	allowed_domains = ['10jqka.com.cn']
	start_urls = [
		'http://stockpage.10jqka.com.cn/300575/holder/'
	]

	# with open('C:/scrapy/crawls_urls.txt', 'r') as f:
		# for line in f.readlines():
			# start_urls.append(line.strip())
		
	#print(start_urls)
	
	#股东人数披露
	
	def checkLTNumber(self, response):
		all_info = []
		sel = scrapy.selector.Selector(response)
		# <div class="td_w">4.73</div>
		data_list = sel.xpath('//div[@class="td_w"]/text()').extract()
		print('len = ', len(data_list))
		length =  len(data_list)
		half = (length//2) -1
		date_list = data_list[0:half]
		num_list = data_list[half+1:length-1]
		
		body = sel.xpath('//table[@class="tbody"]')
	
		info_list_text = body.xpath('.//td').extract()
		
		for i in range(half):
		# ret1 = info_list_text[i].replace('</td>', '').replace('</div>', '').split('>')[-1]
			number = num_list[i]
			ichange_percent = info_list_text[i + half + 1].replace('</td>', '').replace('</span>', '').split('>')[-1]
			date = date_list[i]
			gd_num_info = (self.stock_num, self.cName, number, ichange_percent, date)
			# print(gd_num_info)
			all_info.append(gd_num_info)
		print(all_info)
		stockSql.store_lt_gudong_num_db(all_info)

	#和上期比较持股数量变化
	def checkIchange(self, str):
		ret = str.replace('\r\n', '').replace('\t', '').replace('</s>', '').replace('<s>', '').replace('<td>', '').replace('</td>', '').strip().replace(' ', '').replace('spanclass=', '').split('</span>')
		if(len(ret) == 1):
			str = ret[0]
		else:
			str_temp1 = ret[0].split('>')
			if  '.' in str_temp1[-1]:
	#            print(str_temp1[-1])
				str_tmp2 = str_temp1[-2].replace('<', '').replace('"', '')
	#            print(str_tmp2)
				if(str_tmp2 == 'upcolor'):
					str = '+' + str_temp1[-1]
				else:
					str = str_temp1[-1]
			else:
				str = str_temp1[-1]
		return str
	
	#流通股东数据
	def checkLTGD(self, response):
		sel = scrapy.selector.Selector(response)
		LTGD_body = sel.xpath('//div[@id="flowholder"]')
		date_time = LTGD_body.xpath('.//li/a[@class="fdates"]/text()').extract()
		# print(date_time)
		all_info = []
		date_length = len(date_time)
		
		cur_seq = 0
		one_jidu_info_divs = LTGD_body.xpath('.//table[@class="m_table m_hl ggintro"]')
		# print("gudong info parts %d" % len(one_jidu_info_divs))
		for one_jidu_info in one_jidu_info_divs:
			one_gudong_info_divs = one_jidu_info.xpath('.//tr')
			#print("gudong info member %d" % len(one_gudong_info_divs))
			for one_gudong_info in one_gudong_info_divs:
				name = one_gudong_info.xpath('.//th[@class="tl holder_th"]/a/text()').extract()
				info = one_gudong_info.xpath('.//td/text()').extract()
				info_list = one_gudong_info.xpath('.//td')
				info_list_text = one_gudong_info.xpath('.//td').extract()
				if name and info_list_text and info_list:
					stock_number = self.stock_num
					Cname = self.cName
					gdname = name[0]
					hold_num = info_list[0].xpath('.//text()').extract()[0]
					percent = info_list[2].xpath('.//text()').extract()[0]
					ichange = self.checkIchange(info_list_text[1])
					date = date_time[cur_seq]
					stock_type = info_list[4].xpath('.//text()').extract()[0]					
					gdinfo = (stock_number, Cname,  gdname,  hold_num,  percent, ichange,  date,  stock_type)
					all_info.append(gdinfo)
					# print(gdinfo)
			cur_seq += 1
		
		stockSql.store_lt_gudong_db(all_info)
	
	def checkCName(self,response):
		sel = scrapy.selector.Selector(response)
		self.cName = sel.xpath('//strong/text()').extract()[0]
		# print('cName = ', self.cName)
	
	def parse(self, response):
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		match = pattern.search(str(response)) 
		if match:
			self.stock_num = match.group()
			# print("stock_num =", str(self.stock_num))
			self.checkCName(response)
			self.checkLTNumber(response)
			self.checkLTGD(response)
			
	

		



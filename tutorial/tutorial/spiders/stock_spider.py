#-*- coding: utf-8 -*-
import scrapy
from lxml import etree
import urllib
import re
import sys
from tutorial.items import DmozeItem
import codecs
import json

reload(sys)
sys.setdefaultencoding("utf-8")

class StockSpider(scrapy.Spider):
	name = "stock"
	allowed_domains = ['10jqka.com.cn']
	start_urls = [
	#	'http://stockpage.10jqka.com.cn/000935/holder/'
	]
	for line in open('sh_list'):
		a = line.strip().lstrip().rstrip('\n')
		start_urls.append('http://stockpage.10jqka.com.cn/' + a + '/holder/')
	for line in open('sz_list'):
		a = line.strip().lstrip().rstrip('\n')
		start_urls.append('http://stockpage.10jqka.com.cn/' + a+ '/holder/')
	
	print(start_urls)
	
	
	items = []

	def checkGDnumvers(self, response):
		sel = scrapy.selector.Selector(response)
		#'指标日期'
		date_time_divs = sel.xpath('//table[@class="top_thead"]')
		date_time = date_time_divs.xpath('.//div[@class="td_w"]/text()').extract()
		print(date_time)
		
		length = len(date_time)
		
		#股东总人数(万户)
		gudong_numbers_divs = sel.xpath('//table[@class="tbody"]')
		gudong_numbers = gudong_numbers_divs.xpath('.//div[@class="td_w"]/text()').extract()
		print(gudong_numbers)
		
		#较上期变化
		different_last = gudong_numbers_divs.xpath('.//td/span/text()').extract()
		print(different_last[0:length+1])
		
		#人均流通股
		avarge_numbers = gudong_numbers_divs.xpath('.//td/text()').extract()
		print(avarge_numbers[0:length+1])

	#流通股东数据
	def checkLTGD(self, response):
		sel = scrapy.selector.Selector(response)
		LTGD_body = sel.xpath('//div[@id="flowholder"]')
		date_time = LTGD_body.xpath('.//li/a[@class="fdates"]/text()').extract()
		print(date_time)
		
		date_length = len(date_time)
		
		cur_seq = 0
		one_jidu_info_divs = LTGD_body.xpath('.//table[@class="m_table m_hl ggintro"]')
		print("gudong info parts %d" % len(one_jidu_info_divs))
		for one_jidu_info in one_jidu_info_divs:
			one_gudong_info_divs = one_jidu_info.xpath('.//tr')
			print("gudong info member %d" % len(one_gudong_info_divs))
			for one_gudong_info in one_gudong_info_divs:
				name = one_gudong_info.xpath('.//th[@class="tl holder_th"]/a/text()').extract()
				info = one_gudong_info.xpath('.//td/text()').extract()
				print(name)
				print(info)
				#print("list len %d" % len(info))
				if (name and info):
					item = DmozeItem()
					item['name'] = name[0]
					item['number'] = info[0]
					item['percent'] = info[2]
					item['stockType'] = info[-1].strip()
					item['time'] = date_time[cur_seq]
					item['memType'] = '流通股东'
					self.items.append(item)
			
			cur_seq += 1
				
	#十大股东数据
	def checkSDGD(self, response):
		sel = scrapy.selector.Selector(response)
		SDGD_body = sel.xpath('//div[@id="tenholder"]')
		date_time = SDGD_body.xpath('.//li/a[@class="tdates"]/text()').extract()
		print(date_time)
		
		date_length = len(date_time)
		print("date_time length %d", date_length)
		cur_seq = 0
		one_jidu_info_divs = SDGD_body.xpath('.//table[@class="m_table m_hl ggintro"]')
		print("gudong info parts %d" % len(one_jidu_info_divs))
		for one_jidu_info in one_jidu_info_divs:
			one_gudong_info_divs = one_jidu_info.xpath('.//tr')
			print("gudong info member %d" % len(one_gudong_info_divs))
			for one_gudong_info in one_gudong_info_divs:
				name = one_gudong_info.xpath('.//th[@class="tl holder_th"]/a/text()').extract()
				info = one_gudong_info.xpath('.//td/text()').extract()
				#print(name)
				#print(info)
				#print("list len %d" % len(info))
				if (name and info):
					item = DmozeItem()
					item['name'] = name[0]
					item['number'] = info[0]
					item['percent'] = info[2]
					item['stockType'] = info[-1].strip()
					item['time'] = date_time[cur_seq]
					item['memType'] = '十大股东'
					self.items.append(item)
			
			cur_seq += 1
				
	def storeGDinfo(self, response):
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		match = pattern.search(str(response)) 
		if match:
			file_name = match.group()
			print("match file_name %s" % file_name)
			with codecs.open('/home/yy/data_sto/' + file_name, 'wb', 'utf-8') as f:
				f.truncate()
				for i in self.items:
					line = json.dumps(dict(i), ensure_ascii=False) + "\n"
					f.write(line)
				
	def parse(self, response):
		self.items = []
		self.checkGDnumvers(response)
		self.checkLTGD(response)
		self.checkSDGD(response)
		self.storeGDinfo(response)
		
		#return self.items
	

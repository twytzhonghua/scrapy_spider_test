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
	name = "stock_db"
	allowed_domains = ['10jqka.com.cn']
	start_urls = [
		#'http://stockpage.10jqka.com.cn/000935/holder/'
	]
	
	for line in open('sh_list'):
		a = line.strip().lstrip().rstrip('\n')
		start_urls.append('http://stockpage.10jqka.com.cn/' + a + '/holder/')
	for line in open('sz_list'):
		a = line.strip().lstrip().rstrip('\n')
		start_urls.append('http://stockpage.10jqka.com.cn/' + a+ '/holder/')
	#print(start_urls)
	items = []
	stock_num = 0
	def createGDNumberDb(self):
		pass

	#'''SQLite具有以下五种数据类型：
	#1.NULL：空值。
	#2.INTEGER：带符号的整型，具体取决有存入数字的范围大小。
	#3.REAL：浮点数字，存储为8-byte IEEE浮点数。
	#4.TEXT：字符串文本。
	#5.BLOB：二进制对象。'''
	def createGDDataDb(self):
		conn = sqlite3.connect('gdinfo.db')
		c = conn.cursor()
		c.execute('''CREATE TABLE gdinfo
             (stock_number INTEGER, name text, number REAL, percent REAL, stockType text, time text, memType text)''')

	def checkGDnumvers(self, number, response):
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
	def checkLTGD(self, response, c, con):
		sel = scrapy.selector.Selector(response)
		LTGD_body = sel.xpath('//div[@id="flowholder"]')
		date_time = LTGD_body.xpath('.//li/a[@class="fdates"]/text()').extract()
		print(date_time)
		
		date_length = len(date_time)
		
		cur_seq = 0
		one_jidu_info_divs = LTGD_body.xpath('.//table[@class="m_table m_hl ggintro"]')
		
		all_info = []
		for one_jidu_info in one_jidu_info_divs:
			one_gudong_info_divs = one_jidu_info.xpath('.//tr')
			
			for one_gudong_info in one_gudong_info_divs:
				name = one_gudong_info.xpath('.//th[@class="tl holder_th"]/a/text()').extract()
				info = one_gudong_info.xpath('.//td/text()').extract()
				
				if (name and info):
					sname_info = str(name[0])
					spercent = info[0]
					shold_numbers = float(info[2])
					sstockType = info[-1].strip()
					stime = date_time[cur_seq]
					smemType = u'流通股东'
					gudonginfo = (self.stock_num, sname_info, shold_numbers, spercent, sstockType, stime, smemType)
					all_info.append(gudonginfo)
			cur_seq += 1
		
		#print(all_info)
		c.executemany("INSERT INTO gdinfo VALUES (?,?,?,?,?,?,?)", all_info)
		con.commit()
		
	#十大股东数据
	def checkSDGD(self, response, c, con):
		sel = scrapy.selector.Selector(response)
		SDGD_body = sel.xpath('//div[@id="tenholder"]')
		date_time = SDGD_body.xpath('.//li/a[@class="tdates"]/text()').extract()
		print(date_time)
		
		date_length = len(date_time)
		
		cur_seq = 0
		one_jidu_info_divs = SDGD_body.xpath('.//table[@class="m_table m_hl ggintro"]')
		
		all_info = []
		for one_jidu_info in one_jidu_info_divs:
			one_gudong_info_divs = one_jidu_info.xpath('.//tr')
			for one_gudong_info in one_gudong_info_divs:
				name = one_gudong_info.xpath('.//th[@class="tl holder_th"]/a/text()').extract()
				info = one_gudong_info.xpath('.//td/text()').extract()
				if (name and info):
					sname_info = str(name[0])
					spercent = info[0]
					shold_numbers = float(info[2])
					sstockType = info[-1].strip()
					stime = date_time[cur_seq]
					smemType = '十大股东'
					gudonginfo = (self.stock_num, sname_info, shold_numbers, spercent, sstockType, stime, smemType)
					all_info.append(gudonginfo)
			cur_seq += 1
		
		#print(all_info)
		c.executemany("INSERT INTO gdinfo VALUES (?,?,?,?,?,?,?)", all_info)
		con.commit()

		
	def storeGDinfo(self, response):
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		match = pattern.search(str(response)) 
		if match:
			file_name = match.group()
			print("match file_name %s" % file_name)
			file_name = 'C:/data_sto/' + file_name + '.json'
			with codecs.open(file_name, 'w', 'utf-8') as f:
				f.truncate()
				for i in self.items:
					line = json.dumps(dict(i), ensure_ascii=False) + "\n"
					f.write(line)
				
	def parse(self, response):
		self.items = []
		conn = sqlite3.connect('allgdinfo.db')
		c = conn.cursor()
		if os.path.getsize('allgdinfo.db'):
			pass
		else:
			c.execute('''CREATE TABLE gdinfo (stock_num text, name text, number text, percent text, stockType text, time text, memType text)''')
		
		conn.commit()
		#conn.close()
				 
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		match = pattern.search(str(response)) 
		if match:
			self.stock_num = match.group()
			print("stock_num %s" % str(self.stock_num))
			#self.checkGDnumvers(response)
			self.checkLTGD(response, c, conn)
			self.checkSDGD(response, c, conn)
			#self.storeGDinfo(response)
			conn.close()
		
		#return self.items
	

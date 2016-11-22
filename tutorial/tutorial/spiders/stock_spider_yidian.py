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
import MySQLdb



class StockSpider(scrapy.Spider):
	name = "stock_yidian"
	allowed_domains = ['yidiancangwei.com']
	start_urls = [
		#'http://www.yidiancangwei.com/gudong/sdlt_300111_2015_06_30.html'
	]
	reload(sys)
	sys.setdefaultencoding("utf-8")
	
	db=MySQLdb.connect(host='localhost',user='root',passwd='123',port=3306, charset="utf8")
	cur = db.cursor()  
	cur.execute('create database if not exists yidian_gudonginfo')
	db.select_db('yidian_gudonginfo')
	
	db.set_character_set('utf8')
	cur.execute('SET NAMES utf8;') 
	cur.execute('SET CHARACTER SET utf8;')
	cur.execute('SET character_set_connection=utf8;')
	
	cur.execute('create table if not exists gudonginfo (gudong_name varchar(40), date varchar(20), stock_name varchar(20), percent varchar(20), hold_num varchar(20), increase varchar(20), stock_type varchar(20))ENGINE=InnoDB DEFAULT CHARSET=utf8')
	
	tablerows=cur.fetchall()
	
	for line in open('sh_list'):
		a = line.strip().lstrip().rstrip('\n')
		for iline in open('data_date.list'):
			date_line = iline.strip().lstrip().rstrip('\n')
			start_urls.append('http://www.yidiancangwei.com/gudong/sdlt_'+ a + '_' + date_line + '.html')
		
	for line in open('sz_list'):
		a = line.strip().lstrip().rstrip('\n')
		for iline in open('data_date.list'):
			date_line = iline.strip().lstrip().rstrip('\n')
			start_urls.append('http://www.yidiancangwei.com/gudong/sdlt_'+ a + '_' + date_line + '.html')
	
	#print(start_urls) 
	#流通股东数据
	def checkLTGD(self, response):
		sel = scrapy.selector.Selector(response)
		self.stock_name = sel.xpath('//div[@class="Title shareTit"]/span[@class="blue"]/text()').extract()
		
		#print(self.stock_name)
		
		LTGD_body = sel.xpath('//div[@class="TabBox"]')
		one_jidu_info_divs = LTGD_body.xpath('.//tr')
		all_info = []
		for one_gudong_info in one_jidu_info_divs:
			LTGD_name = one_gudong_info.xpath('.//a/text()').extract()
			other_info = one_gudong_info.xpath('.//td/text()').extract()
			#print(LTGD_name[0].strip())
			#print('name len %d' % len(LTGD_name))
			#print(other_info )
			#print('other info len %d' % len(other_info))
			if not other_info or not LTGD_name:
				#print("name or other info null")
				pass
			else:              
				gdname = LTGD_name[0].strip()
				date = other_info[-1].strip()
				stock_name = self.stock_name
				percent = other_info[2].strip()  
				hold_num = other_info[3].strip()  
				increase = other_info[4].strip()  
				stock_type = other_info[5].strip()
				#print(gdname)				
				#print(percent)
				#print(hold_numbers)
				#print(increase)
				#print(stock_type)
				#print(update_time)
				#print(other_info)
				gdinfo = (gdname, date, stock_name, percent, hold_num, increase, stock_type)
				all_info.append(gdinfo)
		#print(all_info) (%s,%s,%s,%s,%s,%s,%s)
		self.cur.executemany("insert into gudonginfo values (%s,%s,%s,%s,%s,%s,%s)", all_info)
		self.db.commit()
	
	def parse(self, response):
		
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		match = pattern.search(str(response)) 
		if match:
			self.stock_num = match.group()
			#print("stock_num %s" % str(self.stock_num))
			self.checkLTGD(response)

		
		#return self.items
	

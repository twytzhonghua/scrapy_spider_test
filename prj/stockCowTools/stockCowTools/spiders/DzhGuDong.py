# -*- coding: utf-8 -*-
import scrapy
import re
import sys
import urllib.request
from stockCowTools.spiders.stockSql import *
from stockCowTools.spiders.dataHtmlParse import *

class DzhgudongSpider(scrapy.Spider):
	name = "dzh"
	allowed_domains = ['webf10.gw.com.cn']
	start_urls = [
		'http://webf10.gw.com.cn/SH/B10/SH600767_B10.html#'
	]

	#with open('C:/scrapy/ths_urls.txt', 'r') as f:
	#	for line in f.readlines():
	#		start_urls.append(line.strip())
		
	#print(start_urls)

	#流通股东数据
	def checkLTGD(self, response):
		sel = scrapy.selector.Selector(response)
		# <section class="sdgdBox dzh_index" id="十大流通股东">
		LTGD_body = sel.xpath('//section[@id="十大流通股东"]')
		h2 = LTGD_body.xpath('.//h2/text()').extract()
		print('h2 = ', h2)
		#date_time = LTGD_body.xpath('.//li/a[@class="fdates"]/text()').extract()
		#print(date_time)
		#all_info = []
		#date_length = len(date_time)
		
		cur_seq = 0
		one_jidu_info_divs = LTGD_body.xpath('.//div[@class="sdgdCon  sdltgdTb"]')
		print("gudong info parts %d" % len(one_jidu_info_divs))
		for one_jidu_info in one_jidu_info_divs:
			#<table class="f10tabel sdgd_table">
			one_gudong_info_divs = one_jidu_info.xpath('.//table[@class="f10tabel sdgd_table"]')
			#print("gudong info member %d" % len(one_gudong_info_divs))
			#for one_gudong_info in one_gudong_info_divs:
			name = one_gudong_info_divs.xpath('.//td/a/text()').extract()
			info = one_gudong_info_divs.xpath('.//td/text()').extract()
			print('---------------------------------------------------------')
			name_len = len(name) + 1
			#print('name length = ', len(name))
			#print('name  = ', name)
			#print('info = ', info)
			#print('name = %s info = %s' %   (name, info))
			#print("list len %d" % len(info))
			if (name and info):
				for i in range(1,name_len):
					print('cur = ', i)
					"""
					'1.', '5350.83', '未变', '15.70', '流通A股',
					"""
					gdname = name[i-1]
					hold_num = info[5*(i-1) + 1]
					change = info[5*(i-1) + 2]
					percent = info[5*(i-1) + 3]
					stock_type = info[5*(i-1) + 4]
					#date = date_time[cur_seq]
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
				#gdinfo = (stock_number, stock_name,  gdname,  hold_num,  percent, date,  stock_type)
					gdinfo = (stock_number, stock_name,  gdname,  hold_num,  percent, change, stock_type)
					print('gdinfo = ', gdinfo)
				#all_info.append(gdinfo)
		
		
		#store_lt_gudong_db(all_info)
	
	def checkCName(self):
		#sel = scrapy.selector.Selector(response)
		#<div class="nav"><table width="99%"><tbody><tr><td width="11%"><div class="nav_div"><a href="#">运盛医疗</a></div></td><td width="11%"><div class="nav_div" id="blockid_1"><a href="../../SH/B1/SH600767_B1.html">操盘必读</a><img src="../../images/NEW.png"></div></td><td width="11%"><div class="nav_div" id="blockid_2"><a href="../../SH/B2/SH600767_B2.html">财务透视</a></div></td><td width="11%"><div class="nav_div" id="blockid_3"><a href="../../SH/B3/SH600767_B3.html">主营构成</a></div></td><td width="11%"><div class="nav_div" id="blockid_4"><a href="../../SH/B4/SH600767_B4.html">行业新闻</a></div></td><td width="11%"><div class="nav_div" id="blockid_5"><a href="../../SH/B5/SH600767_B5.html">大事提醒</a></div></td><td width="11%"><div class="nav_div" id="blockid_6"><a href="../../SH/B6/SH600767_B6.html">八面来风</a></div></td><td width="11%"><div class="nav_div" id="blockid_7"><a href="../../SH/B7/SH600767_B7.html">公司概况</a></div></td><td width="11%"><div class="nav_div" id="blockid_8"><a href="../../SH/B8/SH600767_B8.html">管 理 层</a></div></td></tr><tr><td width="11%"><div class="nav_div stockName"><span class="stockcode">600767</span></div></td><td width="11%"><div class="nav_div" id="blockid_9"><a href="../../SH/B9/SH600767_B9.html">最新季报</a></div></td><td width="11%"><div class="nav_div" id="blockid_10"><a class="active" href="../../SH/B10/SH600767_B10.html">股东研究</a></div></td><td width="11%"><div class="nav_div" id="blockid_11"><a href="../../SH/B11/SH600767_B11.html">股本分红</a></div></td><td width="11%"><div class="nav_div" id="blockid_12"><a href="../../SH/B12/SH600767_B12.html">资本运作</a></div></td><td width="11%"><div class="nav_div" id="blockid_13"><a href="../../SH/B13/SH600767_B13.html">关联个股</a><img src="../../images/NEW.png"></div></td><td width="11%"><div class="nav_div" id="blockid_14"><a href="../../SH/B14/SH600767_B14.html">公司公告</a></div></td><td width="11%"><div class="nav_div" id="blockid_15"><a href="../../SH/B15/SH600767_B15.html">经营动态</a></div></td><td width="11%"><div class="nav_div" id="blockid_16"><a href="../../SH/B16/SH600767_B16.html">盈利预测</a><img src="../../images/NEW.png"></div></td></tr></tbody></table><div class="close_btn"><div class="close_btn_inner">
		#	<a href="javascript:void(0);" onclick="javascript:closePage('null');return false;"></a></div></div></div>
		#div class="nav_div" href="#"
		#h = sel.xpath('//div[@class="wrapper"]')
		#a = sel.xpath('//a[@href="#"]/text()').extract()
		#print('h = ', h)
		#print('a = ', a)
		#for i in a:
			#self.cName = a.xpath('.//a/[@href="#"]/text()').extract()
			#print('cName = ', self.cName)
			
		num = int(self.stock_num)
		if(num >= 6000):
			hq_url = 'http://hq.sinajs.cn/list=s_sh' + self.stock_num
		else:
			hq_url = 'http://hq.sinajs.cn/list=s_sz' + self.stock_num
		
		page = urllib.request.urlopen(hq_url)
		html = page.read()
		html = html.decode("utf8")
		print(html)
		print('html type = ', type(html))
		content = str(html, encoding = "utf-8")   
		print('content type = ', type(content))
		#content = str.encode(html)
		#print(content)
		#str.encode(html)
		#list = html.split(',')
		#print(list)
	
	def parse(self, response):
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		match = pattern.search(str(response)) 
		if match:
			self.stock_num = match.group()
			print("stock_num =", str(self.stock_num))
			self.checkCName()
			#self.checkLTGD(response)
			
	

		



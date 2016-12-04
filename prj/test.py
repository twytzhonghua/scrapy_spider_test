# -*- coding:utf8 -*-
import urllib2
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import sys

def checkLTGD(response):
	stock_name = response.xpath('//div[@class="Title shareTit"]/span[@class="blue"]/text()').extract()
		
	#print(self.stock_name)
		
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
			stock_name = stock_name
			percent = other_info[2].strip()  
			hold_num = other_info[3].strip()  
			increase = other_info[4].strip()  
			stock_type = other_info[5].strip()
			print(gdname)				
			print(percent)
			print(hold_num)
			print(increase)
			print(stock_type)
			#print(update_time)
			#print(other_info)
			gdinfo = (gdname, date, stock_name, percent, hold_num, increase, stock_type)
			all_info.append(gdinfo)

def get_html(url):
	response = urllib2.urlopen(url)
	return response.read()
	
reload(sys)
sys.setdefaultencoding( "utf-8" )	
url  =  "http://www.yidiancangwei.com/gudong/sdlt_300111_2015_06_30.html";
html = get_html(url)
response = Selector(text=html)

checkLTGD(response)


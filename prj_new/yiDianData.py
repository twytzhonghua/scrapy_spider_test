# -*- coding:utf-8 -*- 
import urllib.request
from scrapy.http import Request
from scrapy.selector import Selector
#from scrapy.http import HtmlResponse
#import sys
#from lxml import etree

from twisted.internet import reactor
from twisted.web import client
 
def get_html_response_url_requset(content):
	html = content
	response =  Selector(text=html)
	checkLTGD(response)



def start_yidian_url_requset(url):
	burl = bytes(url,encoding="utf-8") 
	deferred = client.getPage(burl)
	deferred.addCallback(get_html_response_url_requset)   
	reactor.run()
	


def new_get_html(url):
	headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
	urllib.request.Request(headers)
	f =  urllib.request.urlopen(url, timeout=20)
	html = f.read().decode('utf-8')
	response =  Selector(text=html)
	return response
	

def generateYiDianALLDataUrls(stock_number_list):
	urls = []
	with open('D:/python/scrapy_spider_test/prj_new/date_cfg.cfg', 'r') as f:
		dates = f.readlines()
		print(dates)
	
	for date in dates:
		for number in stock_number_list:
			a_date = date.strip()
			new_url = 'http://www.yidiancangwei.com/gudong/sdlt_' + number + '_' + a_date + '.html'
			new_url = str(new_url)
			urls.append(new_url)
			
	#print(urls)
	#with open('yidian_urls.txt', 'wb') as f:
	#	for url in urls:
	#		f.write(url)
	#		f.write('\n')
	return urls


def checkLTGD(response):
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
			
			
def getYiDianAllLTGD(stocks):
	urls = generateYiDianALLDataUrls(stocks)
	for url in urls:
		response = get_html_response(url)
		checkLTGD(response)
	#return urls
		
		
		
			


#coding=utf-8

import urllib.request
from scrapy.http import Request
from scrapy.selector import Selector
import requests

def get_urls():
	url = []
	with open ('number.cfg', 'r') as f:
		for line in f.readlines():
			temp = 'http://stockpage.10jqka.com.cn/' + line.strip()
			url.append(temp)
	
	return url
			
def get_ret_from_url(url):
	f =  urllib.request.urlopen(url, timeout=20)
	#html = f.read().decode('utf-8')
	html = f.read()
	response =  Selector(text=html)
	head = response.xpath('//div[@class="minute_price clearfix"]')
	print(head)
	info = head.xpath('.//span/text()').extract()
	print(info)

	#name = response.xpath('//title/text()').extract()
	#curPrice = response.xpath('//span[@id="hexm_curPrice"]/text').extract()
	#print(curPrice)
	#print(name)

def request_get_url(url):
	r = requests.get(url)
	print(r.text)
	
	
	
if __name__ == "__main__":
	for url in get_urls():
		#get_ret_from_url(url)
		request_get_url(url)
	
			
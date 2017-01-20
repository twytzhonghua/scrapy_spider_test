# -*- coding: utf-8 -*-
# encoding=utf-8
import scrapy
import re
import urllib
import sys
from lxml import etree
import codecs
import os
import math


#import urllib.request 
#import urllib.error

class ExampleSpider(scrapy.Spider):
	name = "example"
	allowed_domains = ["www.99ww9.com"]
	start_urls = [ ]
	a1=50000
	b1=55000
	for i in range(a1, b1):
		start_urls.append('http://www.99ww9.com/embed/' + str(i))
	#print(start_urls)

	def parse(self, response):
		#reload(sys)
		#sys.setdefaultencoding('utf8')
		
		
		
		name1 = ((response.xpath('//title/text()').extract())[0].split(' '))[0] + '.mp4'
		r1 = re.compile('http:\/\/www\.\S{0,100}\.mp4')
		
	
		#number = response
		
		url1 = r1.findall(response.body.decode('utf-8'))[0]
		#print(url1)
		
		number = url1.replace('/', ' ').split(' ')[-2]
		#print('number = %s' % number)
		
		ret_str  = number + ' ' + name1
		with open ('ret.txt', 'ab') as f:
			#f.truncate()
			#urllib.request.urlretrieve(url1, name1)
			#f.seek(0,2)
			f.write(ret_str.encode('utf-8'))
			f.write('\n'.encode('utf-8'))
		with open('url.txt', 'ab') as f:
			#f.seek(0,2)
			f.write(url1.encode('utf-8'))
			f.write('\n'.encode('utf-8'))
		

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
	a1=40000
	b1=45000
	for i in range(a1, b1):
		start_urls.append('http://www.99ww9.com/embed/' + str(i))
	#print(start_urls)

	def parse(self, response):
		#reload(sys)
		#sys.setdefaultencoding('utf8')
		
		name1 = ((response.xpath('//title/text()').extract())[0].split(' '))[0] + '.mp4'
		r1 = re.compile('http:\/\/www\.\S{0,100}\.mp4')
		
		url1 = r1.findall(response.body.decode('utf-8'))[0]
		print(url1)
		with open (name1, 'w') as f:
			f.truncate()
			urllib.urlretrieve(url1, name1)
		

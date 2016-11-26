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




class ExampleSpider(scrapy.Spider):
	name = "example"
	allowed_domains = ["www.99ww9.com"]
	start_urls = [ ]
	a1=42000
	b1=45000
	for i in range(a1, b1):
		start_urls.append('http://www.99ww9.com/embed/' + str(i))
	print(start_urls)

	def parse(self, response):
		reload(sys)
		sys.setdefaultencoding('utf8')
		name1 = ((response.xpath('//title/text()').extract())[0].split(' '))[0] + '.mp4'
		url1 = re.findall('http:\/\/www\.99ww9\.com\/\S{5,100}\.mp4', response.body)[0]
		print(name1)
		print(url1)
		f = open (name1, 'w')
		f.truncate()
		urllib.urlretrieve(url1, name1)
		

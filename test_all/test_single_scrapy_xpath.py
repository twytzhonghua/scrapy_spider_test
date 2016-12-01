# -*- coding:utf8 -*-
import urllib2
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


def get_html(url):
	response = urllib2.urlopen(url)
	return response.read()
	
url  =  "http://www.baidu.com"	
html = get_html(url)

response = Selector(text=html)
title = response.xpath('//title/text()').extract()

print(title)



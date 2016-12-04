# -*- coding:utf8 -*-
import urllib2
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import sys
#sys.path.append("spider")

from  SpiderYiDian import *


def get_html(url):
	response = urllib2.urlopen(url)
	return response.read()
	
url  =  "http://www.yidiancangwei.com/gudong/sdlt_300111_2015_06_30.html"	
html = get_html(url)

response = Selector(text=html)
title = response.xpath('//title/text()').extract()

print(title)
checkLTGD(response)




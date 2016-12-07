# -*- coding:utf8 -*-
import urllib2
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import sys
import yiDianData
import UpdateStockNumbers




def get_yidian_htmls():
	htmls = []
	
	

reload(sys)
sys.setdefaultencoding( "utf-8" )	

stocks = UpdateStockNumbers.update_all_stock_number()
#print(stocks)



#url  =  "http://www.yidiancangwei.com/gudong/sdlt_300111_2015_06_30.html";

#res = get_html_response(url)


yiDianData.getYiDianAllLTGD(stocks)




#coding=utf-8
# -*- coding:utf-8 -*- 
from lxml import etree
import urllib2
import urllib
import re
import sys
#import requests
import xlrd
import importlib


class UpdateStockNumber():
	def __init__(self, name):
		self.name = name
		self.all_stock = []
		 
	def getHtml(self, url):
		page = urllib2.urlopen(url)
		html = page.read()
		return html

	def find_stock_num(self, url, file_name):
		html = self.getHtml(url)
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}')
		#matchs = pattern.search(html)
		matchs = pattern.findall( html)
		#print(matchs)
		with open(file_name, 'wb') as f:
			f.truncate()
			for i in range(0, len(matchs) -1):
				self.all_stock.append(matchs[i])
				f.write(matchs[i].encode('utf-8'))
				f.write('\n'.encode('utf-8'))
	
			
	def  update_sz_stock_numbers(self):
		url1 = "http://www.sse.com.cn/js/common/ssesuggestdata.js"
		self.find_stock_num(url1, 'sh_list')
				
		
	def download_sz_stock_number(self):
		#res = requests.get('http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1110&tab2PAGENUM=1&ENCODE=1&TABKEY=tab2')
		#res.raise_for_status()
		urllib.urlretrieve('http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1110&tab2PAGENUM=1&ENCODE=1&TABKEY=tab2', 'RomeoAndJuliet.xls')
		#playFile = open('RomeoAndJuliet.xls', 'wb')
		#for chunk in res.iter_content(100000):
		#	playFile.write(chunk)
		#playFile.close()
		
		data = xlrd.open_workbook('RomeoAndJuliet.xls')
		table = data.sheet_by_index(0)
		col_value = table.col_values(0)
		#print(col_value)
		#lenth = IntVar()
		sz_items=[]
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		for i in range(0, len(col_value)): 		
			match = pattern.search(col_value[i]) 
			if match:
				#print match.group()
				self.all_stock.append(match.group())
				sz_items.append(match.group())

		with open('sz_list', 'wb') as f:
			f.truncate()
			for item in sz_items:
				f.write(item.encode('utf-8'))
				f.write('\n'.encode('utf-8'))
	
	def get_all_stock_number(self):
		self.update_sz_stock_numbers()
		self.download_sz_stock_number()
		return self.all_stock
				
def update_all_stock_number():
	update = UpdateStockNumber('update stock')
	return update.get_all_stock_number()
	
	



#coding=utf-8
# -*- coding:utf-8 -*- 
from lxml import etree
import urllib
import re
import sys
#import requests
import xlrd
import importlib


class UpdateStockNumber:
	def __init__(self, name):
		self.name = name
		
	def getHtml(self, url):
		page = urllib.request.urlopen(url)
		html = page.read()
		return html

	def find_stock_num(self, url, file_name):
		#importlib.reload(sys)
		#sys.setdefaultencoding('utf-8')
		html = self.getHtml(url)
		
		with open(file_name + '.html', 'wb') as f:
			f.write(html)
		items = []
		real_items=[]
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		for line in open( file_name + '.html', encoding= 'utf-8'): 		
			match = pattern.search(line) 
			if match:
				print(match.group())
				real_items.append(match.group())

		with open(file_name, 'wb') as f:
			f.truncate()
			for item in real_items:
				f.write(item.encode('utf-8'))
				f.write('\n'.encode('utf-8'))
			
	def  update_stock_numbers(self):
		url1 = "http://www.sse.com.cn/js/common/ssesuggestdata.js"
		#url2 = "http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1110&tab2PAGENUM=1&ENCODE=1&TABKEY=tab2"
		self.find_stock_num(url1, 'sh_list')
		#self.find_stock_num(url2, 'sz_list')
		#self.find_stock_num(url0, 'all_list')
		
		
	def download_sz_stock_number(self):
		#res = requests.get('http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1110&tab2PAGENUM=1&ENCODE=1&TABKEY=tab2')
		#res.raise_for_status()
		#playFile = open('RomeoAndJuliet.xls', 'wb')
		#for chunk in res.iter_content(100000):
		#	playFile.write(chunk)
		#playFile.close()
		
		data = xlrd.open_workbook('RomeoAndJuliet.xls')
		table = data.sheet_by_index(0)
		col_value = table.col_values(0)
		print(col_value)
		#lenth = IntVar()
		sz_items=[]
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		for i in range(0, len(col_value)): 		
			match = pattern.search(col_value[i]) 
			if match:
				#print match.group()
				sz_items.append(match.group())

		with open('sz_list', 'wb') as f:
			f.truncate()
			for item in sz_items:
				f.write(item.encode('utf-8'))
				f.write('\n'.encode('utf-8'))

#updatestock =  UpdateStockNumber('testupdate')
#updatestock.update_stock_numbers()
#updatestock.download_sz_stock_number()

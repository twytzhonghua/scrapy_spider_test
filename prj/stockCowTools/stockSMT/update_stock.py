# -*- coding:utf-8 -*- 
from lxml import etree
import urllib.request
import re
import sys
import xlrd
import csv
import tushare as ts


class UpdateStockNumber():
	def __init__(self, name):
		self.name = name
		self.all_stock = []
		 
	def getHtml(self, url):
		page = urllib.request.urlopen(url)
		html = page.read()
		return html

	def find_stock_num(self, url, file_name):
		html = self.getHtml(url)
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}')
		#matchs = pattern.search(html)
		matchs = pattern.findall(str(html))
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
		urllib.request.urlretrieve('http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1110&tab2PAGENUM=1&ENCODE=1&TABKEY=tab2', 'RomeoAndJuliet.xls')
		
		data = xlrd.open_workbook('RomeoAndJuliet.xls')
		table = data.sheet_by_index(0)
		col_value = table.col_values(0)
		sz_items=[]
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		for i in range(0, len(col_value)): 		
			match = pattern.search(col_value[i]) 
			if match:
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
	
	

def generateYiDianGDUrls(stock_number_list):
	urls = []
	with open('date_cfg.cfg', 'r') as f:
		dates = f.readlines()
		print(dates)
	
	for date in dates:
		for number in stock_number_list:
			a_date = date.strip()
			new_url = 'http://www.yidiancangwei.com/gudong/sdlt_' + number + '_' + a_date + '.html'
			new_url = str(new_url)
			urls.append(new_url)
			
	#print(urls)
	with open('C:/scrapy/yidian_urls.txt', 'wb') as f:
		for url in urls:
			f.write(url.encode('utf-8'))
			f.write('\n'.encode('utf-8'))
	return urls
	



def get_and_store_all_stock_list():
    a = ts.get_stock_basics()
    a.to_csv('c:/scrapy/all_stock.csv', encoding='gbk', index=True)
    print('generate c:/scrapy/all_stock.csv over')


def generate_stock_dic():
    i = 0
    stock_dic = {}
    csv_reader = csv.reader(open('c:/scrapy/all_stock.csv', encoding='gbk'))
    for row in csv_reader:
        if(i == 0) :
            pass
        else:
            if(len(row[0]) == 1):
                row[0] = '00000' + row[0]
            elif (len(row[0]) == 2):
                row[0] = '0000' + row[0]
            elif (len(row[0]) == 3):
                row[0] = '000' + row[0]
            elif (len(row[0]) == 4):
                row[0] = '00' + row[0]
            elif (len(row[0]) == 5):
                row[0] = '0' + row[0]
            else:
                pass
            
        stock_dic[row[0]] = row[1] 

        i += 1
	
    # sorted(stock_dic.keys)
    
    return stock_dic


# 'http://webf10.gw.com.cn/SH/B10/SH600767_B10.html#'
def generateDzhUrls():
	urls = []
	print('begin generateDzhUrls')
	dict = generate_stock_dic()
	for key in dict.keys():
		if key.isdigit():
			if int(key) < 600000 :
				urls.append('http://webf10.gw.com.cn/SZ/B10/SZ' + key+ '_B10.html')
			else:
				urls.append('http://webf10.gw.com.cn/SH/B10/SH' + key + '_B10.html')
			
	#print(urls)
	with open('C:/scrapy/crawls_urls.txt', 'wb') as f:
		for url in urls:
			f.write(url.encode('utf-8'))
			f.write('\n'.encode('utf-8'))
			
def generateThsUrls():
	urls = []
	
	dict = generate_stock_dic()			
	for key in dict.keys():
		urls.append('http://stockpage.10jqka.com.cn/' + key+ '/holder/')

	#print(urls)
	with open('C:/scrapy/crawls_urls.txt', 'wb') as f:
		for url in urls:
			f.write(url.encode('utf-8'))
			f.write('\n'.encode('utf-8'))

# 新浪网站
def generateXlUrls():
	urls = []
	
	dict = generate_stock_dic()			
	for key in dict.keys():
	# http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/603009.phtml#2010-09-30
		urls.append('http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/' + key+ '.phtml#2010-09-30')

	#print(urls)
	with open('C:/scrapy/crawls_urls.txt', 'wb') as f:
		for url in urls:
			f.write(url.encode('utf-8'))
			f.write('\n'.encode('utf-8'))			
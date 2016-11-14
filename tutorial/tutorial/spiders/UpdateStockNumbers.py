from lxml import etree
import urllib
import re
import sys

class UpdateStockNumber:
	def __init__(self, name):
		self.name = name
		
	def getHtml(self, url):
		page = urllib.urlopen(url)
		html = page.read()
		return html

	def find_stock_num(self, url, file_name):
		reload(sys)
		sys.setdefaultencoding('utf-8')
		html = self.getHtml(url)
		
		with open(file_name + '.html', 'wb') as f:
			f.write(html)
		items = []
		real_items=[]
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		for line in open(file_name + '.html'): 		
			match = pattern.search(line) 
			if match:
				print match.group()
				real_items.append(match.group())

		with open(file_name, 'wb') as f:
			f.truncate()
			for item in real_items:
					f.write(item)
					f.write('\n')
			
	def  update_stock_numbers(self):
		url1 = "http://www.caiguu.com/shichang/jujiao/91582_2.html"
		url2 = "http://www.caiguu.com/shichang/jujiao/91582_3.html"
		self.find_stock_num(url1, 'sh_list')
		self.find_stock_num(url2, 'sz_list')
		
updatestock =  UpdateStockNumber('testupdate')
updatestock.update_stock_numbers()

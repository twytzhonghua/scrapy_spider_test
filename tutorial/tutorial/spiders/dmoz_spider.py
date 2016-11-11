import scrapy

from tutorial.items import DmozeItem

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ['10jqka.com.cn']
	start_urls = [
		'http://stockpage.10jqka.com.cn/000932/holder/',
	]

	def parse(self, response):
		
		sel = scrapy.selector.Selector(response)
		#sites = sel.xpath('//tr/th[@class="tl holder_th"]/a/text()')
		#nfo1 = sel.xpath('//tbody/tr/td/text()').extract()
		items = []
		#for site in sites:
		
		dates = sel.xpath('//li/a[@class="fdates"]/text()').extract()
		print  'date len%d', len(dates)
		print dates
		
		handle_nr = 0
		cur_nr = 0
		for res in response.xpath('//tbody/tr'):
			title = res.xpath('th[@class="tl holder_th"]/a/text()').extract()
			info = res.xpath('td/text()').extract()
			
			#print 'date_nr = %d' , handle_nr
			if not title:
				a = 0
				pass
			else:
				#print 'begin dump title info len %d', len(title)
				a = len(title)
				#print title
			
			if not info:
				b = 0
				pass 
			else:
				#print 'begin dump name info len %d', len(info)
				#print info
				b = len(info)
			
			
			print('add info to items cur_nr %d handle_nr%d', cur_nr, handle_nr)
			
			
			if  ( (a ==  1 ) and (b >= 6 )  ):
				if( cur_nr == 10):
					cur_nr = 0
					handle_nr += 1
				#print('add info to items cur_nr %d handle_nr%d', cur_nr, handle_nr)
				item = DmozeItem()
				item['name'] = title
				item['number'] = info[0]
				item['percent'] = info[2]
				item['types'] = info[-1]
				item['nr'] = cur_nr
				if(  ( handle_nr < len(dates) ) ):
					item['time'] = dates[handle_nr]
				items.append(item)
			
				cur_nr += 1
			else: 
				pass
			
		
		return items
	

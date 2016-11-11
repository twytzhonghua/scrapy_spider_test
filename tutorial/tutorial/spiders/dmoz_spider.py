import scrapy

from tutorial.items import DmozeItem

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ['10jqka.com.cn']
	start_urls = [
		'http://stockpage.10jqka.com.cn/000935/holder/',
	]

	def parse(self, response):
		
		#sel = scrapy.selector.Selector(response)
		#sites = sel.xpath('//tr/th[@class="tl holder_th"]/a/text()')
		#nfo1 = sel.xpath('//tbody/tr/td/text()').extract()
		items = []
		#for site in sites:
		for res in response.xpath('//tbody/tr'):
			title = res.xpath('th[@class="tl holder_th"]/a/text()').extract()
			namea = res.xpath('td/text()').extract()
			
			if not title:
				a = 0
				pass
			else:
				print 'begin dump title info len %d', len(title)
				a = len(title)
				print title
			
			if not namea:
				b = 0
				pass 
			else:
				print 'begin dump name info len %d', len(namea)
				print namea
				b = len(namea)
				
			if  ( (a ==  1 ) and (b >= 6 ) ):
				item = DmozeItem()
				item['title1'] = title
				item['info'] = namea
				items.append(item)
				print('add info to items')
			else: 
				pass
		
		return items
	

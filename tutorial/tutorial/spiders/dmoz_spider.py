import scrapy

from tutorial.items import DmozeItem

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ['10jqka.com.cn']
	start_urls = [
		'http://stockpage.10jqka.com.cn/000935/holder/',
	]

	def parse(self, response):
		file_name = response.url.split("/")[-3]
		sel = scrapy.selector.Selector(response)
		sites = sel.xpath('//tr/th[@class="tl holder_th"]/a/text()')
		items = []
		#for site in sites:
		item = DmozeItem()
		item['title'] = sites.extract()
		#open(file_name, 'wb').write(title)
		items.append(item)
			#print(title)
			
		return items
	

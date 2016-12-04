# -*- coding:utf8 -*-


#class SpiderYiDianData(object):

def checkLTGD(self, response):
	sel = scrapy.selector.Selector(response)
	self.stock_name = sel.xpath('//div[@class="Title shareTit"]/span[@class="blue"]/text()').extract()
		
	#print(self.stock_name)
		
	LTGD_body = sel.xpath('//div[@class="TabBox"]')
	one_jidu_info_divs = LTGD_body.xpath('.//tr')
	all_info = []
	for one_gudong_info in one_jidu_info_divs:
		LTGD_name = one_gudong_info.xpath('.//a/text()').extract()
		other_info = one_gudong_info.xpath('.//td/text()').extract()
			#print(LTGD_name[0].strip())
			#print('name len %d' % len(LTGD_name))
			#print(other_info )
			#print('other info len %d' % len(other_info))
		if not other_info or not LTGD_name:
				#print("name or other info null")
			pass
		else:              
			gdname = LTGD_name[0].strip()
			date = other_info[-1].strip()
			stock_name = self.stock_name
			percent = other_info[2].strip()  
			hold_num = other_info[3].strip()  
			increase = other_info[4].strip()  
			stock_type = other_info[5].strip()
			print(gdname)				
			print(percent)
			print(hold_numbers)
			print(increase)
			print(stock_type)
			print(update_time)
			print(other_info)
			gdinfo = (gdname, date, stock_name, percent, hold_num, increase, stock_type)
			all_info.append(gdinfo)
		#print(all_info) (%s,%s,%s,%s,%s,%s,%s)
		#self.cur.executemany("insert into gudonginfo values (%s,%s,%s,%s,%s,%s,%s)", all_info)
		#self.db.commit()
	
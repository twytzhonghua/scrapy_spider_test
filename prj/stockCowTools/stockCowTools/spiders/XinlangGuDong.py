# -*- coding: utf-8 -*-
import scrapy
import re
import sys
import os
import stockSMT.stockSql as stockSql
import stockSMT.update_stock as update_stock
import stockSMT.globalPars as globalPars

class XlgudongSpider(scrapy.Spider):
	name = "xl"
	allowed_domains = ['finance.sina.com.cn']
	start_urls = [
		# 'http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/600079.phtml#2010-09-30'
		# 'http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/300521.phtml#2010-09-30'
	]
	
	self_dict = update_stock.generate_stock_dic()
	print("dic len = ", len(self_dict))
	
	with open(globalPars.getToolBaseWorkDirectory() + 'xl_urls.txt', 'r') as f:
		for line in f.readlines():
			start_urls.append(line.strip())
			
	def checkLTNumber(self, response):
		pass
	
	def reCalcGDData(self, times, all_info):
		for j in range(times):
			jidu_new_div = all_info[j]
			if (j+1) == times:
				return
			jidu_old_div = all_info[j+1]
			# 从一个季度里拿出每个股东数据和上衣季度对比
			for i in range(len(jidu_new_div)):
				find = 0
				new_gd_info = jidu_new_div[i]
				# 当前股东信息和上一个季度每个股东对比
				new_val = int(new_gd_info[3]) / 10000.0
				for k in range(len(jidu_old_div)):
					old_gd_info = jidu_old_div[k]
					# 如果股东在上个季度存在， 则计算差值
					find = 0
					old_val = int(old_gd_info[3]) / 10000.0
					if new_gd_info[2] == old_gd_info[2] :
						find = 1
						if new_gd_info[3] == old_gd_info[3]:
							new_gd_info[-3] = u'不变'
						else:
							val = '%.2f' % (new_val - old_val)
							new_gd_info[-3] = str(val)
							# new_gd_info[3]	= '%.2f' % new_val
							# 找到了就停止本次循环
						break
				
				if find == 0:
					new_gd_info[-3] = u'新进'
					
				new_gd_info[3]	= '%.2f' % new_val
		
	def checkLTGD(self, response):
		sel = scrapy.selector.Selector(response)

		# <td colspan="5" align="left" class="tdr">2011-09-30</td>
		date_list_sel = sel.xpath('//td[@class="tdr"]')
		date_list_txt = date_list_sel.xpath('.//text()').extract()
		# print(date_list_txt)
		# print('date_list_txt len = ', len(date_list_txt))
				
		date_cur = 0
		
		#for data_list_s in date_list_sel:
		# <div align="center">上海机场(集团)有限公司</div>
		tbody = sel.xpath('//div[@align="center"]')
		tbody_td_list = tbody.xpath('.//text()').extract()
		# print(tbody_td_list)
		length = len(tbody_td_list)
		all_info = []
		jidu_info = []
		ret_info_list = []
		name = self.self_dict[self.stock_num]
		# print('length = ', length)
		for i in range(length):
			# print('i = %d date_cur=%d' % (i, date_cur))
			if tbody_td_list[i].isdigit() and int(tbody_td_list[i]) < 13 and date_cur < len(date_list_txt) and i+3 < length and '.' in tbody_td_list[i+3] :
				# (stock_number varchar(20), cname varchar(20),gudong_name varchar(100), hold_num varchar(20), percent varchar(20), ichange varchar(20), date varchar(20), stock_type varchar(20))
				gd_info = [self.stock_num, name, tbody_td_list[i+1], tbody_td_list[i+2], tbody_td_list[i+3], '-', date_list_txt[date_cur], '流通A股']
				jidu_info.append(gd_info)
				# print(gd_info)
				if (i+5 < length) and tbody_td_list[i+5].isdigit() == False :
					all_info.append(jidu_info)
					jidu_info = [] 
					date_cur += 1
				i += 3
			i += 1
		
		# 信息保存到文件中
		# with open('temp.txt', 'w') as f:
			# i = 0
			# for info in all_info:
				# cmd = '\n %d  %s ---------------------------\n' % (i, date_list_txt[i])
				# f.writelines(cmd)
				# number = 0
				# for l in info:
					# f.writelines(l)
					# f.writelines('\n')
					# number += 1
				# cmd2 = '******************%d***********' % number
				# f.writelines(cmd2)
				# i += 1
					
		# print('all_info len = ', len(all_info))
		# jidu_ptr = 0
		cacl_times = len(all_info) - 1
		
		self.reCalcGDData(cacl_times, all_info)
		# print('cacl_times =', cacl_times)
		# for j in range(cacl_times):
			# jidu_new_div = all_info[j]
			# if (j+1) == cacl_times:
				# return
			# jidu_old_div = all_info[j+1]
			# # 从一个季度里拿出每个股东数据和上衣季度对比
			# for i in range(len(jidu_new_div)):
				# find = 0
				# new_gd_info = jidu_new_div[i]
				# # 当前股东信息和上一个季度每个股东对比
				# new_val = int(new_gd_info[3]) / 10000.0
				# for k in range(len(jidu_old_div)):
					# old_gd_info = jidu_old_div[k]
					# # 如果股东在上个季度存在， 则计算差值
					# find = 0
					# old_val = int(old_gd_info[3]) / 10000.0
					# if new_gd_info[2] == old_gd_info[2] :
						# find = 1
						# if new_gd_info[3] == old_gd_info[3]:
							# new_gd_info[-3] = u'不变'
						# else:
							# val = '%.2f' % (new_val - old_val)
							# new_gd_info[-3] = str(val)
							# # new_gd_info[3]	= '%.2f' % new_val
							# # 找到了就停止本次循环
						# break
				
				# if find == 0:
					# new_gd_info[-3] = u'新进'
					
				# new_gd_info[3]	= '%.2f' % new_val
				# ret_info_list.append(new_gd_info)
				
		# print('---------------------------------------------------')
		# print('all_info = ', all_info)
		
		# print(all_info)
		# print('all_info len = ', len(all_info))
		# 信息保存到文件中
		# with open('over.txt', 'w') as f:
			# i = 0
			# for info in all_info:
				# cmd = '\n %d  %s ---------------------------\n' % (i, date_list_txt[i])
				# f.writelines(cmd)
				# number = 0
				# for l in info:
					# f.writelines(l)
					# f.writelines('\n')
					# number += 1
				# cmd2 = '******************%d***********' % number
				# f.writelines(cmd2)
				# i += 1
				
		# print(all_info)
		for info in all_info:
			stockSql.store_old_lt_gudong_db(info)
				

	def parse(self, response):
		pattern = re.compile(r'60[0-3]\d{3}|00[0,2]\d{3}|300\d{3}') 
		match = pattern.search(str(response)) 
		if match:
			self.stock_num = match.group()
			self.checkLTGD(response)
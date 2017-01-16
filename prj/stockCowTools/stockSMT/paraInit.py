import os

import stockSMT.update_stock as update_stock
import stockSMT.stockSql as stockSql
class StockSMTInit():
	print('this is stockSMT StockSMTInit class')
	update_stock.get_and_store_all_stock_list()
	# update_stock.generateDzhUrls()
	# update_stock.generateThsUrls()
	update_stock.generateXlUrls()
	
	stockSql.init_mysql_gudong_data_base()
	
	def __init__(self):
		print('this is stockSMT package')
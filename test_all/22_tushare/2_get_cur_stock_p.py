# -*- coding: utf-8 -*-
import tushare as ts
import time
print ts.__version__


stock_list = [
		'300401', #花园生物
		'300058', #蓝色光标
		'002387' # 黑牛食品
]

while True:
	print('\n------------------------------------------------------------------------------')
	for stock in stock_list:
		df = ts.get_realtime_quotes(stock) 
		print df[['code','name','price','high','low']]
	
	time.sleep(3)

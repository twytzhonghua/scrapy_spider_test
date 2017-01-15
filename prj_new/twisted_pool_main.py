import UpdateStockNumbers
import yiDianData




if __name__ == '__main__':

	#sys.setdefaultencoding( "utf-8" )
	stocks = UpdateStockNumbers.update_all_stock_number()	
	#print(stocks)
	urls = yiDianData.generateYiDianALLDataUrls(stocks)
	
	for url in urls:
		yiDianData.start_yidian_url_requset(url)
	#urls = generateYiDianALLDataUrls(stocks)
	print('start')
	#main(urls)
	
	
	
	print('over')
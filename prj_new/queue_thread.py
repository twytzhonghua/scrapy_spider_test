import threading, sys
import time
import queue
import UpdateStockNumbers
import yiDianData
from lxml import etree
import importlib


#构造一个不限制大小的的队列
SHARE_Q = queue.Queue() 
#设置线程个数
_WORKER_THREAD_NUM = 5   

class MyThread(threading.Thread) :

    def __init__(self, func) :
        super(MyThread, self).__init__()
        self.func = func

    def run(self) :
        self.func()

def worker() :
	global SHARE_Q
	while not SHARE_Q.empty():
		#获得任务参数 
		item = SHARE_Q.get()
		print( "Processing : ", item)
		response = yiDianData.new_get_html(item)
		yiDianData.checkLTGD(response)
		#yiDianData.start_yidian_url_requset(item)
		#time.sleep(1)
		
def generateYiDianALLDataUrls(stock_number_list):
	urls = []
	with open('D:/python/scrapy_spider_test/prj_new/date_cfg.cfg', 'rb') as f:
		dates = f.readlines()
		print(dates)
	
	for date in dates:
		for number in stock_number_list:
			urls.append( 'http://www.yidiancangwei.com/gudong/sdlt_' + number + '_' + date.strip() + '.html')
			
	#print(urls)
	#with open('yidian_urls.txt', 'wb') as f:
	#	for url in urls:
	#		f.write(url)
	#		f.write('\n')
	return urls		
		

		
		
def startRequestURLSmain(urls) :
    global SHARE_Q
    threads = []
	#向队列中放入任务
    for url in urls :  
        SHARE_Q.put(url)
    for i in range(_WORKER_THREAD_NUM) :
        thread = MyThread(worker)
        thread.start()
        threads.append(thread)
    for thread in threads :
        thread.join()


#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading, sys, os
import time
import Queue
import yiDianData
import UpdateStockNumbers

SHARE_Q = Queue.Queue()  #构造一个不限制大小的的队列
_WORKER_THREAD_NUM = 10   #设置线程个数

class MyThread(threading.Thread) :

    def __init__(self, func) :
        super(MyThread, self).__init__()
        self.func = func

    def run(self) :
        self.func()

def worker() :
    global SHARE_Q
    while not SHARE_Q.empty():
		url = SHARE_Q.get() #获得任务
		print(url)
		response = yiDianData.get_html_response(url)
		yiDianData.checkLTGD(response)
        

def main(urls) :
    global SHARE_Q
    threads = []
    for url in urls :  #向队列中放入任务
        SHARE_Q.put(url)
    for i in xrange(_WORKER_THREAD_NUM) :
        thread = MyThread(worker)
        thread.start()
        threads.append(thread)
    for thread in threads :
        thread.join()
		
reload(sys)
sys.setdefaultencoding( "utf-8" )	
#stocks = UpdateStockNumbers.update_all_stock_number()		
#urls = yiDianData.generateYiDianALLDataUrls(stocks)
#main(urls)
print "ok"
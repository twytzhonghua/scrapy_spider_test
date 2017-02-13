# -*- coding: utf-8 -*-
import threading,Queue,sys
import yiDianData


threads=[]
singlelock = threading.Lock()    #设置一个线程锁,避免重复调用

class downloader(threading.Thread):
        def __init__(self, urls):
            threading.Thread.__init__(self)
            self.urls=urls
		    
 
        def run(self):
			#singlelock.acquire()
			for url in self.urls:
				response = yiDianData.get_html_response(url)
				yiDianData.checkLTGD(response)
			#singlelock.release() 
               

 
#多线程下载文件
def main_download(urls):
    #for url in urls:
		t=downloader(urls)
		threads.append(t)
		t.start()
		
		
def start_main(urls):
	main_download(urls)
	for t in threads:
		t.join()


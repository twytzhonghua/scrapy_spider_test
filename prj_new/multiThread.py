import os
import threading
import multiprocessing
import yiDianData


# worker function
def worker(urls, lock):
	#lock.acquire()
	print("pid = ", os.getpid())
	for url in urls:
		#print(url)
		response = yiDianData.get_html_response(url)
		yiDianData.checkLTGD(response)
	#lock.release()


# Multi-thread
def start_download_yidian(urls):
	record = []
	numbers = len(urls)
	times = 10
	per_time = numbers / 10
	lock  = threading.Lock()
	

	for i in range (0, times):
		begin =  i * per_time
		stop =  (i + 1)* per_time - 1
		tmp_urls = urls[begin:stop]
		thread = threading.Thread(target=worker,args=(tmp_urls,lock))
		thread.start()
		record.append(thread)
		
	begin = (i + 1)* per_time
	stop = numbers - 1

	tmp_urls = urls[begin:stop]
	thread = threading.Thread(target=worker,args=('thread',lock))
	thread.start()
	record.append(thread)
	

	for thread in record:
		thread.join()
#-*- coding:utf-8 -*-

import tushare as ts

import requests

from prettytable import PrettyTable
import datetime

from email.header import Header
from email.mime.text import MIMEText
import smtplib
import os
import urllib
from bs4 import BeautifulSoup
import multiprocessing


mail_msg_info = []

def getHtml(url):
	# page = urllib.request.urlopen(url)
	# html = page.read()
	# return html
	HEADERS = { 'Cookie':'', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36' }
	r = requests.get(url, headers=HEADERS)
	# r = requests.get(url)
	return r.content

def send_mail(str):
    from_addr = "zhonghuaqrs@163.com"
    to_addr = ['yangzh0906@thundersoft.com']
    # to_addr = ['zhonghuaqrs@163.com', '466636092@qq.com']
    smtp_server = "smtp.163.com"
    password = "twyt_159"

    msg = MIMEText(str, 'plain', 'utf-8')
    msg['From'] = from_addr
    msg['To'] =   ','.join(to_addr)
    today = datetime.date.today()
    sbuject_str = u'火车票提示 %s'  %  today
    msg['Subject'] = Header(sbuject_str, 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())

    server.quit() 


def add_url_to_multiprocess(url):
	p = multiprocessing.Process(target=parse_html, args=(url,))
	p.start()
	p.join


def parse_yidian_shishi_zuli_caozuo(url):
	my_html = getHtml(url)
	# soup = BeautifulSoup(my_html, 'html.parser')
	soup = BeautifulSoup(my_html)
	content = soup.find_all('td')

	all_info = []
	fmt_info = []
	for con in content:
		all_info.append(con.string.split()[0])

	# print(all_info)
	length = int(len(all_info)/9)

	for i in range(0, length ):
		info_s = [all_info[i*9], all_info[i*9+ 1], all_info[i*9+ 2], all_info[i*9+ 3], all_info[i*9+ 4], all_info[i*9+ 5], all_info[i*9+ 6], all_info[i*9+ 7],all_info[i*9 + 8]]
		fmt_info.append(info_s)

	# mail_msg_info.append()

	Mheaders = u'序号 代码 名称 价格 涨幅 涨速 流通股本 买入 卖出 '.split()
	pt = PrettyTable()

	pt._set_field_names(Mheaders)
	for i in fmt_info:
		pt.add_row(i)

	str1 = str(pt)

	# return str1
	print(str1)

	#check if next useful url:
	useful_urls_div = soup.find('div',attrs={'class':'pagination'})
	if useful_urls_div:
		next_url_content = useful_urls_div.find_all('a',attrs={'class':'previous'})
		if next_url_content:
			for con in next_url_content:
				if con.get_text() == u'下一页' and con['class'][-1] != 'disable':
					# print(con['class'])
					add_url_to_multiprocess(con['href'])
			

def parse_html(url):
	if 'http://www.yidiancangwei.com/ShareTracking' in url:
		parse_yidian_shishi_zuli_caozuo(url)
	

if __name__ == '__main__':
	start_urls = ['http://www.yidiancangwei.com/ShareTracking.php'
	,'http://www.yidiancangwei.com/ShareTracking.php?Time=%s&Type=3' % datetime.date.today()
	]

	for url in start_urls:
		add_url_to_multiprocess(url)


	# print('game over')

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



def getHtml(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	return html

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


def  parse_html(html):
	soup = BeautifulSoup(html)

	# print(soup.body.contents )

	content = soup.find_all('td')

	all_info = []
	fmt_info = []
	for con in content:
		# print(con.string.split()[0])
		all_info.append(con.string.split()[0])

	# print(all_info)
	length = int(len(all_info)/9)

	for i in range(0, length ):
		info_s = [all_info[i*9], all_info[i*9+ 1], all_info[i*9+ 2], all_info[i*9+ 3], all_info[i*9+ 4], all_info[i*9+ 5], all_info[i*9+ 6], all_info[i*9+ 7],all_info[i*9 + 8]]
		# print(info_s)
		fmt_info.append(info_s)

	# print(fmt_info)
	Mheaders = u'序号 代码 名称 价格 涨幅 涨速 流通股本 买入 卖出 '.split()
	pt = PrettyTable()

	pt._set_field_names(Mheaders)
	for i in fmt_info:
		pt.add_row(i)
	# print(length/9)
	# print( soup.find_all('td'))
	# print(str(pt))
	str1 = str(pt)
	with open('ret.txt', 'w') as f:
		f.write(str1)
	# return str(pt)
	# with open('ret.txt', 'r') as f:
	# 	str2 = f.read()
	# 	print(str2)
	# 	send_mail(str2)
	return str1






if __name__ == '__main__':
	url = 'http://www.yidiancangwei.com/ShareTracking.php'
	my_html = getHtml(url)
	str1 = parse_html(my_html)


	send_mail(str1)
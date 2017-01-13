#! /usr/bin/env python
#coding=utf-8
# -*- coding:UTF-8 -*-
'''
Created on 2015年9月14日
 
@author: xiaowenhui
'''
 
import demjson
import urllib.request

import tushare as ts
import pandas as pd

'''
encode：编码，将python对象编码成JSON字符串
decode:解码，将JSON字符串解码成python对象
'''
# 
#data1 = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
#json1 = demjson.encode(data1)
#print(json1)
# 
#json2 = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
#data2 = demjson.decode(json2)
#print(data2)
# 
#json3 = "{'Transformers': {'rating': 'R', 'description': 'A schientific fiction', 'format': 'DVD', 'stars': '8', 'year': '1989', 'type': 'Anime, Science Fiction'}, 'Ishtar': {'rating': 'PG', 'type': 'Comedy', 'description': 'Viewable boredom', 'stars': '2', 'format': 'VHS'}, 'Enemy Behind': {'rating': 'PG', 'description': 'Talk about a US-Japan war', 'format': 'DVD', 'stars': '10', 'year': '2003', 'type': 'War, Thriller'}, 'Trigun': {'rating': 'PG', 'description': 'Vash the Stampede!', 'format': 'DVD', 'episodes': '4', 'stars': '10', 'type': 'Anime, Action'}}"
#data3 = demjson.decode(json3)
#print(data3)

#hq_url = 'http://hq.sinajs.cn/list=s_sh600135'
#page = urllib.request.urlopen(hq_url)
#html = page.read().decode('gb2312').split('"')[1].split(',')
##print(html)
##print(type(html))
#

#url = 'http://webf10.gw.com.cn/SH/B10/SH600767_B10.html'
#page = urllib.request.urlopen(url)
#read_content = page.read()
#with open('SH600767_B10.html', 'wb') as f:
#    f.write(read_content)

a = ts.get_stock_basics()

#a.to_csv('all_stock.csv', encoding='gbk', index=True)
print(type(a))
df = a
shape = df.shape
describe = df.describe()
print('shape = ', shape)
#print('describe = ', describe)
print(a)

df.sort(columns='name')

#df.to_csv('all_stock.csv', encoding='gbk', index=True)
#! /usr/bin/env python
#coding=utf-8
import tushare as ts
 
#a = ts.get_stock_basics()

a = ts.get_industry_classified()
print(type(a))
print(a)
 
#! /usr/bin/env python
#coding=utf-8
#Python数据处理的瑞士军刀：pandas
#
#####第二篇：快速进阶
#
#在上一篇中我们介绍了如何创建并访问pandas的Series和DataFrame类型的数据，本篇将介绍如何对pandas数据进行操作，
#掌握这些操作之后，基本可以处理大多数的数据了。首先，导入本篇中使用到的模块：
#

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

pd.set_option('display.width', 200)

dates = pd.date_range('20150101', periods=5)
print('dates  = ', dates)
#dates  =  DatetimeIndex(['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04', '2015-01-05'], dtype='datetime64[ns]', freq='D')

#将这个日期Series作为索引赋给一个DataFrame：
df = pd.DataFrame(np.random.randn(5, 4),index=dates,columns=list('ABCD'))
print('df = ', df)
#df =                     A         B         C         D
#2015-01-01  0.708299 -1.262400  0.506046 -1.505559
#2015-01-02  0.820239  1.332424  0.851686  0.415229
#2015-01-03 -0.024611  0.583965  0.754146  1.011566
#2015-01-04 -0.716278 -0.524244  1.503202 -0.507789
#2015-01-05  0.144840 -0.120734  0.725664 -1.228411
#

#只要是能转换成Series的对象，都可以用于创建DataFrame：

df2 = pd.DataFrame({ 'A' : 1., 'B': pd.Timestamp('20150214'), 'C': pd.Series(1.6,index=list(range(4)),dtype='float64'), 'D' : np.array([4] * 4, dtype='int64'), 'E' : 'hello pandas!' })
print('df2 = ', df2)
#df2 =       A          B    C  D              E
#0  1.0 2015-02-14  1.6  4  hello pandas!
#1  1.0 2015-02-14  1.6  4  hello pandas!
#2  1.0 2015-02-14  1.6  4  hello pandas!
#3  1.0 2015-02-14  1.6  4  hello pandas!


####二、数据的查看

#在多数情况下，数据并不由分析数据的人员生成，而是通过数据接口、外部文件或者其他方式获取。
#这里我们通过量化实验室的数据接口获取一份数据作为示例：

#from sklearn import svm

stock_list = ['000001.XSHE', '000002.XSHE', '000568.XSHE', '000625.XSHE', '000768.XSHE', '600028.XSHG', '600030.XSHG', '601111.XSHG', '601390.XSHG', '601998.XSHG']

raw_data = DataAPI.MktEqudGet(secID=stock_list, beginDate='20150101', endDate='20150131', pandas='1')

df = raw_data[['secID', 'tradeDate', 'secShortName', 'openPrice', 'highestPrice', 'lowestPrice', 'closePrice', 'turnoverVol']]
print('df.shape = ', df.shape)
print(df)

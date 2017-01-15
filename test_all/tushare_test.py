# -*- coding: utf-8 -*-
import tushare as ts

a = ts.get_hist_data('600848')

print(a)

print(type(a))
#df = ts.get_index()
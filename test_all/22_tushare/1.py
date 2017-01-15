# -*- coding: utf-8 -*-
import tushare as ts


token = '3207956af0aa3427e75a0ae1b294d990870373905df065302ae2311b7b3a8d07'
ts.set_token(token)

mkt = ts.Market() 
df = mkt.TickRTSnapshot(securityID='000001.XSHE')
print('my token = ', ts.get_token())
print(df)
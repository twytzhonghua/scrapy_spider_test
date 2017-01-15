# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
 
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY,YEARLY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc
 
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
 
ticker = '600028' # 600028 ��"�й�ʯ��"�Ĺ�Ʊ����
ticker += '.ss'   # .ss ��ʾ��֤ .sz��ʾ��֤
 
date1 = (2015, 8, 1) # ��ʼ���ڣ���ʽ��(�꣬�£���)Ԫ��
date2 = (2016, 1, 1)  # �������ڣ���ʽ��(�꣬�£���)Ԫ��
 
 
mondays = WeekdayLocator(MONDAY)            # ��Ҫ�̶�
alldays = DayLocator()                      # ��Ҫ�̶�
#weekFormatter = DateFormatter('%b %d')     # �磺Jan 12
mondayFormatter = DateFormatter('%m-%d-%Y') # �磺2-29-2015
dayFormatter = DateFormatter('%d')          # �磺12
 
quotes = quotes_historical_yahoo_ohlc(ticker, date1, date2)
if len(quotes) == 0:
    raise SystemExit
 
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
 
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(mondayFormatter)
#ax.xaxis.set_minor_formatter(dayFormatter)
 
#plot_day_summary(ax, quotes, ticksize=3)
candlestick_ohlc(ax, quotes, width=0.6, colorup='r', colordown='g')
 
ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
 
ax.grid(True)
plt.title('600028')
plt.show()
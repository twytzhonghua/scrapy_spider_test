#! /usr/bin/env python
#coding=utf-8
import wx

import queue_thread
import UpdateStockNumbers
import yiDianData

app = wx.App()
win = wx.Frame(None, title='yy love tt forever', size = (500, 600))

bkg = wx.Panel(win)

def startDownloadYidianData():
	stocks = UpdateStockNumbers.update_all_stock_number()	
	#print(stocks)
	urls = yiDianData.generateYiDianALLDataUrls(stocks)
	#urls = generateYiDianALLDataUrls(stocks)
	print('start')
	queue_thread.startRequestURLSmain(urls)
	print('over')



def search_gudong_func(event):
    pass

def clear_info_func(event):
    pass


def download_yidian_gudong_info(event):
    startDownloadYidianData()


downloadButton 	= wx.Button(bkg, label = u'下载数据')
downloadButton.Bind(wx.EVT_BUTTON, download_yidian_gudong_info)


searchButton = wx.Button(bkg, label = u'查询股东')
searchButton.Bind(wx.EVT_BUTTON, search_gudong_func)



clearButton 	= wx.Button(bkg, label = u'清空')
clearButton.Bind(wx.EVT_BUTTON, clear_info_func)





hbox = wx.BoxSizer()

hbox.Add(downloadButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(searchButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(clearButton, proportion=0, flag=wx.LEFT, border=5)

outStr = wx.TextCtrl(bkg, style = wx.TE_MULTILINE|wx.HSCROLL)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
vbox.Add(outStr,proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=5)
bkg.SetSizer(vbox)

win.Show()
app.MainLoop()








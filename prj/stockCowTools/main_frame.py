#coding=utf-8

import wx
import os
import update_stock



def stock_list_update(event):
    print('receive update button')
    stock_list = update_stock.update_all_stock_number()
    update_stock.generateYiDianGDUrls(stock_list)


def spider_start(event):
    os.system('C:/scrapy/stockSpider.exe')


def createMainFrame():
    app = wx.App()
    win = wx.Frame(None, title='yy love tt forever', size = (500, 600))
    
    bkg = wx.Panel(win)

    downloadButton 	= wx.Button(bkg, label = u'下载数据')
    downloadButton.Bind(wx.EVT_BUTTON, spider_start)
    
    updateStockButton 	= wx.Button(bkg, label = 'update')
    updateStockButton.Bind(wx.EVT_BUTTON, stock_list_update)
    
    
    hbox = wx.BoxSizer()
    hbox.Add(downloadButton, proportion=0, flag=wx.LEFT, border=5)
    hbox.Add(updateStockButton, proportion=0, flag=wx.LEFT, border=5)
    
    bkg.SetSizer(hbox)
    win.Show()
    app.MainLoop()
    
    
if __name__ == "__main__":
    createMainFrame()


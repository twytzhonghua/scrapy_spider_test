#coding=utf-8

import wx
import os
import update_stock
from stockCowTools.spiders.stockSql import * 

class SmartToolMainFrame( wx.Frame ):


    def stock_list_update(self,event):
        print('receive update button')
        stock_list = update_stock.update_all_stock_number()
        update_stock.generateThsUrls(stock_list)

    def spider_start(self, event):
        os.system('C:/scrapy/stockSpider.exe')

    def query_gudong_name(self, event):
        all_ret = []
        name = self.gudongNameText.GetValue()
        print("query_gudong_name %s" % name)
        rets = query_lt_gudong_name(name)
        self.outStr.Clear()
        for ret in rets:
            ret_str = "".join(tuple(ret))
            all_ret.append(ret_str)
            print(ret_str)
            self.outStr.AppendText(ret_str)
            self.outStr.AppendText('\n')
        #print(all_ret)
        
        #final_info = "".join(list(all_ret))
        
        #self.outStr.SetValue(final_info)

    def onAbout(self, evt):
        '''点击about的事件响应'''
        dlg = wx.MessageDialog(self, 'This app is a simple text editor', 'About my app', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def onExit(self, evt):
        '''点击退出'''
        self.Close(True)


    def createMenus(self):
        self.CreateStatusBar()
        
        menubar = wx.MenuBar()
        menufile = wx.Menu()
        
        mnuabout = menufile.Append(wx.ID_ABOUT, '&About', 'about this shit')
        mnuexit = menufile.Append(wx.ID_EXIT, 'E&xit', 'end program')
        
        menubar.Append(menufile, '&File')
        
        #事件绑定
        self.Bind(wx.EVT_MENU, self.onAbout, mnuabout)
        self.Bind(wx.EVT_MENU, self.onExit, mnuexit)
          
        self.SetMenuBar(menubar)
        


    def  __init__( self, parent ):
        app = wx.App()
        win = wx.Frame(None, title='stock smart tool', size = (500, 600))
        
        bkg = wx.Panel(win)
        #self.createMenus()
        self.downloadButton 	= wx.Button(bkg, label = u'下载数据')
        self.downloadButton.Bind(wx.EVT_BUTTON, self.spider_start)
        
        self.updateStockButton 	= wx.Button(bkg, label = '更新列表')
        self.updateStockButton.Bind(wx.EVT_BUTTON, self.stock_list_update)
        
        self.queryButton 	= wx.Button(bkg, label = '查询')
        self.queryButton.Bind(wx.EVT_BUTTON, self.query_gudong_name)
        
        self.gudongNameText = wx.TextCtrl(bkg)
        self.outStr = wx.TextCtrl(bkg, style = wx.TE_MULTILINE|wx.HSCROLL)    
        
        
        hbox = wx.BoxSizer()
        hbox.Add(self.downloadButton, proportion=0, flag=wx.LEFT, border=5)
        hbox.Add(self.updateStockButton, proportion=0, flag=wx.LEFT, border=5)
        
        hbox2 = wx.BoxSizer()
        hbox2.Add(self.gudongNameText, proportion=1, flag=wx.EXPAND)
        hbox2.Add(self.queryButton, proportion=0, flag=wx.LEFT, border=5)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
        vbox.Add(hbox2, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
        vbox.Add(self.outStr,proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=5)    
        
        bkg.SetSizer(vbox)
        win.Show()
        app.MainLoop()
    
    
if __name__ == "__main__":
    init_mysql_gudong_data_base()
    frame = SmartToolMainFrame(None)


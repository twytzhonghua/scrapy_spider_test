#-*- coding:utf-8 -*-

import sys
from langconv import *

import wx


def jian2fan(event):
	line = transferStr.GetValue()
	line = Converter('zh-hant').convert(line)
	#line = line.encode('gbk')
	#print(line)
	outStr.SetValue(line)


# fan 2 jian
def fan2jian(event):
	line = transferStr.GetValue()
	line = Converter('zh-hans').convert(line)
	#line = line.encode('gbk')
	outStr.SetValue(line)


	
app = wx.App()
win = wx.Frame(None, title='yy love tt forever', size = (500, 600))
#icon=wx.EmptyIcon()
#icon.LoadFile("myicon.ico",wx.BITMAP_TYPE_ICO) 
#win.SetIcon(icon)  
#win.tbicon=wx.TaskBarIcon()  
#win.tbicon.SetIcon(icon,"yy love tt forever")  


bkg = wx.Panel(win)


jian2fanButton = wx.Button(bkg, label = u'简转繁')
jian2fanButton.Bind(wx.EVT_BUTTON, jian2fan)

fan2jianButton 	= wx.Button(bkg, label = u'繁转简')
fan2jianButton.Bind(wx.EVT_BUTTON, fan2jian)

transferStr = wx.TextCtrl(bkg)
outStr = wx.TextCtrl(bkg, style = wx.TE_MULTILINE|wx.HSCROLL)

hbox = wx.BoxSizer()

hbox.Add(transferStr, proportion=1, flag=wx.EXPAND)
hbox.Add(jian2fanButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(fan2jianButton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND|wx.ALL, border=5)
vbox.Add(outStr,proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=5)
bkg.SetSizer(vbox)

win.Show()
app.MainLoop()



	

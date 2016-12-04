# -*- coding:utf-8 -*-

import sys
from langconv import *

import wx


reload(sys)
sys.setdefaultencoding('utf-8')

#line = '我爱你'


def jian2fan(event):
	line = transferStr.GetValue()
	a = Converter('zh-hant').convert(line.decode('utf-8'))
	a = line.encode('utf-8')
	print(a)
	outStr.SetValue(a)


# fan 2 jian
def fan2jian(event):
	line = transferStr.GetValue()
	line = Converter('zh-hans').convert(line.decode('utf-8'))
	line = line.encode('utf-8')
	outStr.SetValue(line)


	
app = wx.App()
win = wx.Frame(None, title='yy love tt', size = (500, 600))
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



	
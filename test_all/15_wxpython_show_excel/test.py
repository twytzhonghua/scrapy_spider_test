#!/usr/bin/env python
#coding:UTF-8
'''
Created on 2010-5-14
wxPython多行文本输入框，以及丰富样式模式的
使用范例
@author: zyl508@gmail.com
'''

import wx

class MultiTextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Example For MultiTextCtrl",
                          size=(300,250))
        panel=wx.Panel(self,-1)
        
        #普通多行文本输入框
        multiLabel=wx.StaticText(panel,-1,"Multi-Line:")
        multiText=wx.TextCtrl(panel,-1,"Here we go\n\n\ntest",
                              size=(200,100),
                              style=wx.TE_MULTILINE)
        multiText.SetInsertionPoint(0)
        
        #丰富式样的多行文本输入框
        richLabel=wx.StaticText(panel,-1,"Rich-Label:")
        richText=wx.TextCtrl(panel,-1,
                             "如果系统支持的话\n\nThis is a diff font",
                             size=(200,100),
                             #创建丰富文本控件
                             style=wx.TE_MULTILINE|wx.TE_RICH2)
        richText.SetInsertionPoint(0)
        #设置richText控件的文本样式
        richText.SetStyle(2,6,wx.TextAttr("white","black"))
        points=richText.GetFont().GetPointSize()
        #创建一个字体样式
        f=wx.Font(points+3,wx.ROMAN,wx.ITALIC,wx.BOLD,True)
        #用创建的字体样式设置文本样式
        #richText.SetStyle(8,14,wx.TextAttr("blue",f))
        
        #将上边俩文本框用Sizer管理布局
        sizer=wx.FlexGridSizer(cols=2,vgap=6,hgap=6)
        #AddMany方法添加的一定是一个列表list
        sizer.AddMany([multiLabel,multiText,richLabel,richText])
        panel.SetSizer(sizer)
        
class MyApp(wx.App):
    def __init__(self):
        #重构__init__方法，将错误信息重定位到文件中;
        #默认redirect=True，输出到StdOut或StdError;
        #为防止程序因错误一闪而过无法捕捉信息，可在
        #控制台中使用python -i example.py来运行程序。
        wx.App.__init__(self,redirect=False,filename=r"C:\Runlog.txt")
    def OnInit(self):
        frame=MultiTextFrame()
        frame.Show(True)
        return True
    
def main():
    app=MyApp()
    app.MainLoop()

if __name__=="__main__":
    main()

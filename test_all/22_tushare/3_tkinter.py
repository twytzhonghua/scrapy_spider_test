# -*- coding: utf-8 -*-
import urllib.request
#import requests
import tkinter
from tkinter import *


class StockParser():
    def __init__(self,code_data,edit):
        self.stock_data = code_data
        self.edit=edit
        
        if self.stock_data.split('"')[1] =='': 
            pass
        else:
            print(self.stock_data.split('"')[1])
            self.stock_data=self.stock_data.split('"')[1]
            name = self.stock_data.split(',')[0]
            opening_price = float(self.stock_data.split(',')[1])
            closing_price = float(self.stock_data.split(',')[2])
            price = float(self.stock_data.split(',')[3])
            high = float(self.stock_data.split(',')[4])
            low = float(self.stock_data.split(',')[5])
            
            self.edit.insert(END,[name,opening_price,closing_price,high,low,price,])
    


class Window:
    def __init__(self, root):
        self.root = root      # 创建组件
        self.entryUrl = tkinter.Entry(root,width = 30)
        self.entryUrl.place(x = 65, y = 15)
        self.get = tkinter.Button(root,text = '查询', command = self.Get)
        self.get.place(x = 350, y = 15)
        self.add = tkinter.Button(root,text = '添加', command = self.Add)
        self.delete = tkinter.Button(root,text = '删除', command = self.Del)
        self.add.place(x = 80, y = 55)
        self.delete.place(x=120,y=55)    
        #添加布局框 下面的self.edit, self.scrollbar是插入在frame中的哦    
        self.frame = tkinter.Frame(root, bd=2)
        self.frame.place(x=200,y = 90)
        self.scrollbar = tkinter.Scrollbar(self.frame)
        self.edit = tkinter.Listbox(self.frame,yscrollcommand = self.scrollbar.set,
                width = 50, height = 22)  
        self.scrollbar.config(command=self.edit.yview)
          
        self.edit.grid(row=1,column=2)#这里用了grid，可以学习一下它的用法
        self.scrollbar.grid(row=1,column=3,sticky='ew')
        
        self.indicate=tkinter.Label(root,text='(Please input stock code:sh000000)',fg='red') #这里是完全没有改动，沿用上一节
        self.indicate.place(x=65,y=35)
        self.StockList=[]
    def ListUpdate(self):
        self.lb=tkinter.Listbox(self.root,selectmode = BROWSE)
        for code in self.StockList:
            self.lb.insert(END,code)
        self.lb.pack()
        self.lb.place(x=50,y=90)    
    def Add(self):
        code = self.entryUrl.get()    
        if re.match(r'\w{2}\d{6}$',code) and code not in self.StockList:
            self.StockList.append(code) 
        else:
            pass
        self.ListUpdate()

    def Del(self):
        code=self.entryUrl.get()
        if code in self.StockList:
            self.StockList.remove(code)
        self.ListUpdate()

    def Get(self):
        if self.edit.get(0):
            print(self.edit.get(0))
            self.edit.delete(0,END)
        self.edit.insert(END,['名 字','开盘价','闭盘价','最高','最低','当前价格'])
        for code in self.StockList: 
            url='http://hq.sinajs.cn/list=%s' % (code,)
            page=urllib.request.urlopen(url) #为什么urllib不行呢？
            html= page.read() #记住这样得到的是html，必要是需要用HTMLParser解析，或者手动解析。
            stock_data=html.decode('gb2312')
            #r = requests.get(url)#当然使用requests也是没问题哒               
            #stock_data= r.text  #text直接得到的就是str格式的
            #stock_content=r.content.decode('gb2312')#content则需要转换格式
            hp = StockParser(stock_data,self.edit)

def main():

    root = tkinter.Tk()
    root.title('简易股票查询')
    window = Window(root)
    root.minsize(600,500)
    root.maxsize(600,500)
    root.mainloop()

if __name__ =='__main__':
    main()

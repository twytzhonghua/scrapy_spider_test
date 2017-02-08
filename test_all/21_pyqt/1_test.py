#!/bin/env python3  
# -*- coding: utf-8 -*-  

import sys  
from PyQt5.QtWidgets import QApplication, QWidget    #导入相应的包
      
if __name__ == '__main__':  
      
     app = QApplication(sys.argv)         #创建QApplication对象是必须，管理整个程序，参数可有可无，有的话可接收命令行参数
      
     w = QWidget()                        #创建窗体对象，
     w.resize( 250, 150 )                 #设置窗体大小
     w.move( 100, 300 )                   #设置在屏幕上的显示位置
     w.setWindowTitle( 'Simple' )         #设置窗口标题
     w.show()                             #窗口显示

     sys.exit( app.exec_() )  

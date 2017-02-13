# -*- coding:utf-8 -*-

import platform

def getToolBaseWorkDirectory():
    plat =  platform.system()
    if plat == 'Linux':
        dir = '/home/yzh/'
    else:
        dir = 'C:/scrapy/'

    return dir



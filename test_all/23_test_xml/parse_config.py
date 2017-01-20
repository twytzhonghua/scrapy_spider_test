#! /usr/bin/env python
#coding=utf-8
import xml.etree.ElementTree as ET 

import sys 

tree = ET.parse("stockSmtCfg.xml")     #打开xml文档   
#root = ET.fromstring(country_string) #从字符串传递xml   
root = tree.getroot()         #获得root节点  '


for child in root:   
    print ( 'child tag(%s) attr(%s) ' % (child.tag, child.attrib ) )
    
yidianNode = root.find('yidian')
r = yidianNode.find('enable').text   #子节点下节点rank的值 
print('yidianNode en = ', r)
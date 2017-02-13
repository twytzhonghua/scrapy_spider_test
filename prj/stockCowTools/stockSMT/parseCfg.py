#coding=utf-8


import os, sys
import xml.etree.ElementTree as ET 

import xml.dom.minidom as Dom  
import stockSMT.globalPars as globalPars

def create_yidian_cfg(doc):
    cfg_node = doc.createElement("yidian")
    enable_node = doc.createElement("enable")  
    enable_value = doc.createTextNode("False")  
    enable_node.appendChild(enable_value)
    
    cfg_node.appendChild(enable_node)
    return cfg_node
    

def create_ths_cfg(doc):
    cfg_node = doc.createElement("tonghuashun")
    enable_node = doc.createElement("enable")  
    enable_value = doc.createTextNode("Enable")  
    enable_node.appendChild(enable_value)

    cfg_node.appendChild(enable_node)
    return cfg_node


def create_dzh_cfg(doc):
    cfg_node = doc.createElement("dazhihui")
    enable_node = doc.createElement("enable")  
    enable_value = doc.createTextNode("False")  
    enable_node.appendChild(enable_value)

    cfg_node.appendChild(enable_node)
    return cfg_node


def create_xinlang_cfg(doc):
    cfg_node = doc.createElement("xinlang")
    enable_node = doc.createElement("enable")  
    enable_value = doc.createTextNode("False")  
    enable_node.appendChild(enable_value)

    cfg_node.appendChild(enable_node)
    return cfg_node




def create_stock_smt_cfg():
    print('create_stock_smt_cfg')
    doc = Dom.Document()  
    root_node = doc.createElement("stock_crawl_cfg")  
    root_node.setAttribute("developer", "zhonghua")  
    doc.appendChild(root_node)  
    yiDianNode = create_yidian_cfg(doc)
    thsNode = create_ths_cfg(doc)
    dzhNode = create_dzh_cfg(doc)
    xinlangNode = create_xinlang_cfg(doc)
    
    root_node.appendChild(yiDianNode)
    root_node.appendChild(thsNode) 
    root_node.appendChild(dzhNode) 
    root_node.appendChild(xinlangNode) 
    
    with open(globalPars.getToolBaseWorkDirectory() + "stockSmtCfg.xml", "w")  as f:
        str = doc.toprettyxml(indent = "\t", newl = "\n", encoding = "utf-8")
        f.write(bytes.decode(str))


def get_stock_smt_cfg_en_name():
#    en_list = []

    cfg_exist = os.path.isfile("c:/scrapy/stockSmtCfg.xml")
    print('c:/scrapy/stockSmtCfg.xml is', cfg_exist)
    if cfg_exist:
        print('c:/scrapy/stockSmtCfg.xml is already exist')
    else:
       create_stock_smt_cfg()

    tree = ET.parse(globalPars.getToolBaseWorkDirectory() + "stockSmtCfg.xml")     #打开xml文档
    root = tree.getroot()         #获得root节点  '
   
    sNode = root.find('yidian')
    if( sNode.find('enable').text == 'Enable' ) :
#        en_list.append('yidian')
        return 'yidian'
    
    sNode = root.find('tonghuashun')
    if( sNode.find('enable').text == 'Enable' ) :
#        en_list.append('tonghuashun')
        return 'tonghuashun'

    sNode = root.find('dazhihui')
    if( sNode.find('enable').text == 'Enable' ) :
#        en_list.append('dazhihui')
        return 'dazhihui'
        
        
    sNode = root.find('xinlang')
    if( sNode.find('enable').text == 'Enable' ) :
#        en_list.append('xinlang')
        return 'xinlang'
#    return en_list
    

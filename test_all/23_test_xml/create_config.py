#! /usr/bin/env python
#coding=utf-8
import xml.dom.minidom as Dom  


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
    enable_value = doc.createTextNode("False")  
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
    
    with open("stockSmtCfg.xml", "w")  as f:
        str = doc.toprettyxml(indent = "\t", newl = "\n", encoding = "utf-8")
        f.write(bytes.decode(str))
    
    
if __name__ == "__main__":
    create_stock_smt_cfg()
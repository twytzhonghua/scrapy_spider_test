#! /usr/bin/env python
#coding=utf-8
import xml.dom.minidom as Dom  
 
if __name__ == "__main__":  
    doc = Dom.Document()  
    root_node = doc.createElement("book_store")  
    root_node.setAttribute("name", "newhua")  
    root_node.setAttribute("website", "http://www.jb51.net")  
    doc.appendChild(root_node)  
 
    book_node = doc.createElement("book1")  
 
    book_name_node = doc.createElement("name")  
    book_name_value = doc.createTextNode("hamlet")  
    book_name_node.appendChild(book_name_value)  
    book_node.appendChild(book_name_node)  
 
    book_author_node = doc.createElement("author")  
    book_author_value = doc.createTextNode("William Shakespeare")  
    book_author_node.appendChild(book_author_value)  
    book_node.appendChild(book_author_node)  
 
    root_node.appendChild(book_node)  
 
    with open("book_store.xml", "w")  as f:
        str = doc.toprettyxml(indent = "\t", newl = "\n", encoding = "utf-8")
        f.write(bytes.decode(str))
    
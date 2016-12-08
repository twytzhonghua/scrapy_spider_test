# -*-coding: UTF-8 -*-
from twisted.internet import reactor
from twisted.web import client
 
def result(content):
    print(content)
    reactor.stop()

url = 'http://blog.csdn.NET'
burl = bytes(url,encoding="utf-8") 
deferred = client.getPage(burl)
deferred.addCallback(result)   
reactor.run()
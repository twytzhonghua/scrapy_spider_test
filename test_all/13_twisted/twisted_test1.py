#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Author:pako
#Email/gtalk:zealzpc@gmail.com
from twisted.python import threadable
threadable.init(1)
from twisted.internet import threads, reactor,defer
from random import randint
import time
    
def run():
    
    result=[]
    
    def listCallback(result):  
        """
                    拿到所有线程执行完返回的结果
        """
        result=[r[1] for r in result]
        print(result)
        print("deferlist result =", result)
    
    def doSomeLongTimeThing(sleeptime=0):  
        """ 
                    每个线程同时做的耗时的事
        """  
        print(sleeptime)
        time.sleep(sleeptime)
        return sleeptime
    
    deferlist=[]
    #创建deferlist中的deferred
    for i in range(10):
        d = threads.deferToThread(doSomeLongTimeThing,sleeptime=randint(3,5))
        deferlist.append(d)
    #创建deferredlist
    dl = defer.DeferredList(deferlist)
    #给deferredlist添加回调函数
    dl.addBoth(listCallback)
    print("1st line after the addition of the callback"  )
    print("2nd line after the addition of the callback"  )

if __name__ == '__main__':  
    print("begin ---------------------1111111111")
    run()
    reactor.run()  

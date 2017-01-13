#! /usr/bin/env python
#coding=utf-8
import csv
import tushare as ts
#import pandas as pd

def get_and_store_all_stock_list():
    a = ts.get_stock_basics()
    a.to_csv('c:/scrapy/all_stock.csv', encoding='gbk', index=True)



def generate_stock_dic():
    i = 0
    stock_dic = {}
    csv_reader = csv.reader(open('c:/scrapy/all_stock.csv', encoding='gbk'))
    for row in csv_reader:
        if(i == 0) :
            pass
        else:
            if(len(row[0]) == 1):
                row[0] = '00000' + row[0]
            elif (len(row[0]) == 2):
                row[0] = '0000' + row[0]
            elif (len(row[0]) == 3):
                row[0] = '000' + row[0]
            elif (len(row[0]) == 4):
                row[0] = '00' + row[0]
            elif (len(row[0]) == 5):
                row[0] = '0' + row[0]
            else:
                pass
            
            stock_dic[row[0]] = row[1] 
            stock_number.append(row[0])
            stock_name.append(row[1])
        i += 1
    
    return stock_dic


get_and_store_all_stock_list()
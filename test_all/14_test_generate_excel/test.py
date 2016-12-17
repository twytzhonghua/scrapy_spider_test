#! /usr/bin/env python
#coding=utf-8
import xlwt
f = xlwt.Workbook() #创建工作簿
sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet

list_info = [('杨成', '2016-09-30', '海顺新材', '300501 ', '1.64', '22.00', '新进', '流通A股'), ('杨成', '2016-06-30', '万里石', '002785 ', '0.32', '16.00', '新进', '流通A股'), ('杨成', '2016-06-30', '东音股份', '002793 ', '0.54', '13.40', '新进', '流通A股'), ('杨成', '2016-06-30', '永和智控', '002795 ', '0.53', '13.20', '新进', '流通A股'), ('杨成', '2016-06-30', '名家汇', '300506 ', '0.53', '16.00', '新进', '流通A股'), ('杨成', '2016-06-30', '川金诺', '300505 ', '0.60', '14.00', '新进', '流通A股')]




for i in range(len(list_info)):
    temp = list_info[i]
    for j in range(8):
        sheet1.write(i,j,temp[j])
    #print(type(list_info[i]))
    #sheet1.write(i,temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7])#表格的第一行开始写。第一列，第二列。。。。 
    #sheet1.write(i,temp[0], temp[1], temp[2])
    #print("%s %s %s %s %s %s %s %s " % (temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7]))
f.save('text.xls')#保存文件

#! /usr/bin/env python
#coding=utf-8

import pytesseract 
from PIL import Image 


#im = Image.open("verify.jpg")#(将图片转换为8位像素模式)
#im = im.convert("P") #打印颜色直方图
#print(im.histogram() )
#im2 = Image.new("P",im.size,255)
#
#
#his = im.histogram()
#values = {}
#
#for i in range(256):
#    values[i] = his[i]
#
#for j,k in sorted(values.items(),key=lambda x:x[1],reverse = True)[:10]:
#    print(j,k)
#
#
#for x in range(im.size[1]):
#    for y in range(im.size[0]):
#        pix = im.getpixel((y,x))
##        print(pix)
#        if pix == 138 or pix == 173 or pix == 140: # these are the numbers to get
#            im2.putpixel((y,x),0)
#            
#im2.show()
#


img = Image.open("verify.jpg",'r')
vcode = pytesseract.image_to_string(img)
print(vcode)
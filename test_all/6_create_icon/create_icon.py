# -*- coding: utf-8 -*-
import os,sys
from PIL import Image

image_size = [512,256,144,140,128,120,108,100,88,72,48,32,28]
def create_icon():
     for size in image_size:
          '''pri_image = Image.open("icon.png")
          pri_image.thumbnail((size,size))
          image_name = "icon_%d.png"%(size)
          pri_image.save(image_name)'''
          pri_image = Image.open("IMG_7321.jpg")
          pri_image.resize((size,size),Image.ANTIALIAS ).save("icom_%d.png"%(size))
if __name__ == "__main__":
     create_icon()

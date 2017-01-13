#! /usr/bin/env python
#coding=utf-8
import numpy as np

####三、创建数组

#数组的创建可通过转换列表实现，高维数组可通过转换嵌套列表实现
raw = [0,1,2,3,4]
a = np.array(raw)
print(a)


raw = [[0,1,2,3,4], [5,6,7,8,9]]
b = np.array(raw)
print(b)

#一些特殊的数组有特别定制的命令生成，如4*5的全零矩阵

d = (4, 5)
c = np.zeros(d)
print(c)

#[0, 1)区间的随机数数组

ra = np.random.rand(5)

print(ra)


####四、数组操作

a = np.array([[1.0, 2], [2, 4]])
print("a:", a)
b = np.array([[3.2, 1.5], [2.5, 4]])
print("b:", b)
print("\n\n\na+b:", a+b)


#类似C++，'+='、'-='、'*='、'/='操作符在NumPy中同样支持：

a /= 2
print('a = ', a)


#开根号求指数也很容易：
print ("a:", a)
print ("np.exp(a):", np.exp(a))
print ("np.sqrt(a):", np.sqrt(a))
print ("np.square(a):", np.square(a))
print ("np.power(a, 3):", np.power(a, 3))

#需要知道二维数组的最大最小值怎么办？想计算全部元素的和、
#按行求和、按列求和怎么办？for循环吗？不，NumPy的ndarray类已经做好函数了：

a = np.arange(20).reshape(4,5)
print("a:" ,a)
print( "sum of all elements in a: " , str(a.sum()))
print( "maximum element in a: " , str(a.max()))
print ("minimum element in a: " , str(a.min()))
print ("maximum element in each row of a: " , str(a.max(axis=1)))
print ("minimum element in each column of a: " , str(a.min(axis=0)))

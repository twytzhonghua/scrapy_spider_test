# -*-coding:utf-8 -*-

import numpy as np
print(np.version.full_version)



#生成了一个一维数组a，从0开始，步长为1，长度为20

a = np.arange(20)

print(a)

print(type(a))

#通过函数"reshape"，我们可以重新构造一下这个数组，例如，我们可以构造一个4*5的二维数组
a = a.reshape(4, 5)
print(a)
print(type(a))

#构造更高维的也没问题:
a = a.reshape(2, 2, 5)
print(a)

#既然a是array，我们还可以调用array的函数进一步查看a的相关属性：
#   "ndim"查看维度；"shape"查看各维度的大小；
#   "size"查看全部的元素个数，等于各维度大小的乘积；
#   "dtype"可查看元素类型；"dsize"查看元素占位（bytes）大小。

ndim = a.ndim
shape = a.shape
size = a.size
dtype = a.dtype
#dsize = a.dsize

print('ndim =', ndim)
print('shape = ', shape)
print('size = ', size)
print('dtype = ', dtype)
#print('dsize =', dsize)



    

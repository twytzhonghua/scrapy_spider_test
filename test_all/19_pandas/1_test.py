#! /usr/bin/env python

import pandas as pd
import numpy as np
from pandas import Series, DataFrame


v = pd.__version__
print(v)


####二、Pandas数据结构：Series

#从一般意义上来讲，Series可以简单地被认为是一维的数组。Series和一维数组最主要的区别在于Series类型具有索引（index）
#，可以和另一个编程中常见的数据结构哈希（Hash）联系起来。
#
######2.1 创建Series
#
#创建一个Series的基本格式是s = Series(data, index=index, name=name)，以下给出几个创建Series的例子。首先我们从数组创建Series：
#

a = np.random.randn(5)
print ("a is an array:", a)
s = Series(a)
print("s is a Series:", s)

#a is an array:
#[-1.24962807 -0.85316907  0.13032511 -0.19088881  0.40475505]
#s is a Series:
#0   -1.249628
#1   -0.853169
#2    0.130325
#3   -0.190889
#4    0.404755
#dtype: float64

#可以在创建Series时添加index，并可使用Series.index查看具体的index。
#需要注意的一点是，当从数组创建Series时，若指定index，那么index长度要和data的长度一致：
s = Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print ('\n\n\n', s)
idx = s.index
print ('idx = ', idx)

# a   -1.992225
#b    0.362945
#c    0.589778
#d    0.869942
#e    0.729797
#dtype: float64
#idx =  Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

#创建Series的另一个可选项是name，可指定Series的名称，可用Series.name访问。
#在随后的DataFrame中，每一列的列名在该列被单独取出来时就成了Series的名称：
#

s = Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'], name='my_series')
print('\n\n\n s = ', s)
print('s.name = ', s.name)

#s =  a   -2.601097
#b    0.812920
#c    0.254129
#d   -2.218585
#e   -2.076525
#Name: my_series, dtype: float64
#s.name =  my_series


#Series还可以从字典（dict）创建：

d = {'a': 0., 'b': 1, 'c': 2}
print ("\n d is a dict:", d)
s = Series(d)
print ("s is a Series:", s)
#d is a dict: {'b': 1, 'c': 2, 'a': 0.0}
#s is a Series: a    0.0
#b    1.0
#c    2.0
#dtype: float64


#让我们来看看使用字典创建Series时指定index的情形（index长度不必和字典相同）：

s = Series(d, index=['b', 'c', 'd', 'a'])
print("s = ", s)
#s =  b    1.0
#c    2.0
#d    NaN
#a    0.0
#dtype: float64
#

#我们可以观察到两点：一是字典创建的Series，数据将按index的顺序重新排列；
#二是index长度可以和字典长度不一致，如果多了的话，
#pandas将自动为多余的index分配NaN（not a number，pandas中数据缺失的标准记号)，当然index少的话就截取部分的字典内容。

#如果数据就是一个单一的变量，如数字4，那么Series将重复这个变量：
s = Series(4., index=['a', 'b', 'c', 'd', 'e'])
print("s = ", s)
#s =  a    4.0
#b    4.0
#c    4.0
#d    4.0
#e    4.0
#dtype: float64




#####2.2 Series数据的访问

#访问Series数据可以和数组一样使用下标，也可以像字典一样使用索引，还可以使用一些条件过滤：
s = Series(np.random.randn(10),index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print('s = ', s)
#s =  a    0.044662
#b   -0.480988
#c   -1.111241
#d    1.437037
#e    0.262847
#f    0.080499
#g    0.012579
#h   -2.083167
#i   -1.390602
#j   -2.167402
#dtype: float64

print('s[0] = ', s[0])
print('s[:2] = ', s[:2])
#s[0] =  0.777895054606
#s[:2] =  a    0.777895
#b    1.230415
#dtype: float64

print('s[[2,0,4]] = ', s[[2,0,4]])
#s[[2,0,4]] =  c    0.612171
#a    0.777895
#e    0.466579
#dtype: float64

print('s[s > 0.5]] = ', s[s > 0.5])
#s[s > 0.5]] =  a    0.898001
#f    2.024091
#g    1.063020
#h    1.536762
#i    2.312618
#dtype: float64


####三、Pandas数据结构：DataFrame

#在使用DataFrame之前，我们说明一下DataFrame的特性。DataFrame是将数个Series按列合并而成的二维数据结构，
#每一列单独取出来是一个Series，这和SQL数据库中取出的数据是很类似的。所以，按列对一个DataFrame进行处理更为方便，
#用户在编程时注意培养按列构建数据的思维。DataFrame的优势在于可以方便地处理不同类型的列，
#因此，就不要考虑如何对一个全是浮点数的DataFrame求逆之类的问题了，处理这种问题还是把数据存成NumPy的matrix类型比较便利一些。

#####3.1 创建DataFrame

#首先来看如何从字典创建DataFrame。DataFrame是一个二维的数据结构，是多个Series的集合体。我们先创建一个值是Series的字典，并转换为DataFrame：
d = {'one': Series([1., 2., 3.], index=['a', 'b', 'c']), 'two': Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = DataFrame(d)
print('df = ' , df)
#df =     one  two
#a  1.0  1.0
#b  2.0  2.0
#c  3.0  3.0
#d  NaN  4.0
#

#可以指定所需的行和列，若字典中不含有对应的元素，则置为NaN：
df = DataFrame(d, index=['r', 'd', 'a'], columns=['two', 'three'])
print('df = ' , df)
#df =     two three
#r  NaN   NaN
#d  4.0   NaN
#a  1.0   NaN


#另一种创建DataFrame的方法十分有用，那就是使用concat函数基于Serie或者DataFrame创建一个DataFrame
a = Series(range(5))
print('\na = ' , a)
b = Series(np.linspace(4, 20, 5))
print('\nb = ' , b)
df = pd.concat([a, b], axis=1)
print('df = ' , df)
#df =     0     1
#0  0   4.0
#1  1   8.0
#2  2  12.0
#3  3  16.0
#4  4  20.0

#下面这个例子展示了如何按行合并DataFrame成一个大的DataFrame：

df = DataFrame()
index = ['alpha', 'beta', 'gamma', 'delta', 'eta']
for i in range(5):
    a = DataFrame([np.linspace(i, 5*i, 5)], index=[index[i]])
    df = pd.concat([df, a], axis=0)
print('\ndf = ' , df)
#df =           0    1     2     3     4
#alpha  0.0  0.0   0.0   0.0   0.0
#beta   1.0  2.0   3.0   4.0   5.0
#gamma  2.0  4.0   6.0   8.0  10.0
#delta  3.0  6.0   9.0  12.0  15.0
#eta    4.0  8.0  12.0  16.0  20.0



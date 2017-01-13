#! /usr/bin/env python
#coding=utf-8
import numpy as np
import numpy.linalg as nlg

a = np.random.rand(2,4)
print ("a:", a)
a = np.transpose(a)
print ("a is an array, by using transpose(a):", a)
b = np.random.rand(2,4)
b = np.mat(b)
print ("b:", b)
print("b is a matrix, by using b.T:", b.T)

#a:
#[[ 0.17571282  0.98510461  0.94864387  0.50078988]
# [ 0.09457965  0.70251658  0.07134875  0.43780173]]
#a is an array, by using transpose(a):
#[[ 0.17571282  0.09457965]
# [ 0.98510461  0.70251658]
# [ 0.94864387  0.07134875]
# [ 0.50078988  0.43780173]]
#b:
#[[ 0.09653644  0.46123468  0.50117363  0.69752578]
# [ 0.60756723  0.44492537  0.05946373  0.4858369 ]]
#b is a matrix, by using b.T:
#[[ 0.09653644  0.60756723]
# [ 0.46123468  0.44492537]
# [ 0.50117363  0.05946373]
# [ 0.69752578  0.4858369 ]]

#
#矩阵求逆：



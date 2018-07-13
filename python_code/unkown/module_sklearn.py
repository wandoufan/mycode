# coding:utf-8

# 在进行机器学习时，经常需要打乱样本，
# 这种时候Python中有第三方库提供了这个功能——sklearn.utils.shuffle
# shuffle函数接收pandas中的DataFrame类型的数据，返回打乱后的数据

# sklearn中还提供著名的SVM算法

import pandas as pd
from pandas import Series
from pandas import DataFrame
from sklearn.utils import shuffle
from sklearn import svm


data = {'number':[9, 7, 4],
'color':['blue' ,'black' ,'red'],
'year':[2011,2008,2015]}

frame = DataFrame(data)
print(frame)
# shuffle函数接收pandas中的DataFrame类型的数据，返回打乱后的数据
frame = shuffle(frame)
print(frame)
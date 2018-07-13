# coding:utf-8

# pandas(Python Data Analysis Library)是基于numpy的用来进行数据分析的工具
# pandas包含了大量的库和数据模型，提供了处理大型数据集的函数和方法
# pandas兼具numpy高性能的数组计算功能和关系型数据灵活的数据处理功能


import pandas as pd# 惯例改名为pd
import numpy as np
# pandas中有两种独有的数据类型Series 和 DataFrame
from pandas import Series# 注意首字母是大写
from pandas import DataFrame# 注意首字母是大写

# -------------------------------------------------------------------------------

# Series是一种类似于一维数组的对象，它由一组数据(各种numpy数据类型)和一组与之相关的标签(索引)组成。
# Series对象是索引在左边，数值在右边，其中索引会自动创建

# 通过列表可以直接构造出Series对象
list_1 = [2,4,-6,7,]
s = Series(list_1)
print(s)
# values属性获取数值
print(s.values)
# index属性获取索引
print(s.index)
# 创建Series对象时可以自定义索引(索引可以是非数值的)，index参数指定索引
s = Series(list_1, index=['d','a','c','b'])
print(s)
# 可以通过索引选取Series对象的一个或一组值
print(s['d'])
print(s[['a','c','b']])
# 进行numpy数组运算(如根据布尔数据进行过滤，标量乘法，应用数学函数等)都会保留值和索引之间的链接
print(s[s>2])# 筛选出数组中值大于2的元素
print(s*2)# 将数组中的值都乘以2
print(np.exp(s))
# 把Series对象看做一个定长的有序字典，它是索引值(key)到数据值(value)的一个映射，可以代替字典类型参数
print('b' in s)
# 也可以用字典来创建Series对象，索引值对应key，数据值对应value
dict_1 = {'a':1,'c':-3,'f':9,'b':5}
s1 = Series(dict_1)
print(s1)
# 如果列表中值与字典中的键匹配，则显示在Series对象中
# 如果列表中值与字典中的键不匹配，则显示为NaN(not a number),即缺失数据
list_1 = ['c','d','f']
s1 = Series(dict_1, index=list_1)
print(s1)
# isnull和notnull方法可以用来检测数据缺失
print(s1.isnull())
print(s1.notnull())
# Series对象可以进行算术运算，不同的索引会自动对齐
dict_2 = {'x':4,'c':-5,'f':1,'y':1}
s2 = Series(dict_2)
print(s1)
print(s2)
print(s1+s2)
# Series对象本身及其索引都有一个name属性,可以设置并查看
print(s1.name)
print(s1.index.name)
# Series对象的索引可以通过赋值的方式直接修改
s1.index = ['a', 'b', 'c']
print(s1)

# ------------------------------------------------------------------------------

# DataFrame是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的数值类型
# DataFrame既有行索引又有列索引，可以看做是有Series组成的字典。
# DataFrame中的数据是以一个或多个二维块存放的(而不是列表，字典或其他的一维数据结构)

# 通过传入由等长列表或Numpy数组组成的字典来构造DataFrame,注意长度要相等
data = {'number':[9, 7, 4],
'color':['blue' ,'black' ,'red'],
'year':[2011,2008,2015]}
frame = DataFrame(data)
print(frame)
# 通过columns参数可以指定各个字段的排列顺序
frame = DataFrame(data, columns=['year', 'color', 'number'])
print(frame)
# 和Series对象一样，通过index参数可以自定义索引
# 如果传入的字段参数不存在会被标记为NaN，来表示数据缺失
frame = DataFrame(data,columns=['year', 'color', 'number', 'name'],
	index=['one', 'two', 'three'])
print(frame)
# DataFrame的columns属性和index属性分别可以查看字段和索引
print(frame.columns)
print(frame.index)
# 通过DataFrame的index属性可以直接指定索引的值
frame.index = ['one', 'two', 'three']
# 如果设置了columns和index的name属性，则name信息也会被显示出来
frame.columns.name = 'column'
frame.index.name = 'index'
print(frame)
# DataFrame的values属性可以返回一个包含所有数据的二维数组对象
print(frame.values)
print(type(frame.values))
# 通过类似获取字典中value的方式，可以将DataFrame的一列获取为一个Series对象
# 获取的Series对象的索引和DataFrame中一样，而且name属性也已经被设置了
s1 = frame['year']
print(s1)
# 也可以通过.ix方法指定索引值来将DataFrame的一行获取为一个Series对象
s2 = frame.ix['two']
print(s2)
# DataFrame的列/字段可以通过类似字典赋值的方式直接进行赋值
frame['name'] = ['Tom','Jreey','Jack']
print(frame)
# 也可以通过给列/字段赋值一个Series对象来进行赋值
s = Series([2011,2018,2008], index=['one','two','three'])
frame['year'] = s
print(frame)
# 为DataFrame赋值一个不存在的列会创建出这个新的列
frame['time'] = '20180711'
print(frame)
# del关键字通过类似字典类型的方式来删除列
del frame['time']
print(frame)
# 除了元素是列表的字典外，元素是字典的字典(即嵌套字典)也可以用来构造DataFrame
# 用外层字典的键来作为列/字段，内层字典的键来作为行/索引，相同的索引会自动合并
data = {'time':{1:2008,2:2011,3:2015},
'color':{4:'yellow',5:'blue',6:'red'},
'number':{4:3,5:-7,6:6}}
frame = DataFrame(data)
print(frame)
# DataFrame的T属性可以将列表进行转置
print(frame.T)
# 除了上面两种字典类型之外,还有多个其他类型的数据可以用来构造DataFrame
# lists/dicts/Series/DataFrame类型的数据都可以用来构造DataFrame
list_1 = ['a','b','c']
frame = DataFrame(list_1,columns=['column'])
print(frame)
#-------------------------------------------------------------------------------

# pandas的索引对象负责管理轴标签和其他元数据(比如轴名称等)
# 构建Series或DataFrame时，所用到的任何数组或其他序列的标签都会被转换为一个Index

# page 123

#---------------------------------------------------------------------------------

# 目前项目代码中实际用到的功能

# pandas.read_csv()函数经常被用来读取数据，返回一个DataFrame类型的结果
# pandas.read_csv()函数包含非常多的参数，常用参数有：
# filepath_or_buffer : 指定文件路径，路径URL可以是http, ftp, s3, 和 file.
# sep: 指定分割符，默认是','，C引擎不能自动检测分隔符，但Python解析引擎可以
frame = pd.read_csv('D:/test.csv')
frame.index = [4,5,6]
print(frame)

# DataFrame.head(n)函数查看前n行数据，如果不加n参数则显示全部数据
print(frame.head())
print(frame.head(1))
# DataFrame.tail(n)函数查看前n行数据，如果不加n参数则显示全部数据
print(frame.tail())
print(frame.tail(1))

# 查看DataFrame的长度,即行数/索引长度
print(len(frame))

# DataFrame.shape查看表格数据的长宽，返回一个元组，(行数,列数)
print(frame.shape)

print('-------------------------------------')
# DataFrame.iloc[param1][param2]查看具体的某个数值
# param1为索引值，param2为指定的字段
print(frame.iloc[2])
print(frame.iloc[2]['year'])
# coding:utf-8


# pickle模块可以将列表、字典等复杂的数据类型存储为文件

# 将所有python对象转换为二进制形式存放称为pickling，从二进制转换为对象称为unpickling
# 保存文件的后缀名可以随意，建议用pkl或pickle
# pickle模块和json模块类似，都有dumps,dump,loads,load等方法

import pickle


list1 = ['a', 'b', 'c', 1, 2]
dict1 = {'port': 80, 'name': 'Tom', 'yellow': 'black'}

#保存过程(保存至事先创建好的文件)
#'wb'表示二进制方式写
pickle_file = open('C:/Users/xyf/Documents/python 代码/test_10/pickle_file.txt','wb')
pickle.dump(list1,pickle_file)
pickle_file.close

#打开过程
#'rb'表示二进制方式读
pickle_file=open('C:/Users/xyf/Documents/python 代码/test_10/pickle_file.txt','rb')
list2=pickle.load(pickle_file)
print(list2)

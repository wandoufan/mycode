# coding:utf-8

# JSON（javascript object notation-JAVA对象标记）是一种轻量级的数据交换格式
# json模块就是提供这个数据格式转化功能的模块,类似的还有pickle模块。

# json模块序列化出来的是通用格式的字符串，其他编程语言都认识；
# pickle模块序列化出来的是二进制形式，只有python可以识别，但可以序列化函数；
# json模块提供了四个方法：dumps、dump、loads、load
# pickle模块提供了四个方法：dumps、dump、loads、load
# python对象和json对象的对应关系：
# dict-----object
# list,tuple-----array
# str-----string
# int,float-----number
# True-----true
# Flase-----flase
# None-----null

# dump和dumps都是序列化的方法，dumps只完成了序列化为str，dump必须传文件描述符 ，序列化+写文件
# load和loads都是反序列化方法，loads只完成了反序列化，load接收文件描述符，读文件+反序列化
# 注意：json.loads()方法的对象必须是经过json.dumps()方法处理过的数据，直接传入字符串或其他类型数据都会报错！

import json


list1 = ['a', 'b', 'c']
tupe1 = (1, 2, 3)
str1 = 'abcd'
dict1 = {'a': 1, 'b': 2, 'c': 3}

# 一、4种常用方法
# 1.dumps将列表序列化为json格式，注意：json串的类型就是字符串
j1 = json.dumps(list1)
print(j1, type(j1).__name__)

# 2.loads将json逆序列回list格式
data1 = json.loads(j1)
print(data1, type(data1).__name__)

# 3.dump将list1转化为json数据并写入json.txt文件中
with open('json.txt', 'w') as f:
    json.dump(list1, f)

# 4.load将数据从json.txt中读取并逆序列化为data2
with open('json.txt', 'r') as f:
    data2 = json.load(f)
print(data2)


# 二、注意事项
# 1.对于中文字符使用json.dumps()方法会有编码问题，输出的是ASCII码，不是真正的中文
chinese = json.dumps('这是中文')
print(chinese)

# 2.如果想输出真正的中文需要指定参数ensure_ascii=False
chinese = json.dumps('这是中文',ensure_ascii=False)
print(chinese)

# 3.对于post时得到的json或存有多种语言的json在loads时常会有格式错误
# 通过指定参数strict=False可以设定不严格检查json语法
# result = json.loads(json_type, strict=False)
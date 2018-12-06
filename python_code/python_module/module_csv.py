# coding:utf-8

# csv文件格式是一种通用的电子表格和数据库导入导出格式,csv模块就是提供这个数据格式转化功能的模块。
# CSV(Comma-Separated Values)即逗号分隔值，可以用Excel打开查看。由于是纯文本，任何编辑器也都可打开。
# 在CSV文件中，以,作为分隔符，分隔两个单元格。像这样a,,c表示单元格a和单元格c之间有个空白的单元格。依此类推。
# 与Excel文件不同，CSV文件中：值没有类型，所有值都是字符串;不能指定字体颜色等样式;
# 不能指定单元格的宽高，不能合并单元格;没有多个工作表;不能嵌入图像图表;


import csv
import sys

# list1 = ['a', 'b', 'c', 'd']
# list2 = ['x', 'y', 'z']

# 注意：CSV单行数据有大小限制，超过限制会报错_csv.Error: field larger than field limit (131072)
# 可以通过csv.field_size_limit修改大小限制
csv.field_size_limit(sys.maxsize)

# 读文件
#reader(csvfile, dialect='excel', **fmtparams)
# 第一个参数是可迭代的文件对象，第二个参数是编码风格，默认excel
# 第三个是格式化参数覆盖之前dialect对象指定的编码风格
# 也可以用参数encoding='utf-8'指定编码格式
# 注意：open函数中用'rt'/'wt'，即要用文本模式读写，也可以直接用'r/w'，用'rb'/'wb'会报错
with open('test.csv', 'rt') as csv_file:
    content = csv.reader(csv_file)
    for line in content:  # content 是'_csv.reader'类型的对象
        print(line)  # line是一个列表，包含表格中一行的数据


# 写文件
#writer(csvfile, dialect='excel', **fmtparams)
# 第一个参数是可迭代的文件对象，一般是句柄；第二个参数是编码风格，默认excel
# 第三个是格式化参数覆盖之前dialect对象指定的编码风格
# 也可以用参数encoding指定编码格式(ISO-8859-1/utf-8/gbk等)

list1 = ['one', 'bule', 3, '2008']
list2 = ['two', 'yellow', -7, '2011']
list3 = ['three', 'red', 6, '2015']

with open('D:/test.csv', 'wt') as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerow(list1)
    csv_writer.writerow(list2)
    csv_writer.writerow(list3)

# writerow方法是把数据一次写入一行(列表中每个元素占一列），writerows方法是把数据一次写入多行(列表中每个元素占一行)
# 注意：如果文件't.csv'事先存在，调用writer函数会先清空原文件中的文本，再执行writerow/writerows方法。

# 写文件时可以一次写入多行数据，而且每行包含多列元素
list1 = [['姓名', '性别', '班级'], ['张三', '男', '三班'], [
    '李四', '女', '一班'], ['王五', '', '二班'], ['', '', '四班']]
path = 'C:/mywork/a.csv'
# 注意：打开文件时设置参数newline=''，否则表格每两行之间会空一行
with open(path, 'w', newline='') as file:
    csv_writer = csv.writer(file, dialect='excel')
    csv_writer.writerows(list1)

# 注意：CSV格式的文件有可能调整编码格式或者修改后数据都会集中到第一列，可以用表格的分列功能处理

# 例子1：把列表中每一个词占一行写入列表中
list1 = ['翻炒', '抖音', '网红', '爆雷', '混动', '领投', 'HR', '哔哩']
path = 'C:/mywork/b.csv'

# 错误写法：每个词都是字符串格式的，会被按字分开放入一行的多列中
with open(path, 'w', newline='') as file:
    csv_writer = csv.writer(file, dialect='excel')
    csv_writer.writerows(list1)

# 正确写法：
with open(path, 'w', newline='') as file:
    csv_writer = csv.writer(file, dialect='excel')
    for word in list1:
        list2 = []
        list2.append(word)
        csv_writer.writerow(list2)

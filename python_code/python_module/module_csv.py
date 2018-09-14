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
# 注意：open函数中用'rt'/'wt'，即要用文本模式读写，用'rb'/'wb'会报错
with open('test.csv', 'rt') as csv_file:
    content = csv.reader(csv_file)
    for line in content:# content 是'_csv.reader'类型的对象
        print(line)# line是一个列表，包含表格中一行的数据


# 写文件
#writer(csvfile, dialect='excel', **fmtparams)
# 第一个参数是可迭代的文件对象，第二个参数是编码风格，默认excel
# 第三个是格式化参数覆盖之前dialect对象指定的编码风格
# 也可以用参数encoding='utf-8'指定编码格式

list1 = ['one','bule',3,'2008']
list2 = ['two','yellow',-7,'2011']
list3 = ['three','red',6,'2015']

with open('D:/test.csv', 'wt') as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerow(list1)
    csv_writer.writerow(list2)
    csv_writer.writerow(list3)

# writerow方法是把数据一次写入一行(列表中每个元素占一列），writerows方法是把数据一次写入多行(列表中每个元素占一行)
# 注意：如果文件't.csv'事先存在，调用writer函数会先清空原文件中的文本，再执行writerow/writerows方法。

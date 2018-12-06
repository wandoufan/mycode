# 关于文件操作的相关函数

import os

# 注意：如果想要创建新的文件夹需要用os.mkdir()方法
# 如果需要创建新文件,可以直接用open()函数,如果文件不存在就会自动创建一个新文件
# 例如：path为路径+文件名+文件格式,创建excel等其他格式文件也是同理
path = os.getcwd()+'train.log'+'.txt'
file = open(path,'w')
file.write('80')
file.close()

# 内置函数open()打开函数并返回文件对象/文件句柄
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True)
# file参数是文件名，如果不带路径会默认在当前文件夹寻找并打开
# mode参数指定文件打开模式
# encoding参数指定编码格式，常用encoding='utf-8'或encoding='gbk'或'gb18030'或'ISO-8859-1'
# F = open('test10.txt','r')#只读模式(默认)
# F = open('test10.txt','w')#覆盖写入
# F = open('test10.txt','x')#如果文件已存在，引发异常？？
# F = open('test10.txt','a')#末尾追加写入
# F = open('test10.txt','b')#二进制模式打开
# F = open('test10.txt','t')#文本模式打开(默认)
# F = open('test10.txt','+')#可读写模式打开
# F = open('test10.txt','u')#通用换行符支持


# 文件对象的方法
# f.close()  关闭文件
# f.read(size=-1)  从文件中读取size个字符，未给定size或给定负值时读取剩余所有字符，并返回字符串
# f.readlines()   从文件中读取一整行字符串,返回由每一行字符串为元素组成的列表
# f.write(str)   将字符串str写入文件
# f.write(str+'\n')  字符串按行写入文件中，每写入一次就换行
# f.writelines(seq)  向文件中写入字符串序列seq,seq应该是一个返回字符串的可迭代对象
# f.seek(offset,from)  指针在文件from位置(0代表文件起始位置，1代表当前位置，2代表文件末尾)移动offset个字节
# f.tell()   返回当前在文件中的位置

# 注意：关于'w'参数的覆盖写，在文件关闭前写入的东西都不会被覆盖，覆盖仅指文件打开关闭时！
list1 = ['w', 'x', 'y', 'z']
file = open('a.txt', 'w')
for i in list1:
    file.write('%s\n' % i)
file.close()

# 文件的写入操作，需要确保之前的打开模式有'w'或'a'
f = open('test10.txt', 'w', encoding='utf-8')# 打开文件时可以指定编码格式
f.write('123456789')
f.close()
f = open('test10.txt', 'a')
f.write('''
abcde
python
987654321
    ''')
f.close()

# 两种方法依次输出文本文件中的每一行
f = open('test10.txt', 'r')
# 1.通过f.readlines()方法获取列表
# 注意：尽量不要使用readlines()方法，因为readlines()方法会把文件都一次性读入内存中，性能比较差
# 尤其当文件很大时，打开文件会占用巨量内存
for line in f.readlines():
	print(line)
# 2.直接迭代读取文本文件中的每一行
for each_line in f:
    print(each_line)


# 打开绝对路径的文件，注意：文件路径要用反斜杠/
f = open('C:/Users/xyf/Documents/python 代码/test_10/test10.txt', 'r')
print(f.read())
print(f.tell())
f.seek(2, 0)
print(f.tell())
print(f.read(5))
print(f.tell())
f.seek(0, 0)
print(f.tell())

# 将文件的内容都放入列表中并输出出来
print(list(f))

# 读文件时常有编码错误，需要调整编码格式，解决该问题的样例(待研究chardet库？？)
if not os.path.isfile(file_name):
    logging.error('there is no file named %s, please check the path and input again!' % file_name)
    return None
else:
    import chardet
    f = open(file_name, 'rb')
    result = chardet.detect(f.readline())
    # print(result)
    file_encodes = 'utf-8'
    if 'utf' not in result['encoding']:
        file_encodes = 'gb18030'
    f.close()
    f = open(file_name, encoding=file_encodes)
    lines = f.readlines()
    f.close()
    text = ' '.join(lines)



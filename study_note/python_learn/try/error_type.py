# try-except结构支持的error类型

# Exception:所有的错误类型都可以用Exception来代替，即常见错误的基类

# AssertionError:断言语句失败
# assert关键字后边的条件为假时，程序将停止并返回AssertionError异常，一般用作测试程序的检查点
# list1 = [1, 2, 3]
# assert len(list1) > 3

# AttributeError:试图访问的对象属性不存在
# list1.abc()

# IndexError:索引超出序列范围
# print(list1[3])

# KeyError:字典查找一个不存在的关键字
# dict1 = {'port': 80, 'number': '3.14'}
# print(dict1['color'])

# NameError:试图访问一个不存在的变量
# print(list2)

# OSError:操作系统产生的异常，例如打开一个不存在的文件
# f=open('not_exist.txt','r')
# for each_line in f:
#    print(each_line)

# TypeError：不同类型数据间的无效操作
# a=1+'b'

# ZeroDivisionError:除数为零
# a=5/0

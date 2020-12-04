# 记录关于python语法相关的内容：


# 1.关于斜杠和转义的用法：
# 斜杠\表示转义，也可以表示代码本身的换行，用于代码太长时换行，可以直接忽略
list1 = [1, 2, 3, 4,\
         5, 6, 7, 8]
print(list1)
# 若字符串中本身含有一个\，则需要在前面再加一个\
string = "this is a \\"
# \n表示字符串换行，相当于空出一行
print('hi there,this a long message for you\
	that goes over multiple lines.. \nyou will find out soon that triple quotes in python allows this kind of fun!\n')
# \t表示tab，可以使字符串中间隔开一个tab的距离
print('关于特殊符号\t的解释')
# \r表示回车，相当于换行
print('!!!!\r????')

# 原始字符串操作符r或R来表示特殊字符
# 注意：使用r或R就可以输出特殊字符，其中r或R不会被输出
print(r'\nabc')  # 输出特殊字符

# python中可以在一行写多个语句，中间用分号;分开
a = '12345'; print(a)


# 2.python中字符串的单引号，双引号，三引号的区别：
# 单引号可以直接表示字符串，但遇到字符串包含单引号时必须使用转义符才能表示
s1 = 'let\'s go'
print(s1)
# 单引号中可以包含双引号
s2 = 'hello,"china",world'
print(s2)
# 双引号（注意是"，不是'')表示的字符串中可以包含单引号，即"let's go" 和'let\'s go'相同
s3 = "let's go"
print(s3)
# 三引号可以保持多行字符串的原有格式且不需要换号符\n，三引号中可以包含单引号和双引号
print('''
    锄禾日当午，
    '汗滴禾下土'
    "谁知盘中餐"
    粒粒皆辛苦。
    ''')


# 3.python中is和==的区别：
# Python中对象包含的三个基本要素，分别是：id(身份标识)、type(数据类型)和value(值)
# is和==都是对对象进行比较判断作用的，但对对象比较判断的内容并不相同
# is也被叫做同一性运算符，这个运算符比较判断的是对象间的唯一身份标识，也就是id是否相同
# 如果id相同，则表示是同一个对象，type和value也一定是相同的
# ==判断的是两个对象的值，即只需要判断value是否相同


# 4.python中交换两个对象的值：
# 也可以直接用a, b = b, a来实现
a = 1
b = 2
a, b = b, a
print(a, b)


# 5.python中的三元表达式(三元运算符)：
# 三元表达式在C或Java语言中是 条件表达式？表达式1：表达式2
# max = x > y ? x : y (注意这样的格式在python中不成立)
# Python中是  表达式1 条件表达式 表达式2
a = 1
b = 2
x=a if a > b else b
print(x)


# 6.关于赋值=的用法
# 合法用法：
x = y = z = 1
x += 1
print(x, y, z)
# 非法用法
# x = (y = z +1)


# 7.python中标识符(变量)的命名规范:
# python中的标识符可以由数字，字母，下划线组成，但不能以数字开头
# 标识符可以以下划线开头，如__init__
# python中的标识符区分字母大小写
# 用户定义的标识符不能和python内置的关键字重复


# 8.python的关键字
# 关键字是python中的保留字符，不能用作其他常数或标识符，关键字中只含小写字母
# 常见关键字包括：
# and   exec   not   assert   finally   or   break   for   pass   yield
# class   from   print   continue   global   raise   def   if   return
# del   import   try   elif   in   while   else   is   with   except   lambda


# 9.python中的比较运算符'>'和'<'

# 比较运算符可以进行连续比较，如果一个部分为假，则整个表达式为假
print(1 < 2 < 3)
print('x' < 'y' < 'z')

# 比较运算符的优先级高于逻辑运算符
print('a' > 'b' or 'c')
print('a' < 'b' or 'c')
print('a' > 'b' and 'c')
print('a' < 'b' and 'c')

# 比较运算符的优先级低于算术运算符
x = 1
y = 2
print(y > x + 1)

# 可以进行比较操作的对象包括：
print(1 < 2.0) # 数字和数字之间
print('axy' < 'zbc') # 字符串和字符串之间
print([1, 2, 3] < [3, 2, 1]) # 列表和列表之间
print((1, 2, 3) < (2, 1)) # 元组和元组之间
# 注意：字符串、元组、列表等序列类型的比较都是从第一个元素开始逐个进行比较的
# 如果前面元素都相等，则长度较长的序列更大

# 不可以进行比较操作的对象包括：
# print(3 > 'a') # 数字和字符串之间
# print(3 - 4j > 2 + 3j) # 复数和复数之间
# 记录关于python语法相关的内容：


# 1.关于斜杠和转义的用法：
# 引号表示注释，\n表示字符串换行
print('hi there,this a long message for you\
	that goes over multiple lines.. \nyou will find out soon that triple quotes in python allows this kind of fun!\n')
# 斜杠\表示转义，也可以表示代码本身的换行，用于代码太长时换行，可以直接忽略
list1 = [1, 2, 3, 4,\
         5, 6, 7, 8]
print(list1)
# 原始字符串操作符r/R来表示特殊字符
print(r'\n')  # 输出特殊字符
# \t表示tab，可以使字符串中间隔开一个tab的距离
print('关于特殊符号\t的解释')


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
# 三元表达式其他语言中是 条件表达式？表达式1：表达式2
# Python中是  表达式1 条件表达式 表达式2
a = 1
b = 2
x=a if a>b else b
print(x)
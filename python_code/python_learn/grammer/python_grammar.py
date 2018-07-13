# 记录关于python语法相关的内容：

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

# python中字符串的单引号，双引号，三引号的区别：
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
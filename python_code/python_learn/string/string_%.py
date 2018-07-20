# 常用字符串格式化符有%s,%d,%f;多个参数要用括号括起来
# 注意：字符串和%变量中间用空格隔开，没有逗号','
print('%s is a length of %d,circle is a number about %.2f' %('python', 5, 3.1415))

# 所有字符串格式化符号
print('%s is a sequence of string' %'abc')  # 转化为字符串
print('%c is a sequence of char' %97)  # 转化为字符
print('%d is a sequence of number' %-108)  # 转化为有符号十进制数
print('%u is a sequence of number' %-108)  # 转化为无符号十进制数
print('%o is a sequence of number' %108)  # 转化为无符号八进制数
print('%#o is a sequence of number' %108)  # 转化为无符号八进制数，#用来显示进制表示符
print('%#x is a sequence of number' %108)  # 转化为无符号十六进制数
print('%#X is a sequence of number' %108)  # 转化为无符号十六进制数
print('%.2f is a sequence of number' %3.1415926)  # 转化为精确到小数点后两位的浮点数
print('%e is a sequence of number' %108) # 转化为科学计数法

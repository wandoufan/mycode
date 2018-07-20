# 关于string函数的各种方法

str1 = 'abbbcdddde'
str2 = '12abc!* '
str3 = 'abcd1234'
str4 = '1234'
str5 = '0x1A'
str6 = 'ABCDEfgh'
str7 = '   '
str8 = '  begin    '
str9 = 'hello,world,python!'
# 把字符串里的所有字符都变为大写
print(str1.upper())

# 把字符串中所有的字母都变为小写
print(str6.lower())

# 将字符串首字母大写
print(str1.capitalize())

# 反转字符串中的大小写
print(str6.swapcase())

# 计算部分字符在字符串中出现的次数
print(str1.count('b'))

# 判断指定范围的字符串是否指定的关键字为开头
print(str1.startswith('a'))

# 判断指定范围的字符串是否以指定的关键字为结尾
print(str1.endswith('obj', 1, 6))
print(str1.endswith('e', 0, 20))

# 判断字符串中是否有指定的字符段，若有返回索引值，若没有返回-1
print(str1.find('c'))
print(str1.find('fg'))

# 判断字符串中是否包含指定字符段，最好直接用in来判断
print('a' in 'abcde')

# 类似string.find函数，若有返回索引值，若没有会报错
print(str1.index('c'))
# print(str1.index('f'))

# 若字符串仅由字母和数字构成，则返回Ture，否则返回False
print(str1.isalnum())
print(str2.isalnum())

# 若字符串仅由字母构成，则返回Ture，否则返回False
print(str1.isalpha())
print(str3.isalpha())

# 若字符串仅由数字构成，则返回Ture，否则返回False
print(str1.isdigit())
print(str4.isdigit())

# 若字符串仅由十进制数字构成，则返回Ture，否则返回False
print(str4.isdecimal())
print(str5.isdecimal())

# 若字符串仅由空格构成，则返回Ture，否则返回False
print(str7.isspace())

# 截掉字符串中左边的空格
print(str8.lstrip())

# 删除字符串右边的空格
print(str8.rstrip())

# str.strip([chars])删除字符串头尾指定的字符(默认为空格)
s1 = 'abcdcba'
s2 = s1.strip('a')
print(s2)

# 列表转化为字符串
# 用一个字符串当分隔符，将另外一个字符串的元素分隔开
list1 = ['a', 'b', 'c']
s1 = ''.join(list1)
# 把list中的元素按行输出
s2 = '\n'.join(list1)
print(s1, '\n', s2)
print(','.join(str4))
print(str4.join(str1))

# 字符串转化为列表
# split()函数可以将字符串切割并返回一个列表，默认分割符为空格
# 第一个参数指定分割符，第二个参数指定分割次数
stra = 'hello world everyone'
strb = '2018-05-01'
print(stra.split())
print(strb.split('-'))
print(strb.split('-', 1))

# 将字符串中指定的一部分用另一部分来代替，第三个参数指定替换次数
print(str1.replace('b', 'g', 2))
# 去除字符串中的空格
str1 = 'sdjf sdjkd   sd kfu'
str1 = str1.replace(' ', '')
print(str1)

# 返回标题化的字符串，即所有单词大写开头，其余字母小写
print(str9.title())

# 若字符串是title格式的，则返回Ture，否则返回False
print(str9.istitle())

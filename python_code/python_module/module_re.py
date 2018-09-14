# coding:utf-8

# 正则表达式(Regular Expression，在代码中常简写为regex、regexp、re或RE)
# 正则表达式用来检索、替换符合某个模式的文本;包括普通字符(如a到z之间的字母)和特殊字符(即'元字符')

# re模块是python中用来操作正则表达式的模块，提供查找，替换，分割的功能
import re


# 正则表达式匹配模式：
# 注意：正则式中匹配的目标字符既可以是中英文数字之类的字符，也可以是各种标点符号
# key :匹配所有包含key的字符串
# ^key :^表示匹配以key开头的字符串
# key$ :$表示匹配以Key结尾的字符串
# . :匹配除了换行符'\n'外的任意字符
# [k1k2k3] :表示包含若干字符的一组字符，依次匹配组内的每一个字符
# [^k1k2k3] :表示包含若干字符的一组字符，反向匹配除此之外的每一个字符
# [k1-k2] :表示字符范围，匹配范围内的任意一个字符；常用如[a-z],[0-9]等
# [^k1-k2] :表示字符范围，匹配除了范围内所有字符外的其他字符；
# 注意：对于下面的匹配规则，例如'ooo+'表示以oo开头，后边匹配多个o的字符串
# 注意：只有在'+'前面的最后一个o字符参与匹配多次，前两个o字符只表示以oo开头
# string* :*表示匹配前面字符串的最后一个字符零次或多次；不符合匹配的返回空字符串，而不是none；采用贪婪模式匹配，尽可能多的匹配
# 注意：匹配零次实际会匹配到文本中的每一个字符，但不符合正则规则的字符会返回为一个空字符串在列表中
# string+ :+表示匹配前面字符串的最后一个字符一次或多次；不符合匹配的返回none；采用贪婪模式匹配，尽可能多的匹配
# 注意：贪婪模式下会尽可能多的匹配连续多次符合正则规则的字符串，并统一返回为一个结果
# string? :?表示匹配前面字符串的最后一个字符零次或一次；采用非贪婪模式匹配，至多匹配到一个就算匹配成功
# 注意：非贪婪模式下每匹配到一段符合正则规则的字符串就立即返回一次结果
# re1|re2 :表示匹配任意一个子表达式，逻辑为或；例如，z|food匹配z或food，(z|f)ood匹配zood或food
# string{n} :表示匹配前面字符串的最后一个字符n次的字符串；采用非贪婪模式匹配；符合re规则但少于n次的不算匹配成功
# string{n,} :表示匹配前面字符串的最后一个字符至少n次的字符串；采用贪婪模式匹配；re{1,}等价于re+；re{0,}等价于re*
# string{n,m} :表示匹配前面字符串的最后一个字符至少n次至多m次的字符串；采用贪婪模式匹配
# (re)：小括号标记一个子表达re的开始和结束的位置
# (?imx)re :表示启动i、m、x为三个可选标志，标志分别对应修饰符中的含义；例如，(?i)re表示让子表达式re匹配时不区分大小写
# (?-imx)re :表示关闭i、m、x为三个可选标志


# 特殊匹配符号：
# \s :匹配任何空白符，包括空格、制表符、回车符、换行符、换页符等，等价于[\t\n\r\f]
# \S :匹配任何非空白符
# \w :匹配所有的数字、英文字母、中文字符等字符
# \W :匹配所有的非字符符号，如逗号、句号、分号、括号等等
# \d :匹配所有的数字符号，等价于[0-9]
# \D :匹配所有的非数字符号，等价于[^0-9]
# \b :匹配一个字边界，即字与空格间的位置，可以用来判断是词结尾位置
# 注意：'er\b'可以匹配never中的er，但是不能匹配到very中的er
# \B :匹配非字边界，可以用来判断不是词结尾的位置
# 注意：'er\B'可以匹配very中的er，但是不能匹配到never中的er
# \t :匹配一个制表符tab
# \r :匹配一个回车符
# \n :匹配一个换行符
# \f :匹配一个换页符


# 修饰符用来在re.complie()方法中控制正则表达式的匹配模式：
# re.I 使匹配对大小写不敏感(默认区分大小写)，等价于(?i)re
# re.L 做本地化识别匹配
# re.M 多行匹配，影响^和$
# re.S 使匹配包括换行符在内的所有字符
# re.U 根据unicode字符集解析字符，影响\w,\W,\b,\B
# re.X 忽略空格和'#'后面的注释使匹配模式更容易被理解(并不能在匹配时跳过空格)


# 常用正则匹配式：
# [0-9] :匹配所有数字
# [a-z] :匹配所有小写英文字母
# [A-Z] :匹配所有大写英文字母
# [\u4E00-\u9FA5] :匹配所有中文字符


# 测试：
# str_1 = """welcome 欢迎 123 to 来到 456 beijing 北京 789 fd fod food foood fooood
# xz xyz xyyz xyyyz xyyyyz xyyyyyz"""
# str_1 = 'abcDE FGhijk'
# str_1 = 'abc低端人口'
str_1 = 'HelloPythonWorld'
# str_1 = 'hellopythonworld'
# str_1 = 'HELLOPYTHONWORLD'
# str_1 = 'NEVER hello'
pattern = re.compile(r"^[a-zA-Z]+$")
# pattern = re.compile(r"er\b")
result = pattern.findall(str_1)
print(result)
result = pattern.match(str_1)
print(result)
result = pattern.search(str_1)
print(result)


#    例子1：不区分大小写的匹配全英文片段(需要判断匹配到的长度和整个片段的长度是否一致)：
# (?i)^[a-z]+$
# re.compile(r"^[a-z]+$",re.I)
# ^[a-zA-Z]+$
# ^([a-z]|[A-Z])+$   为什么不行？？？
# ^([a-z]+|[A-Z]+)$  为什么不行？？？
#    例子2：匹配全大写英文或全小写英文片段(需要判断匹配到的长度和整个片段的长度是否一致)：
# ^[a-z]+|[A-Z]+$
#    例子3：判断文本是否是全英文文本(只有英语单词和空格):
# 如何匹配到'hello python world'中的每一个单词？？？
# re.compile(r"^([a-z]+)\b$", re.I)  为什么不行？？？
#    例子4：匹配文本中是否含有指定的多个词(不是单字)：
# re.search(r'公斤|千克|经济', text)

     
# Linux命令中使用正则表达式：
# 'grep "[a-z|周杰伦]" zhoujielun' 选取所有的小写英文字母和周杰伦

# ---------------------------------------------------------------------------

# # 1.re.match(pattern,string,flags=0)在字符串的起始位置匹配模式
# # 如果字符串的开头匹配不成功就返回none，匹配成功返回一个匹配对象
# # pattern参数为要匹配的正则表达式,注意表达式前要加特殊符号修饰符r
# # string参数为要匹配的字符串
# # flags参数用来设置正则表达式的修饰符，多个修饰符用'|'隔开
# str_1 = 'welcome 欢迎 123 to 来到 123 beijing 北京 123'
# result = re.match(r'[a-z]', str_1)
# print(result)
# # 匹配对象的group方法获得匹配到的值
# print(result.group())
# # 匹配对象的span方法获得匹配值的索引范围
# print(result.span())

# # 2.re.search(pattern,string,flags=0)扫描整个字符串并返回第一个成功的匹配
# # 如果字符串的所有地方都匹配不成功就返回none，匹配成功返回一个匹配对象
# # 所有参数和re.match()函数一致
# str_1 = 'welcome 欢迎 123 to 来到 123 beijing 北京 123'
# result = re.search(r'[0-9]', str_1)
# print(result)
# # 匹配对象的group方法获得匹配到的值
# print(result.group())
# # 匹配对象的span方法获得匹配值的索引范围
# print(result.span())

# # 3.re.sub(pattern,repl,string,count=0)用于替换字符串中所有满足的匹配项
# # pattern参数为要匹配的正则表达式,注意表达式前要加特殊符号修饰符r
# # repl参数为要替换的新的字符串，也可以是一个函数
# # string参数为要被替换的原始字符串
# # count参数为模式匹配后要替换的次数，默认0表示不限次数替换所有
# str_1 = 'welcome 欢迎 123 to 来到 123 beijing 北京 123'
# string = re.sub(r'\s', '', str_1)
# print(string) 
# # 特别的，当repl参数为函数时？？？
# # string = re.sub(r'(?P<value>\d+)', '', str_1)
# # def double(matched):
# #     value = int(matched.group('value'))
# #     return str(value*2)
# # string = re.sub(r'[0-9]', double, str_1)
# # print(string)

# # 4.re.compile(pattern[,flags])用于编译正则表达式，返回一个正则表达式(pattern)对象
# # pattern对象有match()、search()、findall()、finditer()、split()、sub()等方法
# # pattern参数为要匹配的正则表达式,注意表达式前要加特殊符号修饰符r
# # flags参数用来设置正则表达式的修饰符，多个修饰符用'|'隔开
# str_2 = 'one 123 two 456 three 789'
# pattern = re.compile(r'[0-9]+', re.I)

# # 5.pattern.match(string[,pos[,endpos]])在字符串的起始位置匹配模式
# # 如果字符串的开头匹配不成功就返回none，匹配成功返回一个匹配对象
# # string参数为要进行匹配的字符串
# # pos参数为匹配开始的起始位置，可选参数，默认字符串开头
# # endpos参数为匹配结束的结束位置，可选参数，默认字符串结尾
# result = pattern.match(str_2, 4, 6)
# # 匹配对象的group方法获得匹配到的值
# print(result.group())
# # 匹配对象的span方法获得匹配值的索引范围
# print(result.span())

# # 6.pattern.search(string[,pos[,endpos]])扫描整个字符串并返回第一个成功的匹配
# # 如果字符串的所有地方都匹配不成功就返回none，匹配成功返回一个匹配对象
# # string参数为要进行匹配的字符串
# # pos参数为匹配开始的起始位置，可选参数，默认字符串开头
# # endpos参数为匹配结束的结束位置，可选参数，默认字符串结尾
# result = pattern.search(str_2, 9, 15)
# # 匹配对象的group方法获得匹配到的值
# print(result.group())
# # 匹配对象的span方法获得匹配值的索引范围
# print(result.span())

# # 7.pattern.findall(string[,pos[,endpos]])找到字符串中所有匹配的结果
# # 返回所有匹配成功的结果的列表，如果所有都没有匹配成功就返回一个空列表
# # string参数为要进行匹配的字符串
# # pos参数为匹配开始的起始位置，可选参数，默认字符串开头
# # endpos参数为匹配结束的结束位置，可选参数，默认字符串结尾
# result = pattern.findall(str_2)
# print(result)

# # 8.pattern.finditer(string[,pos[,endpos]])找到字符串中所有匹配的结果
# # 返回一个包含所有匹配成功的结果的迭代器
# # string参数为要进行匹配的字符串
# # pos参数为匹配开始的起始位置，可选参数，默认字符串开头
# # endpos参数为匹配结束的结束位置，可选参数，默认字符串结尾
# result = pattern.finditer(str_2)
# for num in result:
#     print(num.group())

# # 9.pattern.split(string[,maxsplit=0])用匹配结果分割字符串并将分割结果以列表形式返回
# # string参数为要被替换的原始字符串
# # maxsplit参数为要分割的次数，默认为0，不限制次数
# result = pattern.split(str_2)
# print(result)

# # 10.pattern.sub(repl,string,count=0)
# # repl参数为要替换的新的字符串，也可以是一个函数
# # string参数为要被替换的原始字符串
# # count参数为模式匹配后要替换的次数，默认0表示不限次数替换所有
# result = pattern.sub('', str_2)
# print(result)

# -------------------------------------------------------------------------------------
# 实际用到的项目
# 各种标点符号：
# pattern = re.compile('[\\s\\d,.<>/?:;\'\"[\\]{}()\\|~!@#$%^&*\\-_=+a-zA-Z，。《》、？：；“”‘’｛｝【】（）…￥！—┄－]+')
# doc = re.sub(pattern, ' ', doc)
# pred_label = re.sub(r'__label__', '', pred_labels[0][0])

# 匹配各种标点符号：
# pattern = re.compile(r'[*{}^……=%￥#@！!、,，。`;；？?_【】《》<>()（）~|&]+')
# text = pattern.sub(' ', text)
# pattern = re.compile('\[]')
# text = pattern.sub(' ', text)

# word = '奔驰S级'
# # 筛选出中文英文混合的词
# if re.search(r'[a-z][\u4E00-\u9FA5]|[A-Z][\u4E00-\u9FA5]|[\u4E00-\u9FA5][a-z]|[\u4E00-\u9FA5][A-Z]', word) is not None:
# 	print('yes')
# else:
# 	print('no')

# '^word'表示以word开头，'word$'表示以word结尾，在Linux命令中也可以直接使用
# 正则表达式可以直接在linux命令中使用，例如：
# 'grep -i [a-z] test1.txt' 选取test1.txt中所有包含英文字母的行

# 如何判断字符串中仅包含英文字母??
# def test(word):
#     is_english = 'yes'
#     for character in word:
#         if not bool(re.search(r'[a-z]|[A-Z]', character)):
#             is_english = 'no'
#     if is_english == 'yes':
#         return 'only by english'

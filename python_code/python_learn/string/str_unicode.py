# coding:utf-8

# 在python中，Unicode类型是作为编码的基础类型,即str--(encode)-->str(Unicode)--(decode)-->str
# 准确来说，Unicode不是编码格式，而是字符集。这个字符集包含了世界上目前所有的符号
# unicode可以解释世界上所有的文字，但是占用空间较大，如果确定使用对象都是中国人，可以用下面的国标编码来节省空间
# 在Unicode将所有字符的长度全部统一为16位，因此字符是定长的,例如：\u4f60\u597d\u4e2d\u56fd

# 常见编码格式：
# ASCII码是美国早期制定的编码规范，只能表示128个字符，包括英文字符、阿拉伯数字、西文字符以及32个控制字符。
# GB2312就是在ASCII基础上的简体汉字扩展,在重新编码的数字、标点、字母是两字节长的编码，这些称为“全角”字符；而原来在ASCII码表的127以下的称为“半角”字符。 
# GBK是对GB2312的进一步扩展,收录了21886个汉字和符号，完全兼容GB2312。
# GB18030收录了70244个汉字和字符，更加全面，与 GB 2312-1980 和 GBK 兼容。 
# UTF是在互联网上使用最广的一种Unicode的实现方式。我们最常用的是UTF-8，表示每次8个位传输数据

#unicode的字符串操作符u/U将标准字符串转换为完全的Unicode字符串对象
str1=u'hello'
print(type(str1).__name__)

# python字符串对象的encode方法可以指定编码格式，解决python中的中文出现乱码的问题
# encode(编码)和decode(解码)都是字符串的函数

# encode(encoding,errors)
# 第一个encoding参数指定编码格式，第二个errors参数可以指定不同的错误处理方案
# errors参数默认为'strict',即编码错误引起一个UnicodError; 其他可能得值有 'ignore', 'replace',
# 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。

code = '这是中文字符'
print(type(code))

# 用各种常见编码格式对字符串进行编码，获得bytes类型对象
str1 = code.encode('gb2312')
print(str1, type(str1))

str2 = code.encode('gbk')
print(str2, type(str2))

str3 = code.encode('utf-8')
print(str3, type(str3))

# 用decode进行解码,注意解码方式要与编码方式一致，否则会报错
code1 = str1.decode('gb2312')
print(code1, type(code1))

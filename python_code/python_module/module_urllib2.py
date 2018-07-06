# coding:utf-8

# urllib2模块提供URL相关的功能，它提供了非常简单的借口用来抓取各种协议的URL
# urllib2模块可以简单的看做urllib模块的升级版

# urllib2模块和request模块二者功能非常接近，区别是：
# request模块是基于urllib3的，urllib模块是python的内置模块，而request模块是第三方的模块

# 注意：直接导入urllib2模块会报错，目前先用urllib
# urlllib已经被细分为四个模块：request,error,parse,robotparser
from urllib import request# 用来打开和读取url
from urllib import error# 包含由url.request产生的异常
from urllib import parse# 提供url解析和url引用的功能
from urllib import robotparser# 专门用来解析robots.txt文件


# 1.request模块提供的常用函数：

# urlopen(url[, data[, timeout[, cafile[, capath[, cadefault[, context]]]]])
# 打开一个url对象，或者string对象，或者request对象
url = 'https://www.baidu.com'
response = request.urlopen(url)
print(type(response))
# 返回请求的结果
print(response.reason)
# 返回请求状态码
print(response.code)
print(response.getcode())
# 返回对象的URL路径
print(response.url)
print(response.geturl())
# 返回网页基本信息
# print(response.info())
# 返回网页的内容，注意不加编码格式会产生乱码
print(response.read().decode('utf-8'))


# 2.error模块提供的常用函数：
# .......


# 3.parse模块提供的常用函数：

# parse.urljoin将一个基本的相对路径url和另一个url结合组成一个完成的绝对路径url
# parse.urljoin(base, url, allow_fragments=True)
newurl = parse.urljoin('https://movie.douban.com', 'subject/5964718/?from=top250')
print(newurl)

# parse.urlparse对url路径进行解析，返回一个包含6个元素的元组，包括：
# 协议/scheme,域名/netloc,路径/path,路径参数/params,查询参数/query,片段/fragment
# parse.urlparse(urlstring, scheme='', allow_fragments=True)
parse_result = parse.urlparse('https://movie.douban.com/subject/5964718/;path_params?from=top250#fragment_params')
print(parse_result)
# 还可以继续对username,password,hostname,port进行进一步解析,前提是url中包含这些信息
print(parse_result.username)

# parse.urlsplit也可以对url进行解析，和parse.urlparse不同是：会把路径和路径参数连在一起
# parse.urlsplit(urlstring, scheme='', allow_fragments=True)
split_result = parse.urlsplit('https://movie.douban.com/subject/5964718/;path_params?from=top250#fragment_params')
print(split_result)

# parse.parse_qs对查询参数进行解析,返回一个包含键值对的字典
# parse.parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace')
# parse.parse_qsl对查询参数进行解析,返回一个元素为元组的列表
# parse.parse_qsl(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace')
# qs就是query string，即url地址中最后边的查询参数部分
query = 'Id=123&type=test1%2Ctest2%2Ctest3&Date1=2018-03-25&Date2=2018-04-26'
print(parse.parse_qs(query))
print(parse.parse_qsl(query))

# parse.urlencode与parse.parse_qs相反，可以将一个字典转换成合法的查询参数
# parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus)
dict1 = {'Id': ['123'], 'type': ['test1,test2,test3'], 'Date1': ['2018-03-25'], 'Date2': ['2018-04-26']}
query = parse.urlencode(dict1)
print(query)

# 下面四个函数分别用于url路径进行编码和解码
print(parse.quote('a&b/c+d'))# 除了斜线外都进行编码
print(parse.quote_plus('a&b/c+d'))# 包括斜线在内都进行编码
print(parse.unquote('a+b'))# 加号不进行解码
print(parse.unquote_plus('a+b'))# 加号解码为空格


# 4.robotparser模块提供的常用函数：
# ......
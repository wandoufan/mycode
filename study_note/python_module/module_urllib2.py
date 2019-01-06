# coding:utf-8

# urllib2模块提供URL相关的功能，它提供了非常简单的借口用来抓取各种协议的URL
# urllib2模块可以简单的看做urllib模块的升级版
# 参考资料：
# https://docs.python.org/3/library/urllib.request.html#module-urllib.request

# urllib2模块和request模块二者功能非常接近，区别是：
# request模块是基于urllib3的，urllib模块是python的内置模块，而request模块是第三方的模块

# 注意：直接导入urllib2模块会报错，目前先用urllib
# urlllib已经被细分为四个模块：request,error,parse,robotparser
from urllib import request# 用来打开和读取url
from urllib import error# 包含由url.request产生的异常
from urllib import parse# 提供url解析和url引用的功能
from urllib import robotparser# 专门用来解析robots.txt文件


# 一.request模块提供的常用函数：
# 备注：request模块使用http1.1协议，在请求体的请求头部中包含了'Connection:close'(取消持久连接)

# 1.urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
# urlopen()方法打开一个url对象或string对象或request对象，并返回一个响应体
# data参数以字典格式指定请求数据，当data参数非空值时，http会执行post请求方法而不是get请求方法
# 注意：data一定要是bytes对象，dict需要用parse.urlencode方法进行处理
# 注意：传递请求数据{start:200, filter:None}后使用的是post方法，因此请求数据是不会显示在url中的
# 因此response.url仍然是'https://movie.douban.com'，但实际上已经访问到了'https://movie.douban.com/top250?start=200&filter='
# timeout参数用于自定义超时时间，如果没有指定，会采用默认超时时间
url = 'https://www.baidu.com'
response = request.urlopen(url)
# 响应体有如下几种方法属性：
print(type(response))
# 返回请求的结果(请求成功是OK)
print(response.reason)
# 返回请求状态码(请求成功是200)
print(response.code)
print(response.getcode())
# 返回对象的URL路径
print(response.url)
print(response.geturl())
# 返回网页基本信息，即响应体中的消息报头部分
print(response.info())
# 返回网页的内容，注意不加编码格式会产生乱码
print(response.read().decode('utf-8'))

# 2.urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
# Request类提供抽象的url请求，它相比urlopen方法功能更加全面，可以自己添加请求头部header信息
# data参数以字典格式指定请求数据，当data参数非空值时，http会执行post请求方法而不是get请求方法
# 备注：一个参数有多个值时，多个值可以放入一个列表中
# header参数接收字典格式的请求头部数据，用于将脚本伪装成浏览器来欺骗http服务器
dict1 = {'Id': '123', 'type': ['test1,test2,test3'], 'Date1': '2018-03-25', 'Date2': '2018-04-26'}
my_dict = parse.urlencode(dict1).encode('utf-8')
my_headers = {  
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }  
request_class = request.Request(url, data=my_dict, headers=my_headers)
response = request.urlopen(request_class)
# 备注：最后得到的响应体和上面类型一致，有相同的方法属性


# 二.error模块提供的常用函数：
# .......


# 三.parse模块提供的常用函数：

# 1.parse.urljoin将一个基本的相对路径url和另一个url结合组成一个完成的绝对路径url
# parse.urljoin(base, url, allow_fragments=True)
newurl = parse.urljoin('https://movie.douban.com', 'subject/5964718/?from=top250')
print(newurl)

# 2.parse.urlparse对url路径进行解析，返回一个包含6个元素的元组，包括：
# 协议/scheme,域名(含端口)/netloc,资源路径/path,路径参数/params,查询参数/query,锚部分/fragment
# parse.urlparse(urlstring, scheme='', allow_fragments=True)
parse_result = parse.urlparse('https://movie.douban.com/subject/5964718/;path_params?from=top250#fragment_params')
print(parse_result)
# 还可以继续对username,password,hostname,port进行进一步解析,前提是url中包含这些信息
print(parse_result.username)

# 3.parse.urlsplit也可以对url进行解析，和parse.urlparse不同是：会把路径和路径参数连在一起
# parse.urlsplit(urlstring, scheme='', allow_fragments=True)
split_result = parse.urlsplit('https://movie.douban.com/subject/5964718/;path_params?from=top250#fragment_params')
print(split_result)

# 4.parse.parse_qs对查询参数进行解析,返回一个包含键值对的字典
# parse.parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace')
# 备注：qs就是query string，即url地址中最后边的查询参数部分
query = 'Id=123&type=test1%2Ctest2%2Ctest3&Date1=2018-03-25&Date2=2018-04-26'
print(parse.parse_qs(query))

# 5.parse.parse_qsl对查询参数进行解析,返回一个元素为元组的列表
# parse.parse_qsl(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace')
# 备注：qs就是query string，即url地址中最后边的查询参数部分
query = 'Id=123&type=test1%2Ctest2%2Ctest3&Date1=2018-03-25&Date2=2018-04-26'
print(parse.parse_qsl(query))

# 6.parse.urlencode与parse.parse_qs相反，可以将一个字典转换成合法的查询参数
# 注意：如果要提交的请求字典需要为bytes(字节)类型，必须先用urlencode方法进行编码
# parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus)
dict1 = {'Id': ['123'], 'type': ['test1,test2,test3'], 'Date1': ['2018-03-25'], 'Date2': ['2018-04-26']}
query = parse.urlencode(dict1).encode('utf-8')
print(query)

# 7.下面四个函数分别用于url路径进行编码和解码
print(parse.quote('a&b/c+d'))# 除了斜线外都进行编码
print(parse.quote_plus('a&b/c+d'))# 包括斜线在内都进行编码
print(parse.unquote('a+b'))# 加号不进行解码
print(parse.unquote_plus('a+b'))# 加号解码为空格


# 四.robotparser模块提供的常用函数：
# ......
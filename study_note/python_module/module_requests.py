# coding:utf-8

# requests模块是基于urllib3的第三方库，提供了http协议中对指定url资源的各种操作功能。
# urllib模块和requests模块二者功能非常接近，但urllib是官方自带的模块。
# 一般HTTP请求提交数据，需要编码成URL编码格式，然后作为url的一部分，或者作为参数传到Request对象中。
# 参考资料：
# http://docs.python-requests.org/zh_CN/latest/user/quickstart.html

# Requests 完全满足今日 web 的需求，提供的功能包括：Keep-Alive & 连接池；国际化域名和 URL；
# 带持久 Cookie 的会话；浏览器式的 SSL 认证；自动内容解码；基本/摘要式的身份认证；
# 优雅的 key/value Cookie；自动解压；Unicode 响应体；HTTP(S) 代理支持；文件分块上传；
# 流下载；连接超时；分块请求；支持 .netrc；

# HTTP协议中指定了八种方法/动作来表明对指定URL资源的不同操作方式 ：
# 1.POST(改)：向指定的资源提交数据进行处理请求（例如提交表单或者上传文件），数据被包含在请求体中，post请求可能会导致新资源的创建或者已有资源的修改。
# 2.GET(查)：向特定的资源发出请求。
# 3.PUT(增)：向指定的资源位置上传其最新内容。
# 4.DELETE(删)：请求服务器删除request_url所标识的资源。
# 5.HEAD：和GET一样向服务器请求资源，不过响应体不会被返回。可以在不必传输整个相应内容的情况下，单独获得响应消息头中的信息。
# 6.TRACE：追踪服务器收到的请求，主要用于测试或诊断。
# 7.OPTIONS：返回服务器对特定资源所支持的HTTP请求方法，也可以利用向web服务器发送'*'的请求来测试服务器的功能性。
# 8.CONNECT：HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。

import requests


# 1.发送http请求：
# 可以通过requests库的多个http方法来获取一个requests.models.Response类型的对象
# 这个对象就是web服务器返回的响应消息，包含我们需要的各种数据
r1 = requests.get('https://www.baidu.com')
r2 = requests.post('https://www.baidu.com', data={'key': 'value'})
r3 = requests.put('https://www.baidu.com', data={'key': 'value'})
r4 = requests.delete('https://www.baidu.com')
r5 = requests.head('https://www.baidu.com')
r6 = requests.options('https://www.baidu.com')


# 2.设置查询参数：
# params参数接收字典格式的请求数据/请求参数/查询参数
my_params = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': None, 'key4': ['value3', 'value4']
}
r = requests.get("https://www.baidu.com", params=my_params)
# 每个参数可以支持多个值，当一个参数有多个值时，多个值可以放入一个列表中
# 注意：值为None的键不会被添加到URL的查询字符串里


# 3.设置请求头部header：
# header参数接收字典格式的请求头部数据，用于将脚本伪装成浏览器来欺骗http服务器
# 注意: 定制头部header的优先级低于某些特定的信息源，即自行设置的参数不一定都能生效
my_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
r = requests.get('https://movie.douban.com/chart', headers=my_headers)


# 4.设置cookie
# cookies参数接收字典格式的cookie数据
my_cookies = {
    'username': 'test',
    'password': '000000'
}
r = requests.get('https://movie.douban.com/chart', cookies=my_cookies)


# 5.设置超时时间
# timeout参数接收以秒计数的数字，requests在超过设定时间后就停止等待响应
# 注意：timeout参数仅针对连接过程，在连接后下载响应内容的时间不受timeout的影响
r = requests.get('https://movie.douban.com/chart', timeout=0.5)


# 4.获取响应消息：
r = requests.get('https://movie.douban.com/chart')
# 响应对象包含以下属性：
# 获取对象的url
print(r.url)
# 获取对象的状态码
print(r.status_code)
# 获取请求错误的具体原因(仅当状态码为4xx或5xx的情况)
print(r.raise_for_status())
# 获取编码格式
print(r.encoding)
# 设置编码格式
r.encoding = 'ISO-8859-1'
# 获取响应的消息报头(返回一个字典结构)
print(r.headers)
print(r.headers['Date'])
# 获取响应中cookie(返回一个字典结构)
print(r.cookies)
print(r.cookies['bid'])
# 获取对象的响应内容
# print(r.text)
# 获取二进制的响应内容
# print(r.content)
# requests中有一个内置的json解码器，用来处理json数据
# print(r.json())


# 5.原始响应内容：
# 如果想获取来自服务器的原始套接字响应，需要提前在请求中把关键字stream置为True
r = requests.get('https://movie.douban.com/chart', stream=True)
print(r.raw)
print(r.raw.read(10))
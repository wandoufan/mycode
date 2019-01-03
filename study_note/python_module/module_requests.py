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


# 2.传递url查询参数：
# requests库的请求方法可以通过params关键字参数以字典格式来指定请求数据/请求参数/查询参数
dict1 = {'key1': 'value1', 'key2': 'value2',
         'key3': None, 'key4': ['value3', 'value4']}
r7 = requests.get("https://www.baidu.com", params=dict1)
# 每个参数可以支持多个值，将每个值加入列表结构中即可
# 注意：值为None的键不会被添加到URL的查询字符串里
print(r7.url)


# 3.获取响应消息：
# 响应对象包含以下属性：
# url属性
# ....

# r是返回的请求的状态码
r8 = requests.get('https://movie.douban.com/chart')
# 通过r.text读取服务器响应的内容
# 响应内容是str格式的，相当于网页源码的内容，可以进一步进行分割处理
print(r8.text)
# 通过r.encoding获得/修改编码格式
print(r8.encoding)
r8.encoding = 'ISO-8859-1'
# 对于非文本内容，r.content可以以字节形式获取二进制的响应内容
print(r8.content)
# 通过r.json读取服务器响应的内容
# requests内置了json解码器，r.json处理json数据
# print(r8.json())


# 原始响应内容：
# 如果想获取来自服务器的原始套接字响应，可以访问r.raw,需要在请求中把关键字stream置为True
# r9 = requests.get('https://movie.douban.com/chart', stream=True)
# print(r9.raw)
# print(r9.raw.read(10))


# 定制请求头：
# 如果想为请求添加HTTP头部，传递一个字典给headers参数即可
# dict2 = {'user-agent': 'my-app/0.0.1'}
# r1 = requests.get('https://api.github.com/some/endpoint', headers=dict2)
# print(r1.url)

# ---------------------------------------------------------------------------------------------
# 例子1：传送文本内容作为参数，并输出返回结果

# import requests
# import json

# file_path = 'C:/mywork/yunfu/nlp_project/discover_new_word/测试数据/zhoujielun.txt'

# with open(file_path, 'r', encoding='utf-8') as f:
#     text = f.read()
# dict1 = {'text': text}
# r1 = requests.get('http://service.yunfutech.com:17889/discoverword', data=json.dumps(dict1))

# print(r1.url)
# print(type(r1.json))
# print(r1.json())
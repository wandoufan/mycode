# coding:utf-8

# requests模块是基于urllib3的第三方库，提供了http协议中对指定url资源的各种操作功能。
# urllib模块和requests模块二者功能非常接近，但urllib是官方自带的模块。
# 一般HTTP请求提交数据，需要编码成URL编码格式，然后作为url的一部分，或者作为参数传到Request对象中。

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


# 发送http类型的网络请求：
# 获取一个requests.models.Response类型的对象r1,我们可以从r1中获取所有我们想要到的信息
r1 = requests.get('https://api.github.com/events')
r2 = requests.post('http://httpbin.org/post', data={'key': 'value'})
r3 = requests.put('http://httpbin.org/put', data={'key': 'value'})
r4 = requests.delete('http://httpbin.org/delete')
r5 = requests.head('http://httpbin.org/get')
r6 = requests.options('http://httpbin.org/get')
print(type(r2))


# 传递url参数：
# 可以利用URL的查询字符串(query string)传递某种数据
# 如果手工构建URL，数据会以键/值对的形式放在一个问号后边，如http://httpbin.org/get?key=val
# requests可以通过params关键字参数以一个字符串字典的形式提供数据
dict1 = {'key1': 'value1', 'key2': 'value2',
         'key3': None, 'key4': ['value3', 'value4']}
r7 = requests.get("http://httpbin.org/get", params=dict1)
# 打印输出url，可以看到url已经自动被正确编码了，可以将一个列表作为值传递进去
# 注意：值为None的键不会被添加到URL的查询字符串里
print(r7.url)


# 响应内容：
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
# requests内置了json解码器，r.json处理json数据
print(r8.json())


# 原始响应内容：
# 如果想获取来自服务器的原始套接字响应，可以访问r.raw,需要在请求中把关键字stream置为True
r9 = requests.get('https://movie.douban.com/chart', stream=True)
print(r9.raw)
print(r9.raw.read(10))


# 定制请求头：
# 如果想为请求添加HTTP头部，传递一个字典给headers参数即可
dict2 = {'user-agent': 'my-app/0.0.1'}
r1 = requests.get('https://api.github.com/some/endpoint', headers=dict2)
print(r1.url)

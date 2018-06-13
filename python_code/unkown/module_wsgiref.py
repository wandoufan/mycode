# coding:utf-8


# wsgiref模块是用来实现WSGI标准的Python内置库,可以用做web应用,类似于socket模块
# wsgiref模块封装了socket服务端的代码，只留下一个调用的接口，可以将精力放在Web请求的逻辑处理中

# WSGI(Web Server Gateway Interface)是专门为Python语言制定的web服务器与应用程序之间的网关接口规范
# 只要一个服务器拥有一个实现了WSGI标准规范的模块（例如apache的mod_wsgi模块），那么任意的实现了WSGI规范的
# 应用程序都能与它进行交互。因此，WSGI也主要分为两个程序部分：服务器部分和应用程序部分。 

# wsgiref模块主要分为五个模块：simple_server， util， headers， handlers， validate。
# 其中最常用的时simple_server,它实现了一个简单的WSGI Server和WSGI Application

import wsgiref.simple_server

# make_server(host_ip,port,application)
httpd = wsgiref.simple_server.make_server()

httpd.serve_forever()


# 比较复杂，结合socket部分后期慢慢看 ？？？？
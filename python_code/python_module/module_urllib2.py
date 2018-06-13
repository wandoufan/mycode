#coding:utf-8

#urllib2模块用来URLs，它提供了非常简单的借口用来抓取各种协议的URLs
#urllib2模块可以简单的看做urllib模块的升级版
#在python3中urllib2模块已经被分割为了urllib.request和urllib.error两个模块

#urllib2模块和request模块的区别：
#request模块是基于urllib3的，urllib模块是python的内置模块，而request模块是第三方的模块


#import urllib2#直接导入urllib2模块会报错
import urllib.request
import urllib.error

url='https://www.baidu.com'

#urlopen(url[, data[, timeout[, cafile[, capath[, cadefault[, context]]]]])
#打开一个url对象，或者string对象，或者request对象
response=urllib.request.urlopen(url)
print(type(response))
#返回状态码
print(response.code)
print(response.getcode())
#返回对象的URL路径
print(response.url)
#返回网页基本信息
print(response.info())



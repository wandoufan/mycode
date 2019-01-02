#coding:utf-8

#lxml模块实现对xml文件和HTML文件的解析处理，用来使用xpath
#lxml模块不是python的内置模块，需要安装后使用

import lxml

import requests,queue

from lxml import etree

url='https://movie.douban.com/subject/1292052/'

data=requests.get(url).text

s=etree.HTML(data)

film=s.xpath('//*[@id="content"]/h1/span[1]/text()')
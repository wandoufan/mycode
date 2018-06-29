# encoding:utf-8

# 功能：爬取豆瓣上的单页电影目录，并将名字，时间，演员等组合输出出来

from urllib import request  # 用来打开和读取url
from urllib import error  # 包含由url.request产生的异常
from urllib import parse  # 用来解析url
from urllib import robotparser  # 专门用来解析robots.txt文件
import os
from bs4 import BeautifulSoup  # bs4就是Beautiful Soup 4
import requests


douban_url = 'https://movie.douban.com/chart'
response = requests.get(douban_url)
content = response.text
# 'html.parser'是指最常用的HTML解析器，属于python内置的标准库
soup = BeautifulSoup(content, 'html.parser')

movie_list = []
date_list = []
actor_list = []

# 通过唯一的id属性找到目标数据所在的div标签
# print(div_tag)div_tag = soup.select('#content')
# 通过唯一的id属性找到目标数据所在的div标签
div_tag = soup.select('div[id=content]')
# 进一步缩小范围
div_tag = soup.select('.article')[0]

# 电影名字都在a标签中
a_tags = div_tag.find_all('a')
for a_tag in a_tags:
    movie_name = a_tag.get('title')
    if movie_name != None:
        movie_list.append(movie_name)

# 电影日期和演员都在p标签中
p_tags = div_tag.find_all('p')
for p_tag in p_tags:
    if p_tag.text != '':
        info_list = p_tag.text.split('/')
        movie_date = ''
        for info in info_list:
            if '20' in info:
                movie_date = movie_date + '/' + info
        date_list.append(movie_date)

        movie_actor = ''
        for info in info_list:
            if '20' not in info:
                movie_actor = movie_actor + '/' + info
        actor_list.append(movie_actor)

for i, j, k in zip(movie_list, date_list, actor_list):
    print(i,j,k)
    print('------------------------------------------------------')

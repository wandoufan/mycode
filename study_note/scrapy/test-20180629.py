# encoding:utf-8


from urllib import request  # 用来打开和读取url
from urllib import error  # 包含由url.request产生的异常
from urllib import parse  # 用来解析url
from urllib import robotparser  # 专门用来解析robots.txt文件
import os
from bs4 import BeautifulSoup  # bs4就是Beautiful Soup 4
import requests
import csv
import re


title_list = ['movie', 'director', 'country', 'type', 'comment']
movie_list = []
date_list = []
actor_list = []
director_list = []
comment_list = []
country_list = []
type_list = []

douban_url = 'https://movie.douban.com/top250'
response = requests.get(douban_url)
content = response.text
# 'html.parser'是指最常用的HTML解析器，属于python内置的标准库
soup = BeautifulSoup(content, 'html.parser')


# for tag in soup.find_all(re.compile('^b')):
# 	print(tag.string)

# i = 1
# for tag in soup.find_all('p', class_ = ''):
# 	print(tag.get_text())
# 	print('---%d--------------------------' %i)
# 	i += 1


response = soup.select('span')
response = soup.select('.title')
response = soup.select('a#footer')
print(response)
print(len(response))




# def save_as_csv(data):
# 	with open('D:/douban.csv', 'a') as csv_file:
# 		csv_writer = csv.writer(csv_file)
# 		csv_writer.writerow(data)



# def douban():
# 	# 通过唯一的id属性找到目标数据所在的div标签
# 	div_tag = soup.select('div[id=content]')[0]
# 	# print(div_tag)
# 	# 电影名字在img标签中
# 	img_tags = div_tag.find_all('img')
# 	for img_tag in img_tags:
# 		movie_name = img_tag.get('alt')
# 		movie_list.append(movie_name)

# 	# 评价信息在span标签中
# 	span_tags = div_tag.select('span[class=inq]')
# 	for span_tag in span_tags:
# 		movie_comment = span_tag.text
# 		comment_list.append(movie_comment)

# 	# 其他信息都在p标签中
# 	p_tags =div_tag.select('p[class='']')
# 	for p_tag in p_tags:
# 		infos = p_tag.text.strip()
# 		start = infos.find('导演')
# 		start = start + 3
# 		end = infos.find('主演')
# 		director = infos[start:end].strip()
# 		director_list.append(director)

# 		infos = infos[end+3:].strip()
# 		info_list = infos.split('/')
# 		country = info_list[-2].strip()
# 		country_list.append(country)
# 		type_ = info_list[-1].strip()
# 		type_list.append(type_)

# 	for a,b,c,d,e in zip(movie_list,director_list,country_list,type_list,comment_list):
# 		list_1 = [a,b,c,d,e]
# 		save_as_csv(list_1)

# douban()
# encoding:utf-8


from urllib import request  # 用来打开和读取url
from urllib import error  # 包含由url.request产生的异常
from urllib import parse  # 用来解析url
from urllib import robotparser  # 专门用来解析robots.txt文件
import requests
from bs4 import BeautifulSoup  # bs4就是Beautiful Soup 4
import os
import csv
import re
import json
import pymysql
import time
import random


def parse_html(html, url_dict):
    """
    解析html数据，提取出电影名和每个电影单独的url
    """
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.select('div[class="pic"]')
    for tag in result:
        a_tag = tag.select('a')
        address = a_tag[0]['href']
        img_tag = tag.select('img')
        name = img_tag[0]['alt']
        url_dict[name] = address


def get_movie_info(movie_url):
    """
    获取单个电影的详细信息
    """
    info_dict = {}
    response = requests.get(movie_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    script_tag = soup.select('script[type="application/ld+json"]')[0]
    movie_info = json.loads(script_tag.string, strict=False)
    info_dict['url'] = movie_url
    info_dict['director'] = movie_info['director'][0]['name']
    info_dict['actor_list'] = [actor['name'] for actor in movie_info['actor']]
    info_dict['date'] = movie_info['datePublished']
    info_dict['description'] = movie_info['description']
    info_dict['score'] = movie_info['aggregateRating']['ratingValue']
    return info_dict


def get_all_movie(base_url):
    """
    获取所有的top250电影
    """
    movie_dict = {}  # 存放电影的详细信息
    url_dict = {}  # 存放所有电影及其url信息
    for i in range(10):
        my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        # my_headers = {'Accept': '*/*',
        #            'Accept-Language': 'en-US,en;q=0.8',
        #            'Cache-Control': 'max-age=0',
        #            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
        #            'Connection': 'keep-alive',
        #            'Host': 'www.douban.com'
        #            }
        if i == 0:
            response = requests.post(base_url, headers=my_headers)
            print(response.status_code)
            content = response.text
            parse_html(content, url_dict)
            time.sleep(random.uniform(1, 2))
        else:
            my_param = {}
            my_param['start'] = i * 25
            my_param['filter'] = None
            response = requests.post(base_url, params=my_param, headers=my_headers)
            print(response.status_code)
            content = response.text
            parse_html(content, url_dict)
            time.sleep(random.uniform(1, 2))

    print(len(url_dict))
    for name, movie_url in url_dict.items():
        print(name, movie_url)
        movie_dict[name] = get_movie_info(movie_url)
    return movie_dict


def store_sql(movie_dict):
    """
    将爬虫结果存入sql数据库中
    """
    host = '127.0.0.1'
    user = 'root'
    passwd = '000000'
    database = 'douban_movie'
    connection = pymysql.connect(host, user, passwd, database, port=3306)
    cursor = connection.cursor()
    cursor.execute('use douban_movie')



if __name__ == '__main__':
    base_url = 'https://movie.douban.com/top250'
    movie_dict = get_all_movie(base_url)






# --------三种请求方法-----------------------------------

# 1.使用urllib库进行请求，拼接url路径
# for i in range(10):
#     if i == 0:
#         response = request.urlopen(base_url)
#     else:
#         full_url = base_url + '?' + 'start=%s&filter=' %str(25 * i)
#         response = request.urlopen(full_url)

# 2.使用urllib库进行请求，传递data参数
# for i in range(10):
#     if i == 0:
#         response = request.urlopen(base_url)
#     else:
#         request_data = {'start': i * 25, filter: None}
#         my_data = parse.urlencode(request_data).encode('utf-8')
#         response = request.urlopen(base_url, data=my_data)

# 3. 使用requests库进行请求，传递data参数
# for i in range(10):
#     if i == 0:
#         response = requests.get(base_url)
#         content = response.text
#         parse_html(content, movie_dict)
#     else:
#         my_param = {}
#         my_param['start'] = i * 25
#         my_param['filter'] = None
#         response = requests.get(base_url, params=my_param)
#         content = response.text
#         parse_html(content, movie_dict)
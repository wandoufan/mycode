# encoding:utf-8
# 爬取boss直聘的北京地区的python岗位详细信息
import requests
from bs4 import BeautifulSoup  # bs4就是Beautiful Soup 4
import os
import csv
import re
import json
import pymysql
import time
import random


def get_description(job_id):
    """
    根据job_id打开每个工作的单独页面，并提取出岗位要求信息
    """
    pass

def parse_html(content):
    """
    解析html的内容，提取出有效信息
    """
    soup = BeautifulSoup(content, 'html.parser')
    tag_list = soup.select('div[class="job-primary"]')
    result_list = []
    for tag in tag_list:
        job_info = {}
        job_name = tag.select('div h3 a div')[0].string
        job_info['job_name'] = job_name
        salary = tag.select('div h3 a span')[0].string
        job_info['salary'] = salary
        location = tag.select('div p')[0].contents[0]
        job_info['location'] = location
        work_year = tag.select('div p')[0].contents[2]
        job_info['work_year'] = work_year
        education = tag.select('div p')[0].contents[4]
        job_info['education'] = education
        company = tag.select('div div h3 a')[0].string
        job_info['company'] = company

        trade = tag.select('div div p')[0].contents[0]
        job_info['trade'] = trade
        tmp_list = tag.select('div div p')[0].contents
        if len(tmp_list) == 5:
            staff_number = tmp_list[4]
            finance = tmp_list[2]
        elif len(tmp_list) == 3:
            staff_number = tmp_list[-1]
            finance = 'None'
        job_info['staff_number'] = staff_number
        job_info['finance'] = finance

        date = tag.select('div p')[2].string
        job_info['date'] = date
        hr = tag.select('div h3')[2].contents[1]
        job_info['hr'] = hr
        job_id = tag.select('div h3 a')[0].get('href') 
        job_info['job_id'] = job_id
        company_id = tag.select('div h3 a')[-1].get('href')
        job_info['company_id'] = company_id

        result_list.append(job_info)
    return result_list

def get_response(base_url):
    """
    获取每个url的响应体
    """
    result_list = []
    my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    for i in range(1, 11):
        my_param = {}
        my_param['query'] = 'python'
        my_param['page'] = '%s' %str(i)
        my_param['ka'] = 'page-%s' %str(i)
        response = requests.get(base_url, params=my_param, headers=my_headers)
        print(response.status_code)
        print(response.url)
        if response.status_code != 200:
            break
        content = response.text
        result_list.extend(parse_html(content))
        time.sleep(random.uniform(2, 3))
    return result_list

def store_sql():
    """
    把爬虫结果存入sql数据库中
    """
    pass


if __name__ == '__main__':
    result_list = []
    # first_url = 'https://www.zhipin.com/job_detail/?query=python&scity=101010100&industry=&position='
    # base_url = 'https://www.zhipin.com/c101010100/'
    # base_url = 'https://www.zhipin.com/c101010100/?query=python&ka=sel-salary-0'
    # base_url = 'https://www.zhipin.com/c101010100/y_1/?query=python&ka=sel-salary-1'
    # base_url = 'https://www.zhipin.com/c101010100/y_2/?query=python&ka=sel-salary-2'
    # base_url = 'https://www.zhipin.com/c101010100/y_3/?query=python&ka=sel-salary-3'
    # base_url = 'https://www.zhipin.com/c101010100/y_4/?query=python&page=3&ka=page-next'
    # base_url = 'https://www.zhipin.com/c101010100/y_8/?query=python&ka=sel-salary-8'

    # for i in range(1, 9):
    #     base_url = base_url = 'https://www.zhipin.com/c101010100/y_%s/' %str(i)
    #     print(base_url)
    #     result_list.extend(get_response(base_url))
    #     time.sleep(random.uniform(1, 2))
    # print('工作个数：', len(result_list))
    # for job in result_list:
    #     print(job, '\n')
    # with open('job_info2.text', 'w') as f:
    #     json.dump(result_list, f)


    with open('job_info.text', 'r') as f:
        result_list = json.load(f)

    with open('job_info2.text', 'r') as f:
        result_list2 = json.load(f)
    
    print('集合1工作数：', len(result_list))
    print('集合2工作数：', len(result_list2))

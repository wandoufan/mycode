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
    根据job_id打开每个工作的单独页面，并提取出岗位描述信息
    """
    base_url = 'https://www.zhipin.com'
    job_url = base_url + job_id
    my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    response = requests.get(job_url, headers=my_headers)
    print(response.status_code)
    print(response.url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    div_tag = soup.select('div[class="detail-content"]')[0]
    description = div_tag.select('div[class="text"]')[0].get_text().strip()
    return description

def parse_html(content):
    """
    解析html的内容，提取出有效工作岗位信息
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

        # description = get_description(job_id)
        # time.sleep(random.uniform(1, 2))
        # job_info['description'] = description

        result_list.append(job_info)
    return result_list

def get_response(base_url):
    """
    获取每个url的响应体
    """
    result_list = []
    my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    for i in range(1, 11):  # 爬取每个搜索结果的前十页的数据
        my_param = {}
        my_param['query'] = 'python'
        my_param['page'] = '%s' %str(i)
        my_param['ka'] = 'page-%s' %str(i)
        try:
            response = requests.get(base_url, params=my_param, headers=my_headers)
        except Exception as reason:
            print('错误原因：', reason)
            continue
        print(response.status_code)
        print(response.url)
        if response.status_code != 200:
            break
        content = response.text
        result_list.extend(parse_html(content))
        time.sleep(random.uniform(5, 6))
    return result_list

def store_sql(result_list):
    """
    把爬虫结果存入sql数据库中
    """
    host = '127.0.0.1'
    user = 'root'
    passwd = '000000'
    database = 'boss_job'
    connection = pymysql.connect(host, user, passwd, database, port=3306)
    cursor = connection.cursor()
    cursor.execute('use boss_job')
    for job_info in result_list:
        job_name = '"""' + job_info['job_name'] + '"""'
        salary = '"""' + job_info['salary'] + '"""'
        location = '"""' + job_info['location'] + '"""'
        work_year = '"""' + job_info['work_year'] + '"""'
        education = '"""' + job_info['education'] + '"""'
        company = '"""' + job_info['company'] + '"""'
        trade = '"""' + job_info['trade'] + '"""'
        staff_number = '"""' + job_info['staff_number'] + '"""'
        finance = '"""' + job_info['finance'] + '"""'
        date = '"""' + job_info['date'] + '"""'
        hr = '"""' + job_info['hr'] + '"""'
        job_id = '"""' + job_info['job_id'] + '"""'
        company_id = '"""' + job_info['company_id'] + '"""'

        command = 'insert job_info(job_name, salary, location, work_year, education, company, trade, staff_number, finance, date, hr, job_id, company_id) \
        values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)' %(job_name, salary, location, work_year, education, company, trade, staff_number, finance, date, hr, job_id, company_id)
        cursor.execute(command)
        connection.commit()


if __name__ == '__main__':
    result_list = []
    boss_url = 'https://www.zhipin.com/c101010100/'

    # for i in range(1, 7):
    #     base_url = 'https://www.zhipin.com/c101010100/y_%s/' %str(i)  # 不同的岗位薪资
    #     base_url = 'https://www.zhipin.com/c101010100/t_80%s/' %str(i)  # 不同的融资阶段
    #     base_url = 'https://www.zhipin.com/c101010100/s_30%s/' %str(i)  # 不同的公司规模
    #     print(base_url)
    #     result_list.extend(get_response(base_url))
    #     time.sleep(random.uniform(1, 2))

    for i in ['海淀区', '朝阳区', '东城区', '西城区', '丰台区', '大兴区', '通州区', '石景山区']:
        base_url = 'https://www.zhipin.com/c101010100/b_%s/' %i
        print(base_url)
        result_list.extend(get_response(base_url))
        time.sleep(random.uniform(1, 2))

    print('工作个数：', len(result_list))
    with open('job_info2.text', 'w') as f:
        json.dump(result_list, f)



    # ----------------------------------------------------
    # with open('job_info.text', 'r') as f:
    #     result_list1 = json.load(f)
    # print(len(result_list1))

    # with open('job_info2.text', 'r') as f:
    #     result_list2 = json.load(f)
    # print(len(result_list2))

    # job_id_list1 = [info['job_id'] for info in result_list1]
    # print(len(job_id_list1))
    # job_id_list2 = [info['job_id'] for info in result_list2]
    # print(len(job_id_list2))

    # tmp_list = [info for info in result_list2 if info['job_id'] not in job_id_list1]
    # print(len(tmp_list))
    # result_list1.extend(tmp_list)
    # print(len(result_list1))

    # job_id_list1 = [info['job_id'] for info in result_list1]
    # print(len(set(job_id_list1)))

    # with open('job_info.text', 'w') as f:
    #     json.dump(result_list1, f)


# encoding:utf-8
# 参考资料：
# https://blog.csdn.net/danspace1/article/details/80197106
# https://blog.csdn.net/asdd_1/article/details/78204175
# https://www.cnblogs.com/qiukujun/p/one_simple_spider.html


from urllib import request
from urllib import parse
import requests

# 拉钩网主页
base_url = 'https://www.lagou.com/'
# 拉钩网python搜索结果
python_url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='



my_headers = {  
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',  
    'Host':'www.lagou.com',  
    # 'Referer':'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',  
    'Referer':'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',  
    'X-Anit-Forge-Code':'0',  
    'X-Anit-Forge-Token': 'None',  
    'X-Requested-With':'XMLHttpRequest'  
    }  

my_data = {  
    'first': 'true',  
    'pn':1,  
    'kd':'python'}  

res = requests.post(base_url, headers = my_headers, data = my_data)  
res.raise_for_status()  
res.encoding = 'utf-8'  
# 得到包含职位信息的字典  
# page = res.json() 
print(res.text)


# response = request.urlopen(base_url)
# print(response)
# print(response.read().decode('utf-8'))
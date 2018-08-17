import requests
import json
import os


# file_path = 'C:/mywork/yunfu/nlp_project/discover_new_word/测试数据/zhoujielun.txt'
result_path = 'C:/mywork/yunfu/nlp_project/discover_new_word/科大讯飞74条语料测试结果'
for i in range(1,10):
    file_path = 'C:/mywork/yunfu/nlp_project/discover_new_word/测试数据/74条收录/collection_2-0%d.txt' %i
    file_name = os.path.basename(file_path)
    result_file = result_path + '/result_' + file_name
    with open(file_path, 'r') as f1:
        text = f1.read()
    dict1 = {'text': text}
    r1 = requests.get('http://service.yunfutech.com:17889/discoverword', data=json.dumps(dict1))
    result = str(r1.json())
    with open(result_file, 'w', encoding='utf-8') as f2:
        f2.write(result)

for i in range(10,75):
    file_path = 'C:/mywork/yunfu/nlp_project/discover_new_word/测试数据/74条收录/collection_2-%d.txt' %i
    file_name = os.path.basename(file_path)
    result_file = result_path + '/result_' + file_name
    with open(file_path, 'r') as f1:
        text = f1.read()
    dict1 = {'text': text}
    r1 = requests.get('http://service.yunfutech.com:17889/discoverword', data=json.dumps(dict1))
    result = str(r1.json())
    with open(result_file, 'w', encoding='utf-8') as f2:
        f2.write(result)


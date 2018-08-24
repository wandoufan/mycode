import requests
import json
import os


for i in range(1, 10):
    print('collection_0%d.txt' %i)
    file_path = 'C:/mywork/yunfu/nlp_project/discover_new_word/科大讯飞25条语料测试数据/collection_0%d.txt' %i
    keyword_path = 'C:/mywork/yunfu/nlp_project/discover_new_word/科大讯飞25条语料测试数据/collection_0%d_keywords.txt' %i
    keysegword_list = []
    with open(keyword_path, 'r', encoding='utf-8') as f1:
        for line in f1:
            line = line.strip()
            keysegword_list.append(line)
    print('提供的keyword列表：',keysegword_list)

    with open(file_path, 'r') as f1:
        text = f1.read()
    dict1 = {'text': text}
    # r1 = requests.get('http://service.yunfutech.com:17889/discoverword', data=json.dumps(dict1))
    r1 = requests.get('http://service.yunfutech.com/cws/ltp', data=json.dumps(dict1))
    result1 = r1.json()
    segword_list = []
    word_infos1 = result1['data']['words']
    for word_info in word_infos1:
        word = word_info['word']
        segword_list.append(word)
    # print(segword_list)

    r2 = requests.get('http://service.yunfutech.com/discoverword', data=json.dumps(dict1))
    result2 = r2.json()
    newword_list = []
    word_infos2 = result2['result']
    newword_list = list(word_infos2.keys())
    newword_list.remove('code')
    newword_list.remove('message')
    print('经过ltp分词过滤的发现新词结果：',newword_list)

    alist = []
    for keyword1 in keysegword_list:
        if keyword1 not in segword_list:
            alist.append(keyword1)
    # print('没有被ltp分词分出来的keyword：',alist)

    blist = []
    for keyword2 in alist:
        if keyword2 in newword_list:  
            blist.append(keyword2)
    # print('没有被ltp分词分出来且被新词发现识别的keyword:', blist)
    print('\n')    


for i in range(10, 26):
    print('collection_0%d.txt' %i)
    file_path = 'C:/mywork/yunfu/nlp_project/discover_new_word/科大讯飞25条语料测试数据/collection_%d.txt' %i
    keyword_path = 'C:/mywork/yunfu/nlp_project/discover_new_word/科大讯飞25条语料测试数据/collection_%d_keywords.txt' %i
    keysegword_list = []
    with open(keyword_path, 'r', encoding='utf-8') as f1:
        for line in f1:
            line = line.strip()
            keysegword_list.append(line)
    print('提供的keyword列表：',keysegword_list)

    with open(file_path, 'r') as f1:
        text = f1.read()
    dict1 = {'text': text}
    # r1 = requests.get('http://service.yunfutech.com:17889/discoverword', data=json.dumps(dict1))
    r1 = requests.get('http://service.yunfutech.com/cws/ltp', data=json.dumps(dict1))
    result1 = r1.json()
    segword_list = []
    word_infos1 = result1['data']['words']
    for word_info in word_infos1:
        word = word_info['word']
        segword_list.append(word)
    # print(segword_list)

    r2 = requests.get('http://service.yunfutech.com/discoverword', data=json.dumps(dict1))
    result2 = r2.json()
    # print(result2)
    newword_list = []
    word_infos2 = result2['result']
    newword_list = list(word_infos2.keys())
    newword_list.remove('code')
    newword_list.remove('message')
    print('经过ltp分词过滤的发现新词结果：',newword_list)

    alist = []
    for keyword in keysegword_list:
        if keyword not in segword_list:
            alist.append(keyword)
    # print('没有被ltp分词分出来的keyword：',alist)

    blist = []
    for keyword2 in alist:
        if keyword2 in newword_list:
            blist.append(keyword2)
    # print('没有被ltp分词分出来且被新词发现识别的keyword:', blist)
    print('\n')    



# file_path = 'C:/mywork/yunfu/nlp_project/discover_new_word/科大讯飞25条语料测试数据/collection_03.txt'
# keyword_path = 'C:/mywork/yunfu/nlp_project/discover_new_word/科大讯飞25条语料测试数据/collection_03_keywords.txt'
# keysegword_list = []
# with open(keyword_path, 'r', encoding='utf-8') as f1:
#     for line in f1:
#         line = line.strip()
#         keysegword_list.append(line)
# print(keysegword_list)

# with open(file_path, 'r') as f1:
#     text = f1.read()
# dict1 = {'text': text}
# # r1 = requests.get('http://service.yunfutech.com:17889/discoverword', data=json.dumps(dict1))
# r1 = requests.get('http://service.yunfutech.com:17889/cws/ltp', data=json.dumps(dict1))
# result = r1.json()
# segword_list = []
# word_infos = result['data']['words']
# for word_info in word_infos:
#     word = word_info['word']
#     print(word)
#     segword_list.append(word)

# print(segword_list) 

# for keyword in keysegword_list:
#     if keyword not in segword_list:
#         print('!!!!!!',keyword)  



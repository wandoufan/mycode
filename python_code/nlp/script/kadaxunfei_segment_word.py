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
    r1 = requests.get('http://service.yunfutech.com:17889/cws/ltp', data=json.dumps(dict1))
    result1 = r1.json()
    segword_list = []
    word_infos1 = result1['data']['words']
    for word_info in word_infos1:
        word = word_info['word']
        segword_list.append(word)
    # print(segword_list)

    r2 = requests.get('http://service.yunfutech.com:17889/discoverword', data=json.dumps(dict1))
    result2 = r2.json()
    # print(result2)
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
    print('没有被ltp分词分出来的keyword：',alist)

    blist = []
    for keyword2 in alist:
        if keyword2 in newword_list:  
            blist.append(keyword2)
    print('没有被ltp分词分出来且被新词发现识别的keyword:', blist)
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
    r1 = requests.get('http://service.yunfutech.com:17889/cws/ltp', data=json.dumps(dict1))
    result1 = r1.json()
    segword_list = []
    word_infos1 = result1['data']['words']
    for word_info in word_infos1:
        word = word_info['word']
        segword_list.append(word)
    # print(segword_list)

    r2 = requests.get('http://service.yunfutech.com:17889/discoverword', data=json.dumps(dict1))
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
    print('没有被ltp分词分出来的keyword：',alist)

    blist = []
    for keyword2 in alist:
        if keyword2 in newword_list:
            blist.append(keyword2)
    print('没有被ltp分词分出来且被新词发现识别的keyword:', blist)
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


# 1
# ['公司', '经纬', '创业', 'PR', '领域', 'AI', '行业', '财务', '融资', '创业者']
# 2
# ['人类', '主观', '宗教', '算法', '科学', '狒狒', '伦理', '量子物理', '生物', '香蕉']
# 3
# ['oTMS', '若琪', '物流', '客户', '货主', '公司', 'SaaS', '承运', '运输', '行业']
# 4
# ['人际关系', '曾国藩', '知识', '价值', '真诚', '皇帝', '人际', '思维', '忠臣', 'KMCenter']
# 5
# ['拉伸', '肌肉', '运动', '反射', '损伤', '瑜伽', '关节', '体式', '人体', '肌腱']
# 6
# ['CEO', '创业', 'Clean', 'Master', '猎豹', '公司', '资源', '执行力', '聚焦', '创业者']
# 7
# ['新城', 'XAXQ', '板块', '嘉定', '雄安', '大宁', '沪北', '上海', '新区', '市中心']
# 8
# ['加冕', '公司', '创始人', '突破', '组织', '华为', '君主立宪', '老板', '肖知兴', '强调']
# 9
# ['概念', '产业政策', '记忆', '知识', '语义', '模型', '田志刚', '微软亚洲研究院', '存储', '本质']
# 10
# ['亚马逊', 'FBA', '贝佐斯', '沃尔玛', '第三方', 'AWS', 'Amazon', 'UPS', '仓储', '客户']
# 11
# ['套路', '桥段', '框架', '包袱', '抽象', '三番', '提炼', '模型', '知识', '方法']
# 12
# ['SaaS', 'IT', '美国', 'Oracle', '公司', '经纬', '企业', '亿美元', '领域', '客户']
# 13
# ['客户', '协同', '曾鸣', '互动', '供应链', '互联网', '商业', '时代', '平台', '核心']
# 14
# ['孩子', '心理品质', '饼干', '规则', '生存', 'Momself', '李松蔚', '处分', '问题', '失控']
# 15
# ['饮料', '条件反射', '万亿美元', '可口可乐', '巴甫洛夫', '罗兹', '竞争对手', '心理学', '消费者', 'lollapalooza']
# 16
# ['拉马努金', '知识', 'NB', '领域', '实践', '王小波', '孙悟空', '田志刚', '印度', '数学']
# 17
# ['职场', '上司', '利益', '子君', '在职场', '成功者', '老板', '伪善', '失败者', '理想']
# 18
# ['电商', '阿里', '快消品', '批发市场', '京东', '渗透率', '传统', '毛利', '地方', '互联网']
# 19
# ['知识', '体系', '领域', '实践', '建立', '掌握', '学习', '关联', '概念', '转化成']
# 20
# ['晨型人', '作息', 'Lipnevich', 'eveningness', 'Horne', '夜行人', 'morningness', '研究', '认知', '早起']
# 21
# ['徐邦达', '书画', '知识', '实践', '多隆', '学习', '真迹', '故宫博物院', '合伙人', '干活']
# 22
# ['拉马努金', 'NB', '领域', '实践', '王小波', '孙悟空', '知识', '印度', '数学', '天才']
# 23
# ['伯克利', '戴夫', '去世', 'Facebook', '困境', '庆祝', '振作', '桑德伯格', '韧性', '普遍化']
# 24
# ['生意', '做事', '事情', '一定', '最好', '做到', '做成事', '高明', '精明', '洗衣服']
# 25
# ['记忆力', '大脑', '记忆', '维生素', '健脑', '咀嚼', '补脑', '不饱和脂肪酸', '血液', '花生酱']
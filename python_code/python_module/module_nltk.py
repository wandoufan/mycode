# nltk模块是用来对文本语言进行处理,更适用于英文,使用前需要先安装

# https://www.cnblogs.com/zephyr-1/p/6035310.html?utm_source=itdadao&utm_medium=referral
# http://www.nltk.org/
# https://blog.csdn.net/zzulp/article/details/77150129

import nltk


# 弹出包管理界面，在管理器中可以下载语料，预训练的模型等
# nltk.download()

# NLP分享PPT中出现过的用法
# t0 = nltk.DefaultTagger(str_1)
# t1 = nltk.UnigramTagger(trian_sents, backoff=t0)
# t2 = nltk.BigramTagger(trian_sents, backoff=t1)
# t2.evaluate(test_sents)

str_1 = "At eight o'clock on Thursday morning Arthur didn't feel very good."

# 对给定的文本进行切词分割，返回由分割的字词组成的列表
seg_list = nltk.word_tokenize(str_1)
print('\\ '.join(seg_list))

# 标注每个字词的词性
# 词性对照表：https://blog.csdn.net/john159151/article/details/50255101
tags = nltk.pos_tag(seg_list)
for i, j in tags:
	print(i,j)

# 识别命名实体
entities = nltk.chunk.ne_chunk(tags)
print(entities)

# 展示一个解析树
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()

# 将英文单词还原为一般形式
# 例如：复数->单数(cars->car)、被动->主动(fantasized->fantasize)、(reading->read)
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize(word))
# 该方法有可选参数pos,如果能指定单词的词性，还原结果会更准
print(lemmatizer.lemmatize('fantasized',pos='v'))

# 实现ngram模型
# ngrams(generation, len)方法，可以将可迭代对象切割成所有可能的长度为len的子部分
# generation参数是列表/字符串等类型的语料
# len参数是指定要切割的长度
from nltk.util import ngrams
from collections import Counter
str1 = '1234567891234561234123'
for i in range(5):
    b = ngrams(str1, i)# 即bigram模型
    for j in b:
        print(j)
# 感觉该方法只是一个简单的切分脚本，并没有实现Ngram的定义，没有实现预测的功能？
# 后续还需要自己再对函数结果按照出现频率进行统计？？
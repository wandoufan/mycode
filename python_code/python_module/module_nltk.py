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
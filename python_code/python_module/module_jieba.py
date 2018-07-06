# encoding=utf-8

# jieba模式是用来对文本语言分词等处理,更适用于中文,使用前要先安装
# 文档：https://github.com/fxsjy/jiebademo


# jieba模块的三种分词模式：
# 1.精确模式，试图将句子最精确地切开，适合文本分析；
# 2.全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
# 3.搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。


# jieba模块的算法：
# 基于前缀词典实现高效的词图扫描，生成句子中汉字所有可能成词情况所构成的有向无环图 (DAG)
# 采用了动态规划查找最大概率路径, 找出基于词频的最大切分组合
# 对于未登录词，采用了基于汉字成词能力的 HMM 模型，使用了 Viterbi 算法


# jieba模块中一些概念：
# TF:即(term frequency)词频，指的是某一个给定的词语在该文件中出现的次数。
# TF包含两类，在本文档的词频以及单词在所有文档的词频。

# IDF：即(inverse document frequency)逆向文件频率，是一个词语普遍重要性的权重度量。
# 某一特定词语的IDF，可以由总文件数目除以包含该词语之文件的数目，再将得到的商取对数得到。 

# TF-IDF:即(term frequency–inverse document frequency),是用于信息搜索和信息挖掘的常用加权技术
# TF-IDF用来评估一个字词对于一份文件/文件集的重要程度。
# 字词的重要程度与在文件中的词频TF成正比，与它在整个语料库中出现频率IDF成反比。
# 即字词的权重TF-IDF=TF*IDF

# 词性：把每个词按照形容词，动词，名词等标准进行分类。
# 词性标注的关键问题是消除歧义，因为同一个词在不同的语义下有不同的词性
# 词性对照表：https://blog.csdn.net/kevin_darkelf/article/details/39520881

# 分词粒度：对字符串进行分词切分时的颗粒度大小。如果分词粒度过大，
# 会使该被切分的词没被切分，如果粒度过小，会使不该被切分的词被切分。

# 窗口：每个词的具体意思经常会依赖于上下文来理解，窗口值k就代表围绕
# 目标词左右两侧每侧k个词来理解这个词的具体含义。

# 词向量：是一个用来表示词意思的向量，意思越接近的词在空间中的位置越接近
# 词向量中的数字表示了这个词在各个维度的权重。简单来讲，每个维度都代表了一个意思，
# 这个维度上的数字权重代表了这个词汇与这个意思的接近程度，因此可以通过加减计算获得意思接近的词
# 词向量(Word Vector)一般被看做是文档的特征，不同的词向量有不同的用法
# 常见的四类词向量：Hash算法及延伸、bow算法延伸、word2vec延伸、LDA主题延伸。
# https://blog.csdn.net/sinat_26917383/article/details/52162589
# https://www.sohu.com/a/201458880_693397


import jieba


# 1.分词
# a.产生generator结果
# jieba.cut(target_str, cut_all=False, HMM=False) ,接收三个参数，第一个为要进行分词
# 的字符串，第二个参数控制全模式/精确模式(默认)，第三参数控制是否使用HMM模型
# jieba.cut_for_search(target_str, HMM=False),接收两个参数，分词的字符串和是否使用HMM模式
# 第二个方法粒度较细，更适用于搜索引擎
str_1 = '我来到了北京清华大学'
seg_list = jieba.cut(str_1, cut_all=True)#全模式
print('result:'+'/'.join(seg_list))
seg_list = jieba.cut(str_1, cut_all=False)#精确模式
print('result:'+'/'.join(seg_list))
seg_list = jieba.cut_for_search(str_1)#搜索引擎模式
print('result:'+'/'.join(seg_list))
# jieba.cut以及jieba.cut_for_search方法返回的结果都是一个可迭代的
# generator类型，可以使用for循环逐个输出结果

# b.产生列表结果
# jieba.lcut和jieba.lcut_for_search方法返回的结果都是列表，可以直接输出
seg_list = jieba.lcut(str_1)
print(seg_list)
seg_list = jieba.lcut_for_search(str_1)
print(seg_list)


# 2.设置词典
# a.添加新词典
# 开发者可以指定自己自定义的词典，以便包含 jieba 词库里没有的词。
# (虽然 jieba 有新词识别能力，但是自行添加新词可以保证更高的正确率)
# jieba.load_userdict(dict_file)，加载用户自定义的词典文件
# 词典格式和jieba模块自带的dict.txt文件一样，一个词占一行；
# 每一行分三部分:词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒。
# 注意：词典的txt文本必须保存为 UTF-8 编码格式。	
str_2 = '李小福是创新办主任也是云计算方面的专家'
seg_list = jieba.cut(str_2)
print('before:'+'/'.join(seg_list))
jieba.load_userdict('D:/user_dict.txt')
seg_list = jieba.cut(str_2)
print('after: '+'/'.join(seg_list))

# b.修改词典
# jieba.add_word(word, freq=None, tag=None)和jieba.del_word(word)可在程序中动态修改词典。
# jieba.suggest_freq(segment, tune=True)可以调节单个词语的词频，使其能/不能被识别出来
str_3 = '如果放到post中将出错。'
seg_list = jieba.cut(str_3)
print('before:'+'/'.join(seg_list))
jieba.suggest_freq(('中', '将'), True)
seg_list = jieba.cut(str_3)
print('after: '+'/'.join(seg_list))
str_4 = '台中应该不会被切开'
seg_list = jieba.cut(str_4)
print('before:'+'/'.join(seg_list))
jieba.suggest_freq('台中', True)
seg_list = jieba.cut(str_4)
print('after: '+'/'.join(seg_list))


# 3.关键词抽取
# a.基于 TF-IDF 算法的关键词抽取
# jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
# 返回由元组组成的字典，其中元组由关键词和权重两个元素组成
# 其中，sentence 为待提取的文本,topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
# withWeight 为是否一并返回关键词权重值，默认值为 False,allowPOS 仅包括指定词性的词，默认值为空，即不筛选
str_5 = '此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，\
吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。\
目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。'
import jieba.analyse# 使用方法前要单独导入该模块
print('------------------------------------------------')
for x, w in jieba.analyse.extract_tags(str_5, withWeight=True):
    print(x, w)
print('------------------------------------------------')

# b.基于 TextRank 算法的关键词抽取
# jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v')) 
# 返回由元组组成的字典，其中元组由关键词和权重两个元素组成
for x, w in jieba.analyse.textrank(str_5, withWeight=True):
    print(x, w)
print('------------------------------------------------')


# 4.词性标注
# a.标注词性
# jieba.posseg.cut(string)将制定字符串进行分割，并标注出每个词的词性
import jieba.posseg# 使用方法前要单独导入该模块
str_6 = '我爱北京天安门和姚明'
words = jieba.posseg.cut(str_6)
for word, flag in words:
	print(word, flag)
print('------------------------------------------------')
# jieba.posseg.cut方法返回的结果是可迭代的generator类型，可以使用for循环逐个输出结果

# b.修改分词器
# jieba.posseg.POSTokenizer(tokenizer=None)新建自定义分词器，
# tokenizer参数可指定内部使用的jieba.Tokenizer分词器。
# jieba.posseg.dt为默认词性标注分词器。


# 5.并行分词
# 将目标文本按行分隔后，把各行文本分配到多个 Python 进程并行分词，
# 然后归并结果，从而获得分词速度的可观提升
# 基于 python 自带的 multiprocessing 模块来实现并发进程

# a.jieba.enable_parallel(num)
# 开启并行分词模式，num参数为并行进程数

# b.jieba.disable_parallel()
# 关闭并行分词模式
# 注意：并行分词仅支持默认分词器jieba.dt和jieba.posseg.dt


# 6.返回词语在原文的起止位置
# a.默认模式
# 注意：输入的参数只接受unicode编码格式
str_7 = u'永和服装饰品有限公司'
result = jieba.tokenize(str_7)
# jieba.tokenize方法返回的结果是由元组组成的可迭代的generator类型
# 其中元组由关键词，起始位置，结束位置三个元素组成
for i in result:
	print(i)
print('------------------------------------------------')

# b.搜索模式
result = jieba.tokenize(str_7, mode='search')
for i in result:
	print(i)
print('------------------------------------------------')


# 7.搜索引擎
pass


# 8.命令行分词
# 用于在linux环境下使用jieba命令进行分词
# 'python -m jieba [options] filename'
# 具体参数包括：
# -d [DELIM], --delimiter [DELIM]
# 使用 DELIM 分隔词语，而不是用默认的' / '。若不指定 DELIM，则使用一个空格分隔。
# -p [DELIM], --pos [DELIM]
# 启用词性标注；如果指定 DELIM，词语和词性之间用它分隔，否则用 _ 分隔
# -D DICT, --dict DICT  使用 DICT 代替默认词典
# -u USER_DICT, --user-dict USER_DICT
# 使用 USER_DICT 作为附加词典，与默认词典或自定义词典配合使用
# -a, --cut-all  全模式分词（不支持词性标注）
# -n, --no-hmm  不使用隐含马尔可夫模型
# -q, --quiet  不输出载入信息到 STDERR
# -V, --version   显示版本信息并退出
# 关键词抽取

## 参考资料
> https://blog.csdn.net/mpk_no1/article/details/75201546  
> http://python.jobbole.com/82230/  
> https://baijiahao.baidu.com/s?id=1591759412102633028&wfr=spider&for=pc  
> https://www.jb51.net/article/126423.htm

## 定义
关键词抽取又称为智能标签，可以从一篇文本中抽取出最能代表这篇文章的词  

## 分类方式
1.抽取式  
统计文本中各个词的词频等各种属性值，根据一定的规则和算法得到关键词，这种方式要求关键词出现在文本中且具有较高的词频。这种算法并没有真正理解文章意思，无法获得文章中未出现过的关键词，有一定的局限性。  
2.生成式  
在理解文章语义的基础上重新概括生成关键词，得到的关键词可能没有在文本中出现过，实现难度较高  

## 常用方法

### TF-IDF算法
TF:即(term frequency)词频，指的是某一个给定的词语在该文件中出现的次数。  
TF包含两类，在本文档的词频以及单词在所有文档的词频。  
TF= 词在文档中出现的次数 / 文章总词数  

IDF：即(inverse document frequency)逆向文件频率，是一个词语普遍重要性的权重度量。  
某一特定词语的IDF，可以由语料库中文件总数目除以包含该词语之文件的数目，再将得到的商取自然对数得到。  
IDF= ln(语料库中文档总数/包含该词的文档数)  
备注：定义中是对商取10的对数，即IDF=log10(语料库中文档总数/包含该词的文档数),底的具体取值没有明确规定  

TF-IDF:即(term frequency–inverse document frequency),是用于信息搜索和信息挖掘的常用加权技术  
TF-IDF用来评估一个字词对于一份文件/文件集的重要程度，即字词的权重，常用于关键词抽取  
字词的重要程度与在文件中的词频TF成正比，与它在整个语料库中出现频率IDF成反比。  
计算公式为：TF-IDF=TF×IDF  

### topic-model

### RAKE算法

### jieba工具

### TextRank算法

## 关键词结果的判定
如何判断关键词抽取结果是否准确是目前结果判定的一个难点，因为关键词本身带有很大的主观性  
对于一篇文章很难有明确的标准去界定一个候选词是否是该文章的关键词  

## 项目
1.讯飞语音笔记智能标签项目  
利用关键词抽取从中文笔记中抽取出若干关键词来作为这篇笔记的标签，具体语料数据由讯飞方面提供。  
在TF-IDF算法的基础上，使用新词发现来找到分词工具无法得到的短语(字长4-6之间)，
利用词性判定，实体质量判定，停用字词过滤，话题词加权等手段对结果进行修正，准确率在85%-90%之间。
2.国道论文关键词项目  
从英文论文中抽取出若干最能代表该论文的单词或词组作为该论文的关键词  

## 处理流程
1. 初始化  
1.1 根据文本长度确定候选词最小出现次数  
1.2 检测文本中是否有《》中的电影名，书名，歌曲名等，如果有就后续单独进行处理  
1.3 对文本进行分词，分词结果作为候选关键词  
1.4 对文本进行新词发现，新词发现结果同样补充为候选关键词  

2. 候选关键词初步过滤  
利用各种规则及词表对不合法的候选关键词进行过滤，具体包括：  
2.1 英文停用词过滤  
2.2 长度过短或过长候选词过滤  
2.3 含非法符号的候选词过滤  
2.4 特殊badcase过滤  
2.5 左右非法停用字过滤  

3. 候选关键词分数计算  
3.1 tf-idf分数计算  
TF-IDF=TF×IDF  
3.2 评估实体质量分数  
调用实体质量评估模块评估出候选词的实体质量分数，一般认为关键词是实体词的概率更高  
3.3 评估词性分数  
调用词性判定模块评估候选词的词性，一般认为关键词是名词的概率更高  
3.4 由以上三部分分数获取综合分数  
3.5 利用分数阈值过滤掉分数过低的候选词  

4. 对候选词分数进行加权/减权  
4.1 对符合话题词表的候选词进行加权  
从知乎上爬取了几千个话题列表，一般认为话题词成为关键词的概率更高  

5. 对文本出现在《》中的电影名，书名，歌曲名等特殊词进行计算  
5.1 计算过程与第3部分一致，但对最小词频、最小分数等阈值要求更低  
5.2 将计算结果与上述结果合并  

6. 在候选词中去除具有相同开头/结尾的关键词  
候选词中可能有很多重复的，例如'共享'和'共享单车'，要进行去重操作  

7. 按分数对结果进行排序，并返回分数最高的若干关键词  


## 算法优化细节
1. 由于分词系统的分词颗粒度较细，一些组合词可能会被切分开，例如'共享单车'会被分成'共享'和'单车'，对文本使用新词发现可以获得一些组合词  

2. 对非常大量的语料进行分词可以得到一个全局字典文件，因此字典文件非常大  
全局字典读取到内存要占用大量内存，每次从字典中查询一个候选词也要花费很多时间  
分析字典文件词频也符合二八原则，大部分词只出现很少次数，只有少部分词会出现很多次数  
因此可以只保留字典文件中的高频词汇，字典文件会大大缩小，程序运行效率也提高了很多  
对于没有记录在字典文件中的候选词，候选词的idf值可以设定为一个固定值  
这个做法会损失一些准确度，但可以大大减少程序运行的时间和内存消耗  
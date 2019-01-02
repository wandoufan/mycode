# N-Gram语言模型

## 参考资料
> https://blog.csdn.net/ahmanz/article/details/51273500
> https://yiyibooks.cn/yiyi/nltk_python/index.html

## 简要介绍
N-Gram是一种大量连续词汇识别中的一种常用统计语言模型，即根据前(n-1)个item来预测第n个item  
N=1时称为unigram，N=2称为bigram，N=3称为trigram，其中，N代表依赖范围，即依赖于前N-1个字符；  
另外还有four-gram、five-gram等，但应用很少，因为训练需要更多的语料，但会有更严重的数据稀疏问题  
即如果一个词的出现仅依赖于前面的一个词，称为bigram;如果一个词的出现仅依赖于前面的两个词，称trigram;  
在应用层面，这些item可以是音素（语音识别应用）、单字符（输入法应用）、词（分词应用）或碱基对（基因信息）  
一般来讲，可以从大规模文本或音频语料库中生成n-gram模型，语料规模越大，模型越准确  

## 相关概念
马尔科夫假设理论：一个item的出现概率，只与其前面n个items有关  
最大似然估计：  

## 应用场景
* 输入法  
* 语音识别  
* 分词算法  
* 机器翻译  

## 相关库
* nltk

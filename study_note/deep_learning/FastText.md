# fasttext

## 基本概念
fasttext是facebook开源的一个词向量与文本分类工具，典型应用场景是带监督的文本分类问题  
fasttext提供简单而高效的文本分类和表征学习的方法，性能比肩深度学习而且速度更快  

## fasttext模型和卷积神经网络/CNN模型的区别：
与深层的CNN模型相比，fastText的模型结构是浅层的  
fastText模型远远快于CNN模型，fastText在更大规模的数据集(标签成千上万)上的优势更加明显  

## fastText和word2vec的比较：
1. fastText的架构和word2vec中的CBOW的架构类似，fastText也算是words2vec所衍生出来的，而且两个模块都是同一作者写出来的  
2. 相似处：
图模型结构很像，都是采用embedding向量的形式，得到word的隐向量表达。
都采用很多相似的优化方法，比如使用Hierarchical softmax优化训练和预测中的打分速度。
3. 不同处：  
模型的输出层：word2vec的输出层，对应的是每一个term，计算某term的概率最大；
而fasttext的输出层对应的是分类的label；
不过不管输出层对应的是什么内容，其对应的vector都不会被保留和使用；
模型的输入层：word2vec的输出层，是 context window 内的term；
而fasttext对应的整个sentence的内容，
包括term，也包括 n-gram的内容；
两者本质的不同，体现在 h-softmax的使用：
Wordvec的目的是得到词向量，该词向量 最终是在输入层得到，输出层对应的h-softmax 
也会生成一系列的向量，但最终都被抛弃，不会使用。
fasttext则充分利用了h-softmax的分类功能，遍历分类树的所有叶节点，找到概率最大的label（一个或者N个）

## fastText方法包含三部分:模型架构，层次SoftMax和N-gram特征
1. 单个词或者ngram组合词的词向量取平均后代表该文本的向量，
2. 使用softmax函数预测文本所属各标签类别的概率，损失函数 (Loss function) 
3. 是真实标签类别与预测标签类别之间的负对数似然 (Negative log-likelihood)


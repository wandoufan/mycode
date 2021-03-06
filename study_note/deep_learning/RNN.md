# 循环神经网络(recurrent neural network, RNN)


## 参考资料
> https://www.cnblogs.com/buptzym/p/5437973.html


## 基本概念
循环神经网络是一类以序列数据为输入，在序列的演进方向进行递归且所有节点按链式连接的递归神经网络  


## 应用场景
RNN通过挖掘数据中的时序信息，来处理和预测前后数据有关联的序列化数据  
常见序列化数据包括视频、音频、文本序列等  
RNN常用于语音识别、语言模型、机器翻译以及时序分析等方面  
例如对一个句子中每个词进行词性标注时，每个词的前后位置词都会相互影响各自的词性，因此可以用RNN来处理  


## 循环神经网络模型的特点  
1. RNN的输入值是前后数据有关联的序列化数据  
2. RNN隐藏层的输入不仅包括本次给出的输入值，还包括上一次迭代时隐藏层的输出值  
即RNN相比普通的神经网络多了一个权重矩阵，用来设置上一次隐藏层值作为本次输入的权重  
3. 基础神经网络只在输入层、隐藏层、输出层之间建立了层与层之间的权重值连接  
而RNN可以在隐藏层的每个神经元之间都建立权重值连接  


## 循环神经网络的缺点
RNN也存在梯度消失的问题，当输入序列很长的时候问题尤其严重，因此RNN模型一般不直接使用于应用领域  


## 循环神经网络的参数更新方法
1. BPTT(back-propagation through time)算法  
BPTT即随时间反向传播算法，是常用的训练RNN的方法，本质上还是BP算法  区别在于RNN处理的时间序列数据，所以要基于时间反向传播  
BPTT的中心思想和BP算法相同，沿着需要优化的参数的负梯度方向不断寻找更优的点直至收敛  
2. 实时循环学习（real-time recurrent learning，RTRL）  
RTRL算法则是使用前向传播的方式来更新梯度  


## 常见RNN
1. LSTM(Long Short-Term Memory)长短期记忆神经网络  
LSTM也是一种循环神经网络，适合于处理和预测时间序列中间隔和延迟相对较长的重要事件，记忆时间更长  
LSTM是为了解决一般的RNN无法处理长距离的依赖的问题而专门设计出来的，可以避免常规RNN的梯度消失问题  
2. 门控制循环单元（GRU）

3. SRNN(Sliced recurrent neural networks)切片循环神经网络
传统RNN的隐藏层中神经元的输入依赖于上一神经元的输出，每一步计算都需要等待上一步计算完成，很难实现并行化处理  
SRNN是一种性能优化版的循环神经网络，在不改变循环单元的情况下，比RNN结构快135倍  
SRNN基于RNN结构进行改良，将输入序列切成等长的最小子序列，这样循环单元就可以在每一层的每一个子序列中同时运行  


## CNN和RNN的比较
1. 处理的数据  
CNN主要处理图像，RNN主要处理视频、音频、文本等序列化数据  
2. 扩展方式  
CNN在空间上进行扩展，RNN在时间上进行扩展  
3. 连接方式  
RNN是全连接的，CNN不是全连接的  
4. 输出方式  
RNN是具有记忆功能的连续输出，而CNN是静态输出  
5. NLP应用  
RNN可以用来做词性标注，CNN可以用来做文本分类  
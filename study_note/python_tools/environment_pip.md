# pip

## 简介
pip是用来管理python包的一款工具，可以实现包的安装、更新、管理  
pip是python官方的包管理工具，拥有最全最新的python包  


## conda和pip的对比
二者都是包管理器，可以实现包的安装、更新、卸载，但二者还有很多不同点  
1. 支持的语言
pip只能用来安装python的包，不支持python语言以外的依赖项  
conda虽然大部分包也都是python的，但还支持一些其他语言，如cuda这种C++写的包  
2. 安装的包
pip安装的是python wheel或者源代码的包，需要有编译器的支持，系统中没有编译器时可能会安装失败  
conda安装的是已经编译好的二进制包，不需要编译器，但conda安装的包一般比较大，可能几百M甚至1G多  
3. 管理环境
pip只能实现包的管理功能，如果想要实现环境管理，还需要额外安装virtualenv  
conda带有管理环境的功能，可以轻松管理多个版本的python  
4. python解释器
pip必须在安装好python解释器之后才能使用  
conda不需要实现安装python解释器，甚至可以用conda来下载安装python解释器  
5. 依赖检查
pip依赖检查不严格  
conda具有严格的依赖检查  
6. 包资源
pip的包资源为PyPI，Python的包会被优先发布到PyPI上  
conda的包资源为Anaconda，包数量远少于PyPI  
7. 总结
建议优先用conda来管理，如果conda没有再使用pip安装  
如果使用GPU进行机器学习，用到了CUDA、TensorFlow、PyTorch等库，建议使用conda  
备注：pip的包跟conda不完全重叠，有些包只能通过其中一个装  


## windows下安装pip
备注：需要提前安装好python环境
https://www.cnblogs.com/baiyuer/p/9606773.html
1. 下载pip压缩包
2. 安装pip
```
python setup.py install
```
3. 添加pip环境变量
```
C:\Users\XYF\AppData\Local\Programs\Python\Python36\Scripts
```


## Linux下安装pip
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
在linux中还可以通过下载安装包的方式来安装  
```
git clone https://github.com/liu946/goo.git
cd goo
(sudo) ./install.sh
```


## pip本身的更新
Linux或macOS平台  
```
pip install -U pip
```
Windows平台  
```
python -m pip install -U pip
```


## pip常用命令
备注：以下命令在windows和Linux平台下都可以使用  
1. 安装指定的python包
```
pip install package
```
2. 卸载指定的python包
```
pip uninstall package
```
3. 查看指定python包的详细信息
```
pip show package
```
4. 查看当前环境中的python包列表
注意：查看到的都是安装的第三方包，不包含python内置的库  
```
pip list
```
5. 查看可以进行更新的包
```
pip list --outdated
pip list -o
```


## pip一次安装多个包
把项目需要的依赖包都写入一个requirements.txt的文本中，然后一次性安装  
```
pip install -r C:\requirements.txt
```
requirements.txt文本中格式为package_name==version，例如：  
```
cffi==1.12.3
gevent==1.4.0
greenlet==0.4.15
pycparser==2.19
six==1.12.0
websocket==0.2.1
websocket-client==0.56.0
```


## pip安装超时
安装包时可能存在网络状况不好导致time out，可以手动延长超时时间  
```
pip --default-timeout=100 install pandas
```
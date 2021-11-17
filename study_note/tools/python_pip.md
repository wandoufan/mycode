# pip

## 简介
pip是用来安装python包的一款工具  


## windows下安装pip
备注：需要提前安装好python环境
https://www.cnblogs.com/baiyuer/p/9606773.html
1. 下载pip压缩包
2. 安装pip
```
python setup.py install
```
3. 添加pip环境变量


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